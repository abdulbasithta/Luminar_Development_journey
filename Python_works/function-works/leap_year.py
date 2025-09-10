
def leap_year(year):

    if year %100 ==0 and year %400 ==0 or year %100 !=0 and year %4 ==0:

        return True
    
    return False

print(leap_year(2024))

print(leap_year(2026))

print(leap_year(2000))