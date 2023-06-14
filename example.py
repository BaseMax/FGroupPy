# import fgrouppy

# def multiplication_mod_6(a, b):
#     return (a * b) % 6

def addition_mod_4(a, b):
    return (a * b) % 4

def addition_mod_5(a, b):
    return (a + b) % 5

def addition_mod_15(a, b):
    return (a + b) % 15

def convert_permutation_to_elements(permutations):
    elements = set()
    for permutation in permutations:
        elements.update(permutation)
    return elements

def addition_v4(a, b):
    if a == 'a' and b == 'b':
        return 'c'
    if a == 'b' and b == 'a':
        return 'c'
    if a == 'b' and b == 'c':
        return 'a'
    if a == 'c' and b == 'b':
        return 'a'
    if a == 'c' and b == 'a':
        return 'b'
    if a == 'a' and b == 'c':
        return 'b'

    if a == 'e' and b == 'e':
        return 'e'
    if a == 'e' and b == 'a':
        return 'a'
    if a == 'e' and b == 'b':
        return 'b'
    if a == 'e' and b == 'c':
        return 'c'

    if a == 'a' and b == 'a':
        return 'e'
    if a == 'b' and b == 'b':
        return 'e'
    if a == 'c' and b == 'c':
        return 'e'

    if addition_v4(b, a) != None:
        return addition_v4(b, a)

    return None

# Example permutation list
permutations = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]

# Convert permutation list to elements
group_elements = convert_permutation_to_elements(permutations)

print("Elements of the group:", group_elements)

elements = {0, 1, 2, 3}
elements = {0, 1, 2, 3, 4}
# elements = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
elements = {'e', 'a', 'b', 'c'}

# Create a group
# group = Group(elements, addition_mod_5)
# group = Group(elements, addition_mod_15)
group = Group(elements, addition_v4)

# Check if it's a group
if group.is_group():
    print("The given set and operation form a group.")
else:
    print("The given set and operation do not form a group" + " for rule #" + str(group.why_not_group[0]) + ".")

# Find all subgroups
subgroups = group.find_subgroups()
print("Subgroups:")
for subgroup in subgroups:
    print(subgroup.elements)

# Find inverse elements
print("Inverse elements:")
for element in elements:
    inverse = group.inverse(element)
    print(f"Inverse of {element} is {inverse}")

print("Identity element:", group.identity_element)

print("Is Cyclic: ", group.is_cyclic())
print("Is A-Cyclic: ", group.is_acyclic())

# Find order of group
order = group.get_order()
print("The order of the group is:", order)

# Find order elements
print("Inverse elements:")
for element in elements:
    order = group.get_element_order(element)
    print(f"Order of element {element} is {order}")

# Generate the multiplication table
multiplication_table = group.generate_multiplication_table()

# Print the multiplication list
# print("Multiplication Table:")
# for a, row in multiplication_table.items():
#     for b, result in row.items():
#         print(f"{a} * {b} = {result}")

# Print the multiplication table
print("Multiplication Table:")
print(group.generate_md_multiplication_table())

# Find normal subgroups
normal_subgroups = group.find_normal_subgroups()

# Print the normal subgroups
print("Normal Subgroups:")
for subgroup in normal_subgroups:
    print(subgroup.elements)

# Check if the group is Abelian
if group.is_abelian():
    print("The group is Abelian.")
else:
    print("The group is not Abelian.")

# Print permutation list
permutations = group.to_permutation_list()
print(f"Permutation Lists:")
for permutation in permutations:
    print(str(permutation))
