
# read a year
"""
display century year if last two digit of year is 00
else display non century year
"""

year = int(input("enter year: ")) #2000

if year % 100 == 0:

    print("century year") #ce..

else:

    print("non century year")