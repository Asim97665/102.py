import math

def action(name):
    print('Hello ' + name)

action('Asim')

def maths(num):
    squareroot = math.sqrt(num)
    print(squareroot)
    
maths(49)    

def even(num):
    if(num%2==0):
        print('number is even ')
        
    else:
         print('Number is odd')
         
even(79)

def sum():
    num1 = int(input('Enter 1st num'))
    num2 = int(input('Enter 2nd num'))
     
    storage = (num1+num2)
    print('The answer is ' + str(storage))
        
#sum()

def max():
    num1 = int(input('Enter 1st num'))
    num2 = int(input('Enter 2nd num'))
    num3 = int(input('Enter 3rd num'))
    
    if(num1>num2 and num1>num3):
        print('1st number is the greatest ' + str(num1))
        
    elif(num2>num1 and num2>num3):
        print('2nd number is the greatest '+ str(num2))
        
    else:
        print('3rd number is the greatest' + str(num3))
    
max()
    