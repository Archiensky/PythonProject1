class Student:
    amount = 0
    def __init__(self, height=160, money=0):
        self.height = height
        self.money = money
        Student.amount += 1

nick = Student(money=200)
andrew = Student()
print(nick.money)
print(andrew.money)
# class Student:
#     print("hi")
#     def __init__(self):
#         self.height = 160
#         print(self)
#     def sleep(self):
#         print("sleep")
#
# first_student = Student()
# r_student = Student()
# first_student.sleep()

# class Student:
#     amount_of_students = 0
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_of_students+=1
#     def grow(self, height=1):
#         self.height+=height
#
# nick = Student()
# kate = Student(height=170)
# print(kate.height)
# print(nick.height)
# print("summer")
# nick.grow(height=15)
# print(kate.height)
# print(nick.height)

# class Student:
#     def __init__(self, name=None):
#         self.name = name
#     def __str__(self):
#         return f"I am a student. My name is {self.name}."
#
# nick = Student(name="Nick")
# ann = Student()
# print(nick)
# print(ann)

# import random
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.gladness = 50
#         self.progress = 0
#         self.alive = True
#
#     def to_study(self):
#         print("Time to study")
#         self.progress += 0.1
#         self.gladness -= 7
#
#
#     def to_sleep(self):
#         print("I will sleep")
#         self.gladness += 3
#
#     def to_chill(self):
#         print("Rest time")
#         self.gladness += 5
#         self.progress -= 0.1
#
#     def is_alive(self):
#         if self.progress < -0.5:
#             print("Cast out…")
#             self.alive = False
#         elif self.gladness <= 0:
#             print("Depression…")
#             self.alive = False
#         elif self.progress > 5:
#             print("Passed externally…")
#             self.alive = False
#
#     def end_of_day(self):
#         print(f"Gladness = {self.gladness}")
#         print(f"Progress = {round(self.progress, 2)}")
#
#     def live(self, day):
#         day = "Day " + str(day) + " of " + self.name + " life"
#         print(f"{day:*^50}")
#         live_cube = random.randint(1, 3)
#         if live_cube == 1:
#             self.to_study()
#         elif live_cube == 2:
#             self.to_sleep()
#         elif live_cube == 3:
#             self.to_chill()
#         self.end_of_day()
#         self.is_alive()
#
# nick = Student(name="Nick")
# kate = Student(name="Kate")
# bohdan = Student(name="Bohdan")
# for day in range(3650):
#     if nick.alive == False:
#         break
#     nick.live(day)
#     if kate.alive == False:
#         break
#     kate.live(day)
#     if bohdan.alive == False:
#         break
#     bohdan.live(day)