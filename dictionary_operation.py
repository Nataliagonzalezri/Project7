# empty dictionary
d = {}
print(f"my dictionary is: {d}")

# The key is de number and the value is the first name.
students = {1: "John", 2: "Valentina", 3: "Beatriz"}
student_list = ["John", "Valentina", "Beatriz"]

# add a new student to a dictionary. Order is not important be cause there are keys.
students[7] = "Carlos"
print(f"my students are: {students}")
print(f"Carlos is: {students[7]}")
students["nine"] = "Ignacio"
print(f"my students are: {students}")
# delete valentina
del students[2]
print(f"my students are: {students}")

# we can iterate over a dictionary (each element, one at the time)
for key in students:
    print(f"{key} correspondes to {students[key]}")
    