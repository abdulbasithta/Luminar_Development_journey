"""
expenses=[12000,13000,14000,15000,16000] # List

expenses={"jan":12000,"feb":13000,"mar":14000} # Dictionary

"""


charger={
        "brand":"Lenovo",
         "color":"black",
         "watt":65.0,
         "type":"pin",
         "model":"ADP-65ME",
         "price":1000
         }

# charger_watt=charger["watt"]
# charger_model=charger["model"]

# print(charger_watt)
# print(charger_model)

if "made-in" in charger:

    print("exist")

else:

    print("not exist")

# add | update new key:value

charger["made-in"]="India" #add

charger["price"]=850 #update

print(charger)
