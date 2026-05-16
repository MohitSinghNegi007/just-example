a = int(input("enter a number between 1 and 100: "))
match a:
    case 1:
        print("congratulations")
    case 4:
        print("second prize")
    case 7:
        print("third chhor")
    case _:
        print("beter luck next time")
#         # to make py more convinient we use match case..






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
       