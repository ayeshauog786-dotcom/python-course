class Robot:

    def __init__(self):
        self.name = ""

    def introduce(self):
        print("Hello! My name is", self.name)
        print("I am a robot.")


tom = Robot()
jerry = Robot()

tom.name = "Tom"
jerry.name = "Jerry"

tom.introduce()
print("-------------------")
jerry.introduce()