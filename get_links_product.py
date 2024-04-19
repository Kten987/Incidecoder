import requests
from bs4 import BeautifulSoup
import unidecode

# convert product name sang dạng từ khóa, ví dụ: Pyunkang Yul Cleansing Foam -> Pyunkang+Yul+Cleansing+Foam 
def convert_productname(product_name):
    product_name = unidecode.unidecode(product_name)
    product_name = product_name.replace(" ", "+")
    return product_name

# Đưa ra danh sách link sản phẩm
def get_link_product(product_name) -> list[str]:

    url = "https://incidecoder.com/search/product?query=" + convert_productname(product_name)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    short_product_links = []
    # Lấy tất cả link sp, đk: class 'klavika simpletextlistitem'
    short_product_links = [link.get('href') for link in soup.find_all('a', class_='klavika simpletextlistitem')]
    # Nếu ko có link thì trả về None
    if short_product_links == []:
        product_links = ""
    else:
        product_links = ["https://incidecoder.com" + link for link in short_product_links][0] # chỉ lấy 1 link đầu tiên
    return product_links
    

if __name__ == "__main__":
    test = convert_productname("Pyunkang Yul Cleansing Foam")
    print(get_link_product(test))
