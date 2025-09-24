
# create a dictionary product code,title,category,price,brand

product={
    "code":101,
    "title":"fridge",
    "category":"home-appliance",
    "price":50000,
    "brand":"LG",
    "offer":100
}

# add key stock with value 50 if stock not exist

if "stock" not in product:

    product["stock"]=50

# print(product)

# update offer as current offer+300 if offer exist else add offer as 250
if "offer" in product:

    product["offer"]+=300

else:

    product["offer"]=250

print(product)