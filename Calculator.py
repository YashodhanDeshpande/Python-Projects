print("WELCOME TO A SIMPLE CALCULATOR")
a=float(input("Please enter the first number "))
b=float(input("Please enter the second number "))
OPP=input("Please enter the operation you want to perform \n Press + for addition \n Press - for subtraction \n Press * for multiplication \n Press / for division")
if OPP=="+":
    print("The Answer is", a+b)
elif OPP=="-":
    print("The Answer is", a-b)
elif OPP== "*":
    print("The Answer is", a*b)
else:
    print("The Answer is", a/b)