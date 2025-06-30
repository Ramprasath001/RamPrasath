a=int(input("enter the number:"))
b=[]
for i in range(a*2):
  if i%2!=0:
    b.append(i)
print("count: ",b)