
import pickle
import shelve
import os


class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)


# Serialization using pickle
def save_with_pickle(obj, filename):
    with open(filename, "wb") as file:
        pickle.dump(obj, file)
    print("Object saved using pickle.")


def load_with_pickle(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)


# Persistence using shelve
def save_with_shelve(obj, filename, key):
    with shelve.open(filename) as db:
        db[key] = obj
    print("Object saved using shelve.")


def load_with_shelve(filename, key):
    with shelve.open(filename) as db:
        return db.get(key)


# Main program
student = Student("DEVESH", 101, 90)

# Save and restore using pickle
save_with_pickle(student, "student.dat")
restored_student = load_with_pickle("student.dat")

print("\nRestored using pickle:")
restored_student.display()

# Save and restore using shelve
save_with_shelve(student, "student_db", "student1")
restored_student2 = load_with_shelve("student_db", "student1")

print("\nRestored using shelve:")
if restored_student2:
    restored_student2.display()
