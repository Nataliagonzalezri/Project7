# this machine is just a tracker
students = {"padi": 0, "carlos": 0, "andres": 0, "eduardo": 0}

# there are ten questions, so we need to add a for with 10 steps
for i in range(10):
    name = input(F"Who got the answer right for question {i+1}?")
    if name in students:
        students[name] = students[name] + 1
    else:
        # this means that the students was not in the dictionary, so put value 1
        students[name] = 1

print(f"Here is the list of students and answers: {students}")
# find the winner (find the key with the highest value)
# to step process:
# 1. get a list of all the keys
values = list(students.values())
# print(f"values are {values}")
values.sort(reverse=True) # sorts the list descending
# print(f"sorted values {values}")
winner = values[0]  # "0" is the highest number of questions answered.
# print(f"winns is {winner}")
# 2. once I have the winner value, go over each key and see if she's the winner.
for key in students:
    if students[key] == winner:
        print(f"{key} is the winner! Congrats")