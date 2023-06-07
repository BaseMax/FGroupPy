class Group:
    def __init__(self, elements, operation):
        self.elements = elements  # Set of elements in the group
        self.operation = operation  # Operation that combines two elements
        self.identity_element = None
        self.inverse_elements = {}
        self.why_not_group = None

    def is_group(self):
        # Check closure property
        for a in self.elements:
            for b in self.elements:
                result = self.operation(a, b)
                if result not in self.elements:
                    self.why_not_group = [1, a, b]
                    return False

        # Check associativity property
        for a in self.elements:
            for b in self.elements:
                for c in self.elements:
                    if self.operation(self.operation(a, b), c) != self.operation(a, self.operation(b, c)):
                        self.why_not_group = [2, a, b]
                        return False

        # Check identity element
        # self.identity_element = None
        for element in self.elements:
            has_identity = True
            for other_element in self.elements:
                if self.operation(element, other_element) != other_element or self.operation(other_element, element) != other_element:
                    has_identity = False
                    break
            if has_identity:
                self.identity_element = element
                break
        if self.identity_element is None:
            self.why_not_group = [3]
            return False

        # Check inverse element
        for element in self.elements:
            inverse = self.find_inverse(element)
            if inverse is None:
                self.why_not_group = [4]
                return False
            self.inverse_elements[element] = inverse

        return True

    def find_subgroups(self):
        subgroups = []
        for subset in self.get_all_subsets():
            if self.is_group_subset(subset):
                subgroups.append(Group(subset, self.operation))
        return subgroups

    def get_all_subsets(self):
        subsets = [[]]
        for element in self.elements:
            subsets.extend([subset + [element] for subset in subsets])
        return subsets

    def is_group_subset(self, subset):
        subgroup = Group(subset, self.operation)
        return subgroup.is_group()

    def find_inverse(self, element):
        for other_element in self.elements:
            if self.operation(element, other_element) == self.identity_element and self.operation(other_element, element) == self.identity_element:
                return other_element
        return None

    def inverse(self, element):
        return self.inverse_elements.get(element, None)

    def generate_subgroup(self, element):
        subgroup_elements = set()
        current_element = element

        while current_element not in subgroup_elements:
            subgroup_elements.add(current_element)
            current_element = self.operation(current_element, element)

        return Group(subgroup_elements, self.operation)

    def is_cyclic(self):
        for element in self.elements:
            subgroup = self.generate_subgroup(element)
            if len(subgroup.elements) == len(self.elements):
                return True
        return False

    def is_acyclic(self):
        return not self.is_cyclic()

    def get_order(self):
        return len(self.elements)

    def get_element_order(self, element):
        current_element = element
        power = 1

        while current_element != self.identity_element:
            current_element = self.operation(current_element, element)
            power += 1

        return power

    def generate_multiplication_table(self):
        table = {}
        for a in self.elements:
            row = {}
            for b in self.elements:
                result = self.operation(a, b)
                row[b] = result
            table[a] = row
        return table

    def generate_md_multiplication_table(self):
        headers = list(self.elements)
        table = []

        # Generate header row
        header_row = "|   | "
        for header in headers:
            header_row += str(header) + " | "
        table.append(header_row)

        # Generate separator row
        separator_row = "|---|"
        for _ in headers:
            separator_row += "---|"
        table.append(separator_row)

        # Generate table rows
        for a in self.elements:
            row = "| " + str(a) + " | "
            for b in self.elements:
                result = self.operation(a, b)
                row += str(result) + " | "
            table.append(row)

        return "\n".join(table)

    def find_normal_subgroups(self):
        normal_subgroups = []
        for subgroup in self.find_subgroups():
            is_normal = True
            for element in self.elements:
                for subgroup_element in subgroup.elements:
                    conjugation = self.operation(self.operation(element, subgroup_element), self.inverse(element))
                    if conjugation not in subgroup.elements:
                        is_normal = False
                        break
                if not is_normal:
                    break
            if is_normal:
                normal_subgroups.append(subgroup)
        return normal_subgroups

    def is_abelian(self):
        for a in self.elements:
            for b in self.elements:
                if self.operation(a, b) != self.operation(b, a):
                    return False
        return True

    def to_permutation_list(self):
        permutation_list = []
        element_to_index = {element: index for index, element in enumerate(self.elements)}
        for element in self.elements:
            permutation = [element_to_index[self.operation(element, other_element)] for other_element in self.elements]
            permutation_list.append(permutation)
        return permutation_list

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

# Example permutation list
permutations = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]

# Convert permutation list to elements
group_elements = convert_permutation_to_elements(permutations)

print("Elements of the group:", group_elements)

elements = {0, 1, 2, 3}
elements = {0, 1, 2, 3, 4}
# elements = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}

# Create a group
group = Group(elements, addition_mod_5)
# group = Group(elements, addition_mod_15)

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
