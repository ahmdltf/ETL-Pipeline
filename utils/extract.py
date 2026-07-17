# Modul untuk ekstraksi data
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Header untuk menghindari blocking server
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    )
}

def fetching_content(url):
    # Mengambil halaman HTML dari website
    session = requests.session()
    response = session.get(url)

    if response.status_code == 200:
        return response.content
    else:
        raise Exception("Failed to fetch content")

def parse_product_info(paragraphs):
    # Mengekstrak rating, colors, size, dan gender dari tag <p>
    data = {"Rating": None, "Colors": None, "Size": None, "Gender": None}

    try:
        for p in paragraphs:
            text = p.text.strip()

            if text.startswith("Rating"):
                data["Rating"] = text.replace("Rating:", "").replace("⭐", "").strip()
            elif "Colors" in text:
                data["Colors"] = text
            elif text.startswith("Size"):
                data["Size"] = text
            elif text.startswith("Gender"):
                data["Gender"] = text
    except AttributeError as e:
        print(f"[ERROR] Gagal parsing informasi produk: {e}")

    return data

def extract_products_from_page(html):
    # Mengekstrak data produk dari satu halaman HTML
    products = []

    if html is None:
        return products

    try:
        soup = BeautifulSoup(html, "html.parser")
        cards = soup.find_all("div", class_="collection-card")
        extraction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for card in cards:
            title = card.find("h3", class_="product-title")
            price = card.find("span", class_="price")
            paragraphs = card.find_all("p")

            parsed = parse_product_info(paragraphs)

            products.append({
                "Title": title.text.strip() if title else None,
                "Price": price.text.strip() if price else None,
                "Rating": parsed["Rating"],
                "Colors": parsed["Colors"],
                "Size": parsed["Size"],
                "Gender": parsed["Gender"],
                "timestamp": extraction_time
            })
    except Exception as e:
        print(f"[ERROR] Gagal mengekstrak produk dari halaman: {e}")

    return products

def scrape_products():
    # Mengekstrak seluruh data produk dari halaman 1 sampai 50
    all_products = []

    for page in range(1, 51):
        try:
            url = (
                "https://fashion-studio.dicoding.dev/"
                if page == 1
                else f"https://fashion-studio.dicoding.dev/page{page}"
            )
            html = fetching_content(url)
            products = extract_products_from_page(html)
            all_products.extend(products)
        except Exception as e:
            print(f"[ERROR] Gagal memproses halaman {page}: {e}")

    return all_products

def get_text_or_none(element):
    # Mengambil teks dari elemen HTML atau None jika elemen tidak ada
    return element.text.strip() if element else None
