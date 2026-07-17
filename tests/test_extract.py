# Test untuk modul extract
from utils.extract import scrape_products

def test_scrape_products_real():
    # Masukkan kode ini: test scraping asli
    products = scrape_products()

    assert isinstance(products, list)
    assert len(products) > 0