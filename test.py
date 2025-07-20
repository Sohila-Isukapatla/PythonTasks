fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list =[]

for x in fruits:
    if "a" in x :
        new_list.append(x)

print(new_list)

list_b = [x for x in fruits if "a" not in x]
