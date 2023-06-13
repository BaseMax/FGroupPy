# FGroup Software Group in Python (FGroupPy)

FGroupPy is a software tool that allows you to perform various operations and analyses on mathematical groups. It provides a Python class called Group that represents a group and offers a set of methods to work with groups, including checking group properties, finding subgroups, generating multiplication tables, identifying normal subgroups, determining if a group is Abelian, and more.

## Installing

```bash
$ pip install dist/fgroup-1.0.0.tar.gz
Processing c:\users\max\fgroup\dist\fgroup-1.0.0.tar.gz
```

## Getting Started

To use the FGroup software, follow these steps:

- Ensure you have Python installed on your system (version 3.6 or later).
- Download the FGroup software files or clone the repository from the source.
- Import the Group class into your Python script or interactive environment.

## Class Group and Its Constructor

The Group class is the core component of the FGroup software. It represents a mathematical group and provides methods to work with groups. The constructor of the Group class takes two parameters:

```python
class Group:
    def __init__(self, elements, operation):
        self.elements = elements  # Set of elements in the group
        self.operation = operation  # Operation that combines two elements
```

- elements: A set of elements that form the group. These elements can be of any type, such as integers, characters, or objects.
- operation: A function that defines the binary operation used to combine two elements of the group. The function should take two elements as input and return the result of the operation.

## Group Properties and Analysis

The Group class provides several methods to analyze and work with groups:

### Checking Group Properties: is_group()

The is_group() method checks if the given set of elements and the operation form a valid group. It verifies the closure property, associativity property, identity element, and inverse elements of the group.

### Finding Subgroups: find_subgroups()

The find_subgroups() method finds all the subgroups of the group. It returns a list of Group objects, each representing a subgroup of the original group.

### Checking Subgroup Validity: is_group_subset(subset)

The is_group_subset(subset) method checks if a given subset of elements forms a valid subgroup of the group. It takes a list of elements as input and returns a boolean value indicating whether the subset is a valid subgroup.

### Finding Normal Subgroups: find_normal_subgroups()

The find_normal_subgroups() method finds all the normal subgroups of the group. It returns a list of Group objects, each representing a normal subgroup of the original group.

### Determining if a Group is Abelian: is_abelian()

The is_abelian() method checks if the group is Abelian, i.e., if the group's operation is commutative.

### Checking Cyclicity and Acyclicity: is_cyclic(), is_acyclic()

The is_cyclic() method checks if the group is cyclic, i.e., if there exists an element in the group that generates the entire group. The is_acyclic() method returns the opposite, indicating if the group is not cyclic.

### Getting Group Order: get_order()

The get_order() method returns the order of the group, i.e., the number of elements in the group.

### Getting Element Order: get_element_order(element)

The get_element_order(element) method returns the order of a specific element in the group. It determines the smallest positive integer n such that raising the element to the power n yields the identity element.

### Finding Inverse Element: inverse(element)

The inverse(element) method returns the inverse element of a given element in the group, if it exists. Otherwise, it returns None.

### Generating Multiplication Table: generate_multiplication_table()

The generate_multiplication_table() method generates a multiplication table for the group. It returns a dictionary where the keys represent the rows of the table and the values are dictionaries representing the entries in each row.

### Generating Markdown Multiplication Table: generate_md_multiplication_table()

The generate_md_multiplication_table() method generates a multiplication table for the group in Markdown format. It returns a string containing the table that can be directly displayed in Markdown-supported environments.

### Converting to Permutation List: to_permutation_list()

The to_permutation_list() method converts the group elements and the group's operation into a permutation list representation. It returns a list of permutations, where each permutation represents the result of applying the group operation to an element with other elements in the group.

### Example Usage

Here's an example demonstrating the usage of the FGroup software:

```python
# Import the Group class
from fgroup import Group

# Define the elements and operation for the group
elements = {'e', 'a', 'b', 'c'}

def addition_v4(a, b):
    # Define the binary operation
    # Custom operation for illustrative purposes
    # Replace with your own operation as needed
    # ...

# Create a group instance
group = Group(elements, addition_v4)

# Check if it's a group
if group.is_group():
    print("The given set and operation form a group.")
else:
    print("The given set and operation do not form a group.")

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

# Find the identity element
print("Identity element:", group.identity_element)

# Check if the group is cyclic
print("Is Cyclic:", group.is_cyclic())

# Find the order of the group
order = group.get_order()
print("The order of the group is:", order)

# Generate the multiplication table
multiplication_table = group.generate_multiplication_table()

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

# Convert the group to permutation list
permutations = group.to_permutation_list()
print("Permutation Lists:")
for permutation in permutations:
    print(str(permutation))
```

## Customization

You can customize the FGroup software by modifying the group elements, defining a different operation, or extending the Group class to add new functionality specific to your requirements.

## Conclusion
The FGroup software provides a convenient way to work with mathematical groups. By leveraging the Group class and its methods, you can analyze group properties, find subgroups, generate multiplication tables, and perform various group operations.

Copyright 2023, Max Base
