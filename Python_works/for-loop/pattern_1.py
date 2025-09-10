#pgm2

# 1 1 1 1
# 2 2 2 2
# 3 3 3 3

for row in range(1,4):

    for col in range(1,5):

        print(row,end=" ")
    
    print()


# < > < >
# < > < >
# < > < >

for row in range(1,4):

    for col in range(1,5):

        if col % 2 ==0:

            print(">",end=" ")
        
        else:

            print("<",end=" ")
    
    print()