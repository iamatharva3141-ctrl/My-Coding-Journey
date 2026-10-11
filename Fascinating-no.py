n=int(input("enter a number"))
k1=2*n
k2=3*n
c=0
s=str(n)+str(k1)+str(k2)

for i in  s:
 if i in "123456789":
   c=c+1
if c==len("123456789"):
  print(f"{s}  is Fascinating number")