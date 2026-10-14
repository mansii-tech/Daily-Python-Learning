#-----Multiple Inheritance-----
#1 child and 2 parent class

class Phone: #parent class1
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def make_call(self,number):
        return f"{self.brand} {self.model} is calling number"

    def send_message(self,number,message):
        return f"{self.brand} {self.model} sent message to {number} : {message}"
    
class Camera: #parent class2
    def __init__(self,resolution):
        self.resolution = resolution
    def take_photo(self):
        return f"Taking photo with {self.resolution}MP camera"
    
    def record_video(self):
        return f"Recording video with {self.resolution}MP camera"
    
#creating smartphone
class Smartphone(Phone,Camera):
    def __init__(self,brand,model,resolution):
        Phone.__init__(self,brand,model)
        Camera.__init__(self,resolution)
        
#creating object of smartphone
s=Smartphone("iphone","promax","100")
print(s.make_call(12345))
print(s.send_message(123,'hello from mansi'))
print(s.take_photo())
print(s.record_video())