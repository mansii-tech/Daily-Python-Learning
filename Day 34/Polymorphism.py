#example of polymorphism(with inheritancce)
class Shape:
    def draw(self):
        pass
class Circle(Shape):
    def draw(self):
        print("draw method of circle class")
class Rectangle(Shape):
    def draw(self):
        print("draw method of rectangle class")
def call_draw(Shape):
    Shape.draw()
obj=input("enter circle or rectangle")
c=""
if obj=="circle":
    c=Circle()
elif obj=="Rectangle":
    c=Rectangle()
call_draw(c)
#example of polymorphism(without inheritance)
class Circle():
    def draw(self):
        print("draw method of circle class")
class Rectangle():
    def draw(self):
        print("draw method of rectangle class")
def call_draw(s):
    s.draw()
obj=input("enter circle or rectangle")
c=""
if obj=="Circle":
    c=Circle()
elif obj=="Rectangle":
    c=Rectangle()
call_draw(c)
#create a base class 
        
    