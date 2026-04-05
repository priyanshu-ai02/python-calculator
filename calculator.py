#Calculator using python
import math

#Basic operations

def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def mul(a,b):
    return(a*b)

def div(a,b):
    if b == 0:
        return('Error : Division by zero')
    return(a/b)

def power(a,b):
    return(a**b)

#Scientific functions

def square_root(x):
    if x<=0:
        return('Error')
    return(math.sqrt(x))

def sin(x):
    return(math.sin(math.radians(x)))

def cosine(x):
    return(math.cos(math.radians(x)))

def tangent(x):
    return(math.tan(math.radians(x)))

def log(x):
    if x <= 0:
        return('Error')
    return(math.log10(x))

#main program

def calculator():
    while True:
        print("\n === Scientific calculator ===")
        print("1.Add 2.Sub 3.Mul 4.Div ")
        print("5.Power 6.Sqrt 7.Sin 8.Cos 9.Tan 10.Log")
        print("0. Exit")

        choice = input('Enter Your Choice:- ').strip()

        if choice == "0":
            print('Error')
            break
        
        elif choice in ('1' , '2' , '3' , '4' ,'5'):
            a = float(input('Enter your 1st number: '))
            b = float(input('Enter your 2nd number: '))

            if choice == '1':
                print('Result :' , add (a,b))

            elif choice == '2':
                print('Result :' , sub (a,b))
                
            elif choice == '3':
                print('Result :' , mul (a,b))
                
            elif choice == '4':
                print('Result :' , div (a,b))
                
            elif choice == '5':
                print('Result :' , power (a,b))

        elif choice in ('6' , '7' , '8' , '9' , '10'):
            
            x = float(input('Enter the value of x'))

            if choice == '6':
                print('Result:' , square_root(x))

            elif choice == '7':
                print('Result :' , sin(x))

            elif choice == '8':
                print('Result:' , cosine(x))

            elif choice == '9':
                print('Result:' , tangent(x))

            elif choice == '10':
                print('Result:' , log(x))

#Run program
calculator()
