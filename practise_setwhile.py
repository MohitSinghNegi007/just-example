# sum = 0
# i = 1

# while i<+101:
#     sum += i
#     i +=1

# print(sum)   


# wap to enter s password untill the correct password is entered:

password = "1234"
entered_password = input("enter password")

while(entered_password != password):
    entered_password = input("wrong! 3 attempt ramaining")

print("u r logged in")    