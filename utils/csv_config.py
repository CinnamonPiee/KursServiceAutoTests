import csv
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from datetime import datetime
from dotenv import load_dotenv
import os


load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def convert_csv_to_xlsx(csv_file):
    """Конвертирует CSV в XLSX"""
    xlsx_file = csv_file.replace(".csv", ".xlsx")
    df = pd.read_csv(csv_file)
    df.to_excel(xlsx_file, index=False)
    return xlsx_file


def upload_to_google_drive(file_path):
    """Загружает файл на Google Диск"""
    scope = ["https://www.googleapis.com/auth/drive.file"]

    creds = Credentials.from_service_account_file(os.getenv("GOOGLE_API_CREDENTIALS"), scopes=scope)

    client = gspread.authorize(creds)

    drive_service = build("drive", "v3", credentials=creds)

    file_metadata = {
        "name": os.path.basename(file_path),
        "parents": ["1vQ9NZfk-dwiTsv7jV6q-z6w-PY7G08gu"]
    }

    media = MediaFileUpload(file_path, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id"
    ).execute()

    print(f"Файл загружен на Google Drive, ID: {file.get('id')}")


def log_csv_error(page_name: str, error_msg: str, url: str):
    """Записывает ошибки в CSV файл bug_reports/<page_name>/<YYYY-MM-DD>/errors.csv"""

    current_date = datetime.now().strftime("%Y-%m-%d")
    log_dir = os.path.join(BASE_DIR, "bug_reports", page_name, current_date)
    os.makedirs(log_dir, exist_ok=True)

    csv_file = os.path.join(log_dir, "errors.csv")

    file_exists = os.path.isfile(csv_file)

    with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Страница", "Ошибка", "URL"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), error_msg, url])
