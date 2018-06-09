# OOPS Learnings
"""
1. Methods Overriding

"""

# Parent Class
class Account_Details:

    # default variable, accessable in all the function of this class
    # constructor
    # init - global intialization for this class
    def __init__(self):
        self.name = "csk"
        self.age =27

    # self is keyword to access
    def personal_account(self):
        return {self.age,self.name}

    def corporate_account(self):
        print(self.name)
        return [self.age,self.name]

    def account(self,id, name, amount):
        print(self.age)
        return (id, name, amount)
    def test(self):
        return "Parent class method"


# Child class
class Occupation_Details(Account_Details):
    def test(self):
        return "child class method"




if __name__ == '__main__':
    # child class object
    account = Occupation_Details()
    print(account.test())

