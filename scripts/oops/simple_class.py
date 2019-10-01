# OOPS Learnings
"""
1. simple class
"""

class Classroom:
    # Constructor
    # when the class is executing the first function which executes
    def __init__(self):
        self.width = 100
        self.height = 200
        print("Default Exection : ",self.width,self.height)

    def room(self):
        self.cost = self.width*self.height
        print(self.cost)
        return self.cost

if __name__ == '__main__':
    # object - instance of the clas
    classroom = Classroom()

    # input()
    # btech_room_cost = classroom.room()
    # print(btech_room_cost)





