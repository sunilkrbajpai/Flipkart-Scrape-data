from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

item=input("Enter the product you want to search on FLIPKART:---\t\t")   #get item name
item = item.replace(" ", "")

my_url = "https://www.flipkart.com/search?q="+item
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"_1-2Iqu row"})
#print(len(containers))                #print total number of class

#print(soup.prettify(containers[0]))    #parse html in class

container = containers[0]
name=container.findAll("div", {"class":"_3wU53n"})     #print name of product
#print(name[0].text)
price = container.findAll("div", {"class":"_1vC4OE _2rQ-NK"})
#print(price[0].text)

ratings = container.findAll("div", {"class":"hGSR34"})
#print(ratings[0].text)

filename = "products.csv"
f = open(filename, "w", encoding="utf-8")                 #open file in write mode

headers = "Products_name, pricing, rating\n"
f.write(headers)

for container in containers:
    name = container.findAll("div", {"class": "_3wU53n"})  # print name of product
    product_name=name[0].text
    #print(product_name)
    price = container.findAll("div", {"class": "_1vC4OE _2rQ-NK"})
    product_price=price[0].text
    product_price=product_price.replace(",", "")
    product_price=product_price.replace("₹", "Rs. ")

    #print(product_price)
    ratings = container.findAll("div", {"class": "hGSR34"})
    product_rating=ratings[0].text
    #print(product_rating)

    print(product_name.replace(",","|")+", "+product_price+", "+product_rating+"\n")
    f.write(product_name.replace(",", "|") + ", " + product_price+ ", " +product_rating + "\n")

f.close()
