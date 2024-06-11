"""
for-loop: Iterate any collection
"""

print("for loop with string/list/any-other-collections")
print("-"*20)
# ------------------

my_string= "Python"
print("my_string:", my_string)

# Syntax: for any_variable_name in any_collection
for i in my_string:
    print("Each Char:", i)
print("\n\n")

my_list = ["C", "Java-1", "python", "Java-2", "Perl"]
print("my_list:", my_list)
for j in my_list:
    print("Each Value:", j)

print("#"*40, end="\n\n")
########################################

print("for loop with Dictionary")
print("-"*20)
# ------------------

my_dictionary = {"course": "python", "duration": 10, "location": "india"}
print("my_dictionary:", my_dictionary, end="\n\n")

# >>> my_dictionary.keys()
# ['course', 'duration', 'location']
# >>>
print("Using my_dictionary.keys()")
for each_key in my_dictionary.keys():
    print("each_key:", each_key)
    print("Value:", my_dictionary[each_key])
print("\n\n")

# >>> my_dictionary.values()
# ['python', 10, 'india']
print("Using my_dictionary.values()")
for each_value in my_dictionary.values():
    print("Each Value:", each_value)
print("\n\n")

# >>> my_dictionary.items()
# [('course', 'python'), ('duration', 10), ('location', 'india')]
print("Using my_dictionary.items()")
for each_item in my_dictionary.items():
    print("Each Item:", each_item)
    print("Key:", each_item[0])
    print("Value:", each_value[1])
print("\n\n")

print("#"*40, end="\n\n")
########################################

