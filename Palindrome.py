number = 1221
temp = number
operation = 0

while number > 0:
    singleDigit = temp % 10
    operation = (operation * 10) + singleDigit
    temp = temp // 10

if number == operation:
  print('Palindrome')
else:
  print("Not Palindrome")