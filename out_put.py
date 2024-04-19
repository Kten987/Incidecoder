import pandas as pd
from get_links_product import convert_productname, get_link_product
from craw import get_product_details
import time
import re

def input_product_name(source = "Thinh_Assignment.csv"):
    df = pd.read_csv(source) # giữ nguyên giá trị duplicate
    product_name_list = df["productName"].tolist()

    return product_name_list

list_output = []
def get_output(product_name_list):
    # Duyệt qua từng tên sản phẩm trong list
    len_list = len(product_name_list)
    for product_name in product_name_list:

        # Thứ tự prodcut hiện tại
        count_product_processing = product_name_list.index(product_name) + 1
        if count_product_processing % 25 == 0:
            time.sleep(3)
            print(f"Done {product_name} -- estimated: {count_product_processing*100 /len_list}% -- products left: {len_list - count_product_processing}")
        # Clean product name, ex: The Auragins Glow Complexion Serum 14% Vitamin C ... -> The Auragins Glow Complexion Serum
        productName_clean = re.split("\d+\.\d+%|\d+%", product_name)[0].strip()

        # Get product links
        product_links = get_link_product(convert_productname(productName_clean))
        try:
            if product_links == "":
                list_output.append({"productName": product_name, "productName_clean": productName_clean , "process": "None link found"})
            else:
                out_put = get_product_details(product_links)
                out_put["productName"] = product_name
                out_put["productName_clean"] = productName_clean
                list_output.append(out_put)
                
        except Exception as e:
            print(f"Error: {e} because of {product_name}")
        

    df_output = pd.DataFrame(list_output)
    return df_output

if __name__ == "__main__":
    product_name_list = input_product_name()
    df_output = get_output(product_name_list)
    df_output.to_csv("output_4.csv", index=False)
