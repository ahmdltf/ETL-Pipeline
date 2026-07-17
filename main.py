# File utama untuk menjalankan aplikasi
from utils.extract import scrape_products
from utils.transform import transform_products
from utils.load import (
    save_to_csv,
    save_to_google_sheets,
    save_to_postgresql,
    db_url
)

def main():
    # Menjalankan seluruh proses ETL pipeline
    try:
        raw_products = scrape_products()
        clean_df = transform_products(raw_products)

        save_to_csv(clean_df)

        save_to_google_sheets(
            clean_df,
            spreadsheet_name="Dicoding ETL Submission"
        )

        db_config = {
            "host": "localhost",
            "database": "etl_db",
            "user": "postgres",
            "password": "pass"
        }

        save_to_postgresql(clean_df, db_url)


        print("ETL pipeline selesai.")
    except Exception as e:
        print(f"[FATAL] ETL pipeline gagal dijalankan: {e}")

if __name__ == "__main__":
    main()
