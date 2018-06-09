# OOPS Learnings
"""
1. simple class
"""


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


if __name__ == '__main__':
    # Creating an object for the class
    # Account is a varible
    # Printing the class
    print(Account_Details)

    # Converting the class to object
    account = Account_Details()
    print(account)
    #
    print(account.personal_account())




