#Simple Python Calculator
class Calculator :
    def sum(self , a, b):
        return(a+b)
    def sub(self , a, b):
        return(a-b)
    def mul(self , a , b):
        return(a*b)
    def div(self , a , b ):
        if b == 0:
            return('Cannot divide by zero')
        return(a/b)
    
a = int(input('Enter the 1st number : '))
b = int(input('Enter the 2nd number : '))
op = (input('Enter the operation you want to do (+,-,*,/): '))

obj = Calculator()

if op == '+':
    print(f'The sum of {a} + {b} is {obj.sum(a,b)} ')

elif op == '-':
    print(f'The subtraction of {a} - {b} is {obj.sub(a,b)} ')

elif op == '*':
    print(f'The multiplication of {a} * {b} is {obj.mul(a,b)} ')

elif op == '/':
    print(f'The division of {a} / {b} is {obj.div(a,b)} ')
