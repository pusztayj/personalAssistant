"""
File: personalAssistantClass.py
Description: Designs a class that models an assistant
"""

from smartImport import smartImport
from personalAssistantClass import PersonalAssistant


def createAssistant():
    """Constructs a PersonalAssistant object and returns it."""
    print("Please name your assistant")
    name = input(">> ")
    print("Please provide your name")
    user = input(">> ")
    print("Now creating your assistant...")
    return PersonalAssistant(name, user)

def main():
    manageImports()
    assistant = createAssistant()
    assistant.run()
    
if __name__ == "__main__":
    main()



def manageImports():
    import importlib
    imports = ["assistanceFunctions"]
    for module in imports:
        globals().update(importlib.import_module(smartImport(module)).__dict__)


class PersonalAssistant(object):
    """A class that models an assistant."""
    
    def __init__(self, name, user):
        """Constructor for a PersonalAssistant."""
        self._name = name
        self._user = user

    def run(self):
        """Runs a PersonalAssistant."""
        while True:
            print("\n" + self._name + " - How may I help you?\n")
            user_input = input(">> ").upper()
            if user_input != "":
                self.display(checkInput(user_input))
            else:
                self.display("Until Next Time...")
                break

    #A temporary method until a GUI class is developed
    def display(self, value):
        if value != None:
            print(value)

    def changeUser(self, newUser):
        """Changes the name of the user."""
        self._user = newName

    def changeName(self, newName):
        """Changes the name of the PersonalAssistant."""
        self._name = newName

    def getName(self):
        """Returns the name of the PersonalAssistant."""
        return self._name

    def getUser(self):
        """Returns the name of the user."""
        return self._user

    def exit(self):
        """Ends the PersonalAssistant program."""
        pass
