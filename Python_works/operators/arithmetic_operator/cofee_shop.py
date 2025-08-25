
# 5 cofee

bill_total = 185

head_count = 5

tip_amount = 25

gst = (5 / 100) * bill_total

tot_amount = bill_total + tip_amount +gst

# individual split

# per_head = (bill_total + tip_amount) / head_count

per_head = tot_amount / head_count

print("Each one pay", per_head, "Rs")