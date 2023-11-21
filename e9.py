#Python program that creates a custom class with an 'init' method. Use 'ellipsis' to indicate that some attributes may be added dynamically.
class MyClass:
    def __init__(self, attribute1, attribute2, attribute3, attribute4=...):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        self.attribute4 = attribute4

    def set_attribute4(self, value):
        self.attribute4 = value

obj = MyClass("Red", "Green", "White")
print("Attribute 1:", obj.attribute1)
print("Attribute 2:", obj.attribute2)
print("Attribute 3:", obj.attribute3)
print("Attribute 4:", obj.attribute4)  
obj.set_attribute4("Orange")
print("Modified Attribute 4:", obj.attribute4)
