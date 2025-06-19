def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1) 
print(factorial(5))    
print(factorial(0))
print(factorial(1))
    
#fibonacci sequence   
a=int(input('Enter Your Numbeer:'))
def fibonacci(n):    
    if(n==1 or n==0):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range(a):    
    print(fibonacci(i))
    
    
    
    