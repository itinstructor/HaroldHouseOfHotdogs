"""
    File: pickle_object.py
    Description: Example of pickling and unpickling a custom object
"""
import pickle


# Create a custom class that you want to pickle and unpickle
class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        """Return a string representation of the object."""
        return f"Student(name='{self.name}', age={self.age})"


# Create an instance of the custom class and pickle it:
student1 = Student("Alice", 20)
print(f"{student1}")

# Pickle the object and save it to a file
print("Pickle the object")
with open("student.pickle", "wb") as file:
    pickle.dump(student1, file)

# Unpickle the object from the file
with open("student.pickle", "rb") as file:
    student1 = pickle.load(file)

print("Unpickle the object")
# Student1 holds the unpickled object
print(student1)
