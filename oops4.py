class Human:
    def __init__(self):
        print("human == init")
    def eat(self):
        print("veggies")
    def shelter(self):
        print("house")

class Animal(Human):
    def __init__(self):
        super().__init__()
        print("animal == init")
    def shelter(self):
        print("domes - house : wild - forest")
    def eat(self,meat= None):
        if meat == None:
            print("veggies")
        else:
            print(meat+"eats this")
class Bird(Animal,Human):
    def __init__(self):
        super().__init__()
        print("bird == init")

a1 =Bird()
# a1 =Animal()
# a1.eat("lion")
