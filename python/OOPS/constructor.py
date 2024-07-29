class student:
    # constructor with parameter give as name
    def __init__(self,name):
        self.name = name
        
    def get_name(self):
        return self.name
    
student1=student('ilihas')
print(student1.get_name())