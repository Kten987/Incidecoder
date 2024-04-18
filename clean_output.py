import pandas as pd
from out_put import input_product_name, get_output

def clean_columns(df,list_columns):
    for col in list_columns:
        df[col] = df[col].str.strip() # xóa khoảng trắng ở 2 đầu 
        df[col] = df[col].str.replace(r"\[more\]|\[less\]", "", regex=True) # xóa các chuỗi [more] và [less]
        df[col] = df[col].str.replace(r"\s{2,}", " ", regex=True) # xóa các khoảng trắng dư thừa

def clean_output(source = "Thinh_Assignment.csv"):
    input_df = input_product_name(source)
    df = get_output(input_df)
    # clean columns
    clean_columns(df, ["incide_enDescription", "incide_ingredients"])
    df["incide_productName"] = df["brand"] + " " + df["short_product_name"]
    df["isTrue_productName"] = df["productName"] == df["productName_clean"]
    return df

if __name__ == "__main__":
    t = clean_output("Product Data incidecoder - 8.csv")
    t.to_csv("output_sheet8.csv", index=False)
