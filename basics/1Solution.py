class A:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    
obj = A(20,30)
print(obj.add())