def square_digits(num):
    number = ""
    for digit in str(num):
        number += str(int(digit) * int(digit))
    return int(number)
