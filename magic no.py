

for n in range(1,100):
 while n!=1:
  k2=0
  while n!=0:
     k1=n%10
     n=n//10
     k2=k2+k1
     
  n=k2
if n==1:    
 print("Magic no.= ",n)