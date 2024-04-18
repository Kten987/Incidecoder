import requests
from bs4 import BeautifulSoup

# Lấy thông tin chi tiết sản phẩm, output lưu vào dict
def get_product_details(url) -> dict:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # create emtpy result 
    result = {}

    if response.status_code == 200:
        result['Link incidecoder'] = url

        # Lấy tên brand, đk: id "product-brand-title"
        brand_element = soup.find("span", id="product-brand-title")
        # Nếu ko có brand thì trả về ""
        if brand_element:
            result['brand'] = brand_element.get_text(strip=True)
        else:
            result['brand'] = ""

        # Lấy product_name, đk: id "product-title"
        title_element = soup.find("span", id="product-title")
        if title_element:
            result['short_product_name'] = title_element.get_text(strip=True)
        else:
            result['short_product_name'] = ""

        # Lấy description, đk: id "product-details"
        element = soup.find(id="product-details")
        if element:
            result['incide_enDescription'] = element.get_text()
        else:
            result['incide_enDescription'] = ""

        # Lấy mô tả thành phần, đk: id "ingredlist-short"
        ingredlist_element = soup.find(id="ingredlist-short")
        if ingredlist_element:
            result['incide_ingredients'] = ingredlist_element.get_text()
        else:
            result['incide_ingredients'] = ""

        # Lấy link ảnh, đk: id "product-main-image"
        div_element = soup.find("div", id="product-main-image")
        img_element = div_element.find("img")

        result['incide_imageKey'] = img_element["src"]
        result["process"] = "Success"
    else:
        result['Link incidecoder'] = url
        result['brand'] = ""
        result['short_product_name'] = ""
        result['incide_enDescription'] = ""
        result['incide_ingredients'] = ""
        result['incide_imageKey'] = ""
        result["process"] = "Failed"

    return result

if __name__ == "__main__":
    test = get_product_details("https://incidecoder.com/products/pyunkang-yul-low-ph-pore-deep-cleansing-foam-4")
    print(test["incide_imageKey"])
