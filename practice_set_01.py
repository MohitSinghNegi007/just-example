# que 1
print("Hello World! Welcome to python learning.")

# que 2 write a poem with single print statement
print('''Twinkle Twinkle little star,
How I wonder what you are.      ''')

# or
print("twinkle twinkle little star,\nhow i wonder what you are")

# que 3
# create variables to store:- your naem(string)
# your age(int), height in mt(flaot), a boolean value representing whether you are a student
# print all in one line.....

name = "Mohit"
age = 22
height = 170.22
is_student = True

print("the name of the student is " + name + ". He is " + str(age) + " years old. He is " + str(height) + " cms tall. " + "Student: " + str(is_student))
# can only concatinate str not int

# que 4
# convert it into an  int and add 10 to it. print the result...
num = "45"
print(int(num) + 10)


# que 5
# write a program that 
# ask the user for their favourite food,    prints{wow! i also like the <food>}

food = input("What is your favoourite food?\n")

print("Wow! I also like " + food)
# in terminal


# que 6
# wat that takes 2 no. as input from the user.,,,,,prints their sum, diff, prid, and quotient

a = int(input("Enetr first no.\n"))
b = int(input("Enter second no.\n"))

print("a + b is", a+b)
print("a * b is", a*b)
print("a / b is", a/b)
print("a - b is", a-b)


# que7
# print the following using escape sequences:
# harry siad, "py is awesome!",, this is a new line,, this is a tab ->      <- here

print('Harry said, "Python is awesome!"\nTHis is on a new line.\nTHis is a tab ->\t>- here')

# wap that takes integer as input fron the user,,, prints the sq.  and cube of that no.
a = int(input("Enter your no \n"))

print("square is" , a**2)
print("cube is", a**3)
