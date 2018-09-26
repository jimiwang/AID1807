






class Mylist:
    def __init__(self,iterable=()):
        self.data = list(iterable)

    def __repr__(self):
        return "Mylist(%s) " % self.data

    def __add__(self,other):
        # L = self.data + other.data
        return Mylist(self.data + other.data)

    def __mul__(self,rhs):
        L=self.data * rhs 
        return Mylist(L)

L1=Mylist([1,2,3])
L2=Mylist([4,5,6])
L3= L1 + L2
print(L3)   #Mylist([1,2,3,4,5,6])
L4= L2 + L1
print(L4)   #Mylist([4,5,6,1,2,3])
L5=L1*3
print(L5)   #Mylist([1,2,3,1,2,3,1,2,3])





