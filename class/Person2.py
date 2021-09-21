class Person():
    def __init__(self,name):
        self.name=name
    def __del__(self):
        print("забанен... " ,self)
p=Person()
p.__del__()
print()