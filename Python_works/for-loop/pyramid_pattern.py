
# 5 col and 5 row

#      *            (4 space)
#     *  *          (3)
#    *  *  *        (2)
#   *  *  *  *      (1)
#  *  *  *  *  *    (0)

for row in range(1,6):

    for sp in range(1,6-row):

        print(" ",end="")

    for col in range(1,row+1):
        
        print("* ",end="")

    print("")