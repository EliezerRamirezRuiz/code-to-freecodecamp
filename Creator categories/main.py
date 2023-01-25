 
class Category():
  def __init__(self):
    self.ledger = []


  def __repr__(self):
    return repr(self.ledger)
    
  def deposit(self, d:str , a:int):
    if d == "":
      self.ledger.append({"description":"", "amount":a})
    else:
      self.ledger.append({"description":d, "amount":a})

  
  def withdraw(self,d:str,a:int):
    if self.Check_found(a) == True:
      self.ledger.append({"description":d, "amount":-a})  
      return True
    else:
      return False

    
  def get_balance(self):
    container = []
    """------------"""
    for i in self.ledger:
      container.append(i.get('amount'))
      
    container = sum(container)
    
    return container

    
  def Transfer(self , obj , m:int):
    if isinstance(obj, Category) == True and self.withdraw(f"Transfer to other category", m) == True:
      obj.deposit(f"Transfered from other category", m)
      return True
        
    else:
      return False
    
    
  def Check_found(self, m:int):
    if m < self.get_balance():
      return True
    else:
      return False
      

a = Category()
b = Category()

a.deposit("Initial deposit", 10000)
b.deposit("Initial deposit", 10000)
b.withdraw("get my money", 15000)

a.Transfer(b,1000)

d = a.get_balance()
e = b.get_balance()

print(d,e)
print(a.ledger)
print(b.ledger)
