# Test untuk modul transform
import pandas as pd
from utils.extract import scrape_products
from utils.transform import transform_products

def test_transform_products_real():
    raw_products = scrape_products()
    df = transform_products(raw_products)

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    expected_columns = [
        "Title",
        "Price",
        "Rating",
        "Colors",
        "Size",
        "Gender",
        "timestamp"
    ]

    for col in expected_columns:
        assert col in df.columns