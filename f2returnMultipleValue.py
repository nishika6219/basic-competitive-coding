#can return multiple values at a time via pointer in python

def multiple():
    n1 = int(input("Enter the value of n1:"))
    n2 = int(input("Enter the value of n2:"))
    sum = n1 + n2
    sub = n1 - n2
    mul = n1 * n2
    div = n1 / n2

    return sum, sub, mul, div

result = multiple()
print(result)   #tuple me return karega
            
