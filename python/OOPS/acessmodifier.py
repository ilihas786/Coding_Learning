# These control the visiblity of data members

# public  (by default all parameters are public)

class PUBLIC:
    def __init__(self):
        self.public_attribute=None
        
    def public_function():
        pass
    
# private

class PRIVATE:
    def __init__(self):
        self.__private_attribute=None # To make atribute/function as private we have to add '__'  ( 2 underscore ) before name of vairable
        
    def __private_function():# This is private function
        pass
    
obj=PRIVATE()
# print(obj.__private_attribute) # ERROR acesssing private member directly

# protected 
class PROTECTED:
    def __init__(self):
        self._protected_attribute=None # To make atribute/function as protected we have to add '_' ( 1  underscore ) before name of vairable
        
    def _protected_function():# This is protected function
        pass
    
obj=PRIVATE()
# print(obj.__private_attribute) # ERROR acesssing private member directly