arr=[10,11,12,13,15,16,17]

# {10:even,11:odd,12:even,...}

odd_even={num:"even"if num%2 ==0 else "odd" for num in arr}

print(odd_even)