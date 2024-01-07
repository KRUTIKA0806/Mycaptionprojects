n=int(input("Enter your number: "))
x1=0
x2=1
print(x1)
print(x2)
c=3
while c<=n:
    y=x1+x2
    print(y)
    x1=x2
    x2=y
    c=c+1