# que 1

#1. wap that ask a user for a num and prints whether it is pos. neg. or Zero
#2. create a program that checks if a person is eligible to vote....
#3. wap that takes a no from the user and prints even if it is even otherwise odd

num = int(input("enter your num: "))
print(num)
if(num == 0):
    print("num is zero")
elif(num < 0):
    print("num is neg")
else:
    print("num is pos")



age = int(input("enter age"))
if(age>18):
    print("yes u can cast vote")
else:
    print("soryy bro")



num = int(input("enter num "))
print(num)

if(num % 2== 0):
    print("even")
else:
    print("odd")



     # que... ask th euser to enter a day num(1-7) and pribnt the corrosponding day of th eweek using match case
        # wap that simulstes simple calculator,,... ask th euser for 2 num. and an op(+ - * /)...perform the op using match case...


a = int(input("enter num between 1 and 7 : "))
match a:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")            
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")    



a = int(input("enter num 1 : "))
b = int(input("enter num 2 : "))

operation = input("choose operation: ")

match operation:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)   



        # print no from 1 to 10 using a for loop
        # print mult. of table of num. netered by User
        # calculate sum of all no from 1 - 100 using a for loop
        # print the following pattern using a for loop


for i in range(1, 11):
    print(i)


n = int(input("enter num"))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)


sum = 0
for i in range(1, 101):
    print(i)
    sum += i

print(sum)   



for i in range(1, 10):
    print(" * " *i)


    
