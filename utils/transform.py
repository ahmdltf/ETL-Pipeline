# Modul untuk transformasi data
import pandas as pd

USD_TO_IDR = 16000

def transform_products(raw_products):
    # Membersihkan dan mentransformasi data hasil ekstraksi
    try:
        df = pd.DataFrame(raw_products)

        # Menghapus data invalid
        df = df[df["Title"] != "Unknown Product"]

        # Menghapus nilai null
        df.dropna(inplace=True)

        # Membersihkan Price dan konversi ke rupiah
        df["Price"] = (
            df["Price"]
            .str.replace("$", "", regex=False)
            .astype(float)
            * USD_TO_IDR
        )

        # Membersihkan Rating
        df["Rating"] = (
            df["Rating"]
            .str.replace("/ 5", "", regex=False)
            .astype(float)
        )

        # Membersihkan Colors (contoh: "3 Colors" → 3)
        df["Colors"] = (
            df["Colors"]
            .str.replace(" Colors", "", regex=False)
            .astype(int)
        )

        # Membersihkan Size
        df["Size"] = df["Size"].str.replace("Size: ", "", regex=False)

        # Membersihkan Gender
        df["Gender"] = df["Gender"].str.replace("Gender: ", "", regex=False)

        df["timestamp"] = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")

        # Menghapus duplikat
        df.drop_duplicates(inplace=True)

        return df

    except (ValueError, KeyError, TypeError) as e:
            print(f"[ERROR] Gagal transformasi data: {e}")
            return pd.DataFrame()