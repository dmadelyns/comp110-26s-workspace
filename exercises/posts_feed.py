from class_writing import profile 

"""Instantiate the Profile class."""

user1: profile = profile("110_rulez")
print(user1.private)

user1.private = False 
print(user1.private)

user1.tweet("OOP is cool!")

