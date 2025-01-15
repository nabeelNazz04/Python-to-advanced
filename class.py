class Human:
  def __init__(self,n,o):
    self.name=n
    self.occupation=o
  def getname(self):
    if self.occupation=='actor':
      print(self.name,"is an actor")
    elif self.occupation=='tennis player':
      print(self.name,"is a tennis player")
  def speak(self):
    print(self.name,'says Hello')
tom=Human('tom cruise','actor')
an=Human('an','tennis player')
tom.getname()
an.getname()
tom.speak()