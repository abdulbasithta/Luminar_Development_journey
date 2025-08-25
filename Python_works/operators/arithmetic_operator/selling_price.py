# calculate selling price

# cost price

purchase_price = int(input("Enter the purchase price: "))

# profit margin in percenage

profit_margin = int(input("Enter the % of profit margin "))

profit = (profit_margin / 100) * purchase_price


selling_price = purchase_price + profit

print("Selling Price: Rs ", selling_price)