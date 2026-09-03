s1=[]
s2=[]
c=0
e0=0
e1=0
e2=0
iv={}
sum=0
product={"rice":{"price":56,"stock":0},
         "aata":{"price":50,"stock":0},
         "soap":{"price":20,"stock":4},
         "shampoo":{"price":90,"stock":2}}
print("All available products are")
for i in product:
    print("-",i,"-")
for i in product:
    print("(",i,")")
    
    c=0
    e0=0
    e1=0
    e2=0
    for k,v in product[i].items():
        print(k,"=",v)
        
        c=c+1 
        if c==1:
           e1=v
        if c==2:
            e2=v
            if v<=5 and v>0:
              s2.append(i)  
            if v==0:
              s1.append(i)
              print(f"total inventory value of {i} is = 0")
              iv[i]=[0]
        e0=e0+e1*e2
        if e0>0:
         print(f"total inventory value of {i} is = ",e0)
         sum=sum+e0
         iv[i]=e0
            
print("|Total inventory values are| =              ",iv)        
print("|items with low (less than 5) stock left| = ",s2)
print("|items with no stock left| =                ",s1)
print("|Total inventory sum| =                     ",sum)