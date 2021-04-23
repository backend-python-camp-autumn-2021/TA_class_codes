class A:
    def __init__(self,name) -> None:
        self.name = name
        
    def say_who_i_am(self):
        print(self.name)
        return None
    
    
class BacheYeA(A):
    '''
    Sample of override
    '''
    
    def say_who_i_am(self):
        # return super().say_who_i_am()
        # print('Nemikham Esmamo Begam!')
        return self.name
    
print("helo")

def hello_world():
    return 

variable = hello_world