# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

#def factorial(n):
    #if n == 0:
       # return 1
    #else:
       # return n * factorial(n-1)

#def factorial(n):
    #while n == 0:
        #return 1
    #else:
        #return n * factorial(n-1)

def factorial(n):
    result = 1
    while n >= 1 :
        result = result * n
        n = n - 1
    return result


print (factorial(4))
#>>> 24
print (factorial(5))
#>>> 120
print (factorial(6))
#>>> 720
