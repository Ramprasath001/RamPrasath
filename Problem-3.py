def series(a):
    b=[]
    for i in range(1,a*2,2):
        b.append(i)
        if len(b)==a:
            break
    if a%2==0:
        b.pop() 
    return b
a = int(input("Enter a value: "))
print("Output:",series(a))
