class oops2:
    oops ="inheritance"

    def __init__(self,name):
        self.name=name
    def instancemethod(self):
      # self.name=name
        print(f"name :{self.name}")
    @classmethod
    def classmethod(cls):
        print(cls.oops)
    @staticmethod
    def ststicmethod():
        print("nothing to do with class variables and instance variables")
n1 = oops2("shamy")
n1.instancemethod()
oops2.classmethod()
oops2.ststicmethod()