# Modul untuk loading data
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
from sqlalchemy import create_engine

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
db_url = "postgresql+psycopg2://postgres:pass@localhost:5432/etl_db"

def save_to_csv(df, filename="products.csv"):
    # Menyimpan data hasil transformasi ke file CSV
    try:
        df.to_csv(filename, index=False)
        print(f"[INFO] Data berhasil disimpan ke {filename}")
    except Exception as e:
        print(f"[ERROR] Gagal menyimpan CSV: {e}")

def save_to_google_sheets(df, spreadsheet_name, worksheet_name="Sheet1"):
    # Masukkan kode ini: simpan data ke Google Sheets (Service Account, clean)
    try:
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = Credentials.from_service_account_file(
            "google-sheets-api.json",
            scopes=scopes
        )

        client = gspread.authorize(creds)

        spreadsheet = client.open(spreadsheet_name)

        # Buat worksheet jika belum ada
        if worksheet_name not in [ws.title for ws in spreadsheet.worksheets()]:
            worksheet = spreadsheet.add_worksheet(
                title=worksheet_name,
                rows=1000,
                cols=20
            )
        else:
            worksheet = spreadsheet.worksheet(worksheet_name)

        worksheet.clear()

        # Update data
        worksheet.update(
            [df.columns.tolist()] + df.astype(str).values.tolist()
        )

        print("[INFO] Data berhasil disimpan ke Google Sheets")

    except Exception as e:
        print(f"[ERROR] Gagal menyimpan ke Google Sheets: {repr(e)}")

def clean_encoding(df):
    for col in df.select_dtypes(include="object").columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.encode("utf-8", errors="ignore")
            .str.decode("utf-8")
        )
    return df

def save_to_postgresql(df: pd.DataFrame, db_url: str, table_name="products"):
    try:
        engine = create_engine(db_url)

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print("[INFO] Data berhasil disimpan ke PostgreSQL")

    except Exception as e:
        print(f"[ERROR] Gagal menyimpan ke PostgreSQL: {e}")
