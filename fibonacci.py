#pa devolver el array del enésimo fibonacci
def fibonacci(n):
    if n==0:
        fibonacci=[0]
        return fibonacci 
    elif n==1:
        fibonacci=[0,1]
        return fibonacci
    else: 
        fibonacci=[0,1]
        a,b=0,1
        for _ in range(n-1):
            a,b=b,a+b
            fibonacci.append(b)
        return fibonacci
    
print(fibonacci(10))


#pa devolverlo dado un número n así: 
'''
Fibonacci Series
Write a program that generates the Fibonacci series up to a given number 'n'.

fibonacci(0) -> []

fibonacci(10) -> [0, 1, 1, 2, 3, 5, 8]

fibonacci(23) -> [0, 1, 1, 2, 3, 5, 8, 13, 21]

#pa devolver el enésimo fibonacci

'''

'''
def fibonacci_given(n):
    if n==0:
        fibonacci=[]
        return fibonacci 
    elif n==1:
        fibonacci=[0,1]
        return fibonacci
    else: 
        fibonacci=[0,1]
        a,b=0,1
        while n>b+a:
            a,b=b,a+b
            fibonacci.append(b)
        return fibonacci
'''

#pa devolver sólo el numerito
def find_fibonacci(n):
    if n==0:
        return 0 
    elif n==1:
        return 1
    else: 
        a,b=0,1
        for _ in range(n-1):
            a,b=b,a+b
        return b
