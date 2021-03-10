a = "Helllo world"
b = {"Bogdan": 7, "Mary": 5, "Elon": 10}

def function_in_module():
    print("this is a function that is in a module")

# in orden not to run this code when imported, we need to guard it
if __name__ == "__main__":
    name = input("What is your name?")
    print(f"Hello {name}")