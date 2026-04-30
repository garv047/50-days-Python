num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reversed number =", reverse)
'''
num = input("Enter a number: ")
print("Reversed number =", num[::-1])
'''
