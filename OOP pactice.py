#Demostration of OOP concepts(Inheritance,Polymorphism,Abstract Base class) in python

from abc import ABC, abstractmethod
import math

class Input:
    def __init__(self, *args):
        self.args=args
      
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod 
    def display(self):
        pass

class square(Shape,Input):
    def __init__(self,s):
        Input.__init__(self,s)
        self.s = s
    def area(self):
        return self.s**2
    
    def perimeter(self):
        return 4 * self.s

    def display(self):
        print(f"Square with side {self.s}, area {self.area()}, and perimeter {self.perimeter()}")

class rectangle(Shape,Input):
    def __init__(self,l,b):
        Input.__init__(self,l,b)
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b
    
    def perimeter(self):
        return 2 * (self.l + self.b)

    def display(self):
        print(f"Rectangle with length {self.l} and breadth {self.b}, area {self.area()}, and perimeter {self.perimeter()}")

class triangle(Shape,Input):
    def __init__(self,a,b,c):
        Input.__init__(self,a,b,c)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def display(self):
        print(f"Triangle with sides {self.a}, {self.b}, and {self.c}, area {self.area()}, and perimeter {self.perimeter()}")

if __name__=="__main__":
 
 s1=[]
 s2=[]
    

 n=(input("enter--\n 1 parameters  for square \n 2 parameters seperated by commas for rectangle \n 3 parameters seperated by commas for triangle:\n your answer =  "))
 s1=(n.split(","))
 for i in range(len(s1)):
     s2.append(int(s1[i]))


 if len(s1)==1:
    ob1=square(*s1)
    ob1.display()
 elif len(s1)==2:
    ob2=rectangle(*s2)
    ob2.display()
 elif len(s1)==3:
    ob3=triangle(*s2)
    ob3.display()
    