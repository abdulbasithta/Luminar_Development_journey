

def is_armstrong(num):

    digit_count = len(str(num))

    sum = 0

    original = num

    while(num != 0):

        digit = num %10

        exponent = digit ** digit_count

        sum = sum + exponent

        num = num //10

    return original == sum

print(is_armstrong(153)) #True

print(is_armstrong(123)) #False
