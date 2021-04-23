import pickle ,datetime
import hashlib 
    

class User():
    def __init__(self,username,password) -> None:
        self.username = username
        self.date = datetime.datetime.today()
        self.passwrod = self.hash_with_sha256(password)
        self.is_admin = False
        
    def login(self,password):
        if self.passwrod == self.hash_with_sha256(password):
            return True
        return False
    
    def hash_with_sha256(self,input):
        return hashlib.sha256(input.encode()).hexdigest()
    
    
class Food():
    def __init__(self,name) -> None:
        self.name = name
        self.amount = 0
        
class Cart():
    def __init__(self,name) -> None:
        self.name = name
        self.food =None
        self.user =None
        

'''
    We Have a DB file that has three list ->{
        'user':[
            
        ],
        'food':[
            
        ],
        'cart':[
            
        ],
    }
'''
def storeData(): 
    db = {
        'uesr':[],
        'food':[],
        'cart':[]
    } 
    db['user'].append(User('Mehrdad','kmn123789'))
    db['food'].append(Food('GormeSabZ',10))
    db['cart'].append(Cart('GormeSabZ','Mehrdad'))
    
    dbfile = open('sampledb', 'ab')
    pickle.dump(db, dbfile)                      
    dbfile.close() 
  
  
  
  
def loadData(): 

    dbfile = open('sampledb', 'rb')      
    db = pickle.load(dbfile) 
    for keys in db: 
        print(keys, '=>', db[keys]) 
        
    dbfile.close() 
  
if __name__ == '__main__': 
    storeData() 
    loadData()
