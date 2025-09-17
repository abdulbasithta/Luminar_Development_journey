# bms,dst,ptm,wkn
orders=["bms","bms","bms","ptm","ptm","ptm","wkn","wkn","wkn","bms","bms","ptm"]

bms_ticket_sold =0

ptm_ticket_sold =0

wkn_ticket_sold =0

# highest ordered movie platform

for ord in orders:

    if ord =="bms":

        bms_ticket_sold +=1
    
    elif ord =="ptm":

        ptm_ticket_sold +=1

    elif ord =="wkn":

        wkn_ticket_sold +=1


if bms_ticket_sold > ptm_ticket_sold and bms_ticket_sold > wkn_ticket_sold:

    print("bms is highest")

elif ptm_ticket_sold > bms_ticket_sold and ptm_ticket_sold > wkn_ticket_sold:

    print("ptm is highest")

elif wkn_ticket_sold > bms_ticket_sold and wkn_ticket_sold > ptm_ticket_sold:

    print("wkn is highest")

# lowest

if bms_ticket_sold < ptm_ticket_sold and bms_ticket_sold < wkn_ticket_sold:

    print("bms is lowest")

elif ptm_ticket_sold < bms_ticket_sold and ptm_ticket_sold < wkn_ticket_sold:

    print("ptm is lowest")

elif wkn_ticket_sold < bms_ticket_sold and wkn_ticket_sold < ptm_ticket_sold:

    print("wkn is lowest")

# total_ticket_sold

total_ticket_sold = len(orders)

print("total ticket sold", total_ticket_sold)