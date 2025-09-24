
orders=["tea","cofee","tea","coldcofee","tea","cofee","lemon tea","tea","coldcofee"]

order_count= {}

for o in orders:

    if o in order_count:

        order_count[o] +=1

    else:

        # order_count.update({o:1})
        order_count[o] =1

print(order_count)