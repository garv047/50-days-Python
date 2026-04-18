n = int(input("Enter number "))
g = 0
for i in range(2,n):
    if n%i==0:
        g = 1
        break
if g==1:
    print("Not Prime")
else:
    print("Prime")
