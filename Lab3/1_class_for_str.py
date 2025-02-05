class StringHandler:
    def __init__(self):
        self.string = ""
        

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        self.stringUpperCase = self.string.upper()
        print(stringUpperCase)
        


obj = StringHandler()
obj.getString()
obj.printString()
print(obj.stringUpperCase)
