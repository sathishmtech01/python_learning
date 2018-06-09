# OOPS Learnings
"""
1. simple class
"""

class Account_Details:
    
    # self is constructor
    def personal_account():

        return {"id":"Pid_1",
                "name":"csk",
                "amount":100}

    def corporate_account():
        return {"id":"Cid_1",
                "name":"csk",
                "amount":100}

    def account(id,name,amount):
        return (id,name,amount)


if __name__ == '__main__':


    # Simple class function calling, where Account_Details is class and personal_account is function
    print(Account_Details.personal_account())

    # Simple class fuction with passing arguments
    id = "Pid_1"
    name = "csk"
    amount = 100

    print(Account_Details.account(id, name, 200))




