# Armstrong Number

number = int(input('Enter Number: '))
sum = 0
ans = number

while number > 0:
    singleDigit = number % 10
    sum += singleDigit * singleDigit * singleDigit
    number = number / 10

if ans == sum:
    print("This Number Is Armstrong")
else:
    print("This Number Is Normal")

