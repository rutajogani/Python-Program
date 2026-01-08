# number of  factorial series

number = int(input("Enter Number: ")) 
num1 = 0
num2 = 1

for i in range(1 , number + 1):
        text = num1 + num2
        num1 = num2
        num2 = text
        print(text, end = " ")
