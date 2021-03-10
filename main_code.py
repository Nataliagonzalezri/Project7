# we want to use the module
# the most common is:
# import module
# other way is this:

#import module as external_module
from module import b as b1
from module2 import b, a

# b from module
print(f"b = {b1}")
# b from module2
print(f"b = {b}, a = {a}")

# If want to call the function in the module:
# module.function_in_module()

