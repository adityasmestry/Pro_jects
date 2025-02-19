#Finonacci series
c = int(input("Enter limit: "))  
a=0
b=1 
print("Fibonacci series up to given number:")
while a <= c:
    print(a)
    temp=a+b
    a=b
    b=temp
