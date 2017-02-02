# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

# def biggest (a, b, c):
#     if a > b :
#         if a > c :
#             return a
#         else: # c >= a > b
#             return c
#     else: # b >= a
#         if b > c:
#             return b
#         else : #c >= b >= a
#             return c
## option2
def bigger(a, b):
    if a > b:
        return a
    else:
        return b

def biggest(a, b, c):
    return bigger(bigger(a, b), c)

print (biggest(3, 6, 9))
#>>> 9

print (biggest(6, 9, 3))
#>>> 9

print (biggest(9, 3, 6))
#>>> 9

print (biggest(3, 3, 9))
#>>> 9

print (biggest(9, 3, 9))
#>>> 9
