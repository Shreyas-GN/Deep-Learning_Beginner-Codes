class model(object):
  def __init__(self,numlayers,numunits,name):
    self.layers = numlayers
    self.units = numunits
    self.name = name
    self.weights = 1
  
  def howManyUnits(self):
    totalUnits = self.layers*self.units
    print(f'This model has {totalUnits} units in the model.')

  def trainTheModel(self,x):
    self.weights += x
    return self.weights
  
  def __str__(self):
    return f'This is a {self.name} model.'

m1=model(34,2,'Shreyas')
m1.howManyUnits()
m1.trainTheModel(3)
