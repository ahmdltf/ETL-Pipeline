# Test untuk modul load
import pandas as pd
from utils.extract import scrape_products
from utils.transform import transform_products
from utils.load import (
    save_to_csv,
    save_to_postgresql,
    save_to_google_sheets,
    db_url
)

def test_save_to_csv_real():
    # Masukkan kode ini: test simpan CSV asli
    raw = scrape_products()
    df = transform_products(raw)

    save_to_csv(df, "test_products.csv")

    assert True


def test_save_to_postgresql_real():
    # Masukkan kode ini: test simpan PostgreSQL asli
    raw = scrape_products()
    df = transform_products(raw)

    save_to_postgresql(df, db_url)

    assert True


def test_save_to_google_sheets_real():
    # Masukkan kode ini: test simpan Google Sheets asli
    raw = scrape_products()
    df = transform_products(raw)

    save_to_google_sheets(
        df,
        spreadsheet_name="Dicoding ETL Submission"
    )

    assert True
