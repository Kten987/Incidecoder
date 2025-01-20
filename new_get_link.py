import requests
from bs4 import BeautifulSoup
import unidecode

# Đưa ra danh sách link sản phẩm
def get_link_product(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    short_product_links = []
    # Lấy tất cả link sp, đk: class 'klavika simpletextlistitem'
    short_product_links = [link.get('href') for link in soup.find_all('a', class_='klavika simpletextlistitem')]
    # Nếu ko có link thì trả về None
    if short_product_links == []:
        product_links = ""
    else:
        product_links = ["https://incidecoder.com" + link for link in short_product_links]
    
    return product_links
    

if __name__ == "__main__":
    print(get_link_product("https://incidecoder.com/search?query=Laikou"))