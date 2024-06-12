"""
Variable Scopes
1) Local Scope
2) Enclosed Scope
3) Global Scope
4) builtins
"""

print("1) Local Scope:")
print("-"*20)
# ------------

def f():
    a = 100 # Local Scope, We can't access outside the function
    print("Inside Func, value of a is: ", a)

f()
# print("Value of a:", a) # WE CAN'T ACCESS HERE

print("#"*40, end="\n\n")
#########################

print("2) Global Scope:")
print("-"*20)
# ------------

x = 100 # Global scope, we can access anywhere in the program
def f():
    print("Inside f() global x is :", x) # We can access
f()
print("Value of x in global:", x)

print("#"*40, end="\n\n")
#########################