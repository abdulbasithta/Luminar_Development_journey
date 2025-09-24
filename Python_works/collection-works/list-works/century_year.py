
years=[1899,1900,2000,2021,2022,2023,1991,1992]

# century_year_list
# non_century_year_list

century_year =list() # []

non_century_year=list()

for yr in years:

    if yr % 100 ==0:

        century_year.append(yr)

    else:

        non_century_year.append(yr)

print("Century year", century_year)

print("Non-Century year", non_century_year)
