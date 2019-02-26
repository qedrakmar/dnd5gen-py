class character:
    def __init__(self):
        self.returned = self.testing()

    def testing(self):
        self.blah = "undeclared self.blah"
#        self.testing.next = "undeclared self.testing.next"
        return "Returned"

a = character()
print(a.returned)
print(a.blah)
# print(a.testing.next)
print(a.testing)
