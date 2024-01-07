class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.coords = (self.x,self.y)
    
    def move(self,x,y):
        self.x += x
        self.y += y
    
    def __add__(self , p):
        return Point(self.x+p.x, self.y + p.y)
    def __str__(self):
        return "(" + str(self.x) + ',' + str(self.y) + ')'


p1 = Point(1,3)
p2 = Point(5,6)
p3 = p1 + p2
print(p1 + p2)