
n=int(input("Enter a number: "))
while n!=1:
  k2=0
  while n!=0:
     k1=n%10
     n=n//10
     k2=k2+k1**2
     
  n=k2
if n==1:    
 print("Happy no.= ",n)