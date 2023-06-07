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

# def multiplication_mod_6(a, b):
#     return (a * b) % 6

def addition_mod_4(a, b):
    return (a * b) % 4

def addition_mod_5(a, b):
    return (a + b) % 4

elements = {0, 1, 2, 3}#, 4}

# Create a group
group = Group(elements, addition_mod_5)

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
# (2 + x) / 5 = 0 ==> 3 is inverse of 2
# (4 + x) / 5 = 0 ==> 1 is inverse of 4

print("Identity element:", group.identity_element)

print("Is Cyclic: ", group.is_cyclic())
print("Is A-Cyclic: ", group.is_acyclic())
