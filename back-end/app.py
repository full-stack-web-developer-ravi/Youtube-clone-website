import requests
from bs4 import BeautifulSoup
import csv
import pandas as p


url = "https://www.flipkart.com/search?q=mobiles"
# url = "https://www.flipkart.com/"
# url = "https://learning.ccbp.in/frontend-development/course?c_id=80afae69-e9c6-4c29-ab24-ea4495213e9f&"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")


title = soup.find_all(
    "div", class_="_2kHMtA")
# images = soup.find_all('div', class_="CXW8mj")
# # brand = soup.find_all("div", class_="_2WkVRV")
# # ratings = soup.find_all('span', class_='_2_R_DZ')
# details = soup.find_all('div', class_='_3khuHA')
# # price = soup.find_all('div', class_='_30jeq3 _1_WHN1')
# # discount_price = soup.find_all('div', class_="_3I9_wc _27UcVY")
# discount_percent = soup.find_all('div', class_='_2tDhp2')


for i in title:
    print(i.text)

# title_list = []
# img_list = []
# # # brand_list = []
# # ratings_list = []
# details_list = []
# # price_list = []
# # discount_price_lits = []
# discount_percentage_list = []

# for title, img, detail, discount_percentage in zip(title, images, details, discount_percent):

#     title_list.append(title.text)
#     img_list.append(img.img['src'])
#     # brand_list.append(brand.text)
#     # ratings_list.append(rating.text)
#     details_list.append(detail.text)
#     # price_list.append(pricing.text)
#     # discount_price_lits.append(discount_pricing.text)
#     discount_percentage_list.append(discount_percentage.text)


# print(title_list)
# print()
# print(img_list)
# print()
# # print(ratings_list)
# # print()
# print(details_list)
# print()
# # print(price_list)
# # print()
# # print(discount_price_lits)
# # print()
# print(discount_percentage_list)


# data = {
#     "title": title_list,
#     "img_url": img_list,
#     # "ratings": ratings_list,
#     "details": details_list,
#     # "brand": brand_list,
#     # "price": price_list,
#     # "discount_price": discount_price_lits,
#     "discount_percentage": discount_percentage_list
# }


# model = p.DataFrame(data=data)
# model.to_csv("fashiondata.csv")
