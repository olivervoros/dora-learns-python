"""
PYTHON LISTS: QUICK GUIDE AND PRACTICE
======================================

A list stores multiple values in one variable. Lists:

* keep their order;
* can contain duplicate values;
* can be changed after they are created;
* use zero-based indexes (the first item has index 0).

Example:
    fruits = ["apple", "banana", "orange"]
    print(fruits[0])   # apple
    print(fruits[-1])  # orange (negative indexes count from the end)

COMMON LIST OPERATIONS AND METHODS
----------------------------------

    len(items)                  Number of elements
    items[index]                Read an element
    items[index] = new_value    Change an element
    items.append(value)         Add one value to the end
    items.insert(index, value)  Add a value at a chosen position
    items.extend(other_list)    Add all values from another iterable
    items.remove(value)         Delete the first matching value
    items.pop(index)            Delete and return an element
    del items[index]            Delete an element or slice
    items.clear()               Delete every element
    items.index(value)          Find the index of the first match
    items.count(value)          Count matching values
    items.sort()                Sort the original list
    sorted(items)               Return a new sorted list
    items.reverse()             Reverse the original list
    value in items              Check whether a value exists

Slicing selects part of a list:
    items[start:stop:step]

List comprehensions are a compact way to transform or filter a list:
    squares = [number ** 2 for number in numbers]
    evens = [number for number in numbers if number % 2 == 0]
"""


def examples():
    """Run short examples of the most common list operations."""
    fruits = ["apple", "banana", "orange"]
    print("Original:", fruits)

    # Add elements.
    fruits.append("mango")
    fruits.insert(1, "pear")
    fruits.extend(["kiwi", "grape"])
    print("After adding:", fruits)

    # Read and change elements.
    print("First fruit:", fruits[0])
    fruits[2] = "blueberry"
    print("After changing index 2:", fruits)

    # Delete elements in several ways.
    fruits.remove("pear")
    removed_fruit = fruits.pop()
    del fruits[0]
    print("After deleting:", fruits)
    print("pop() returned:", removed_fruit)

    # Search and count.
    print("Does the list contain mango?", "mango" in fruits)
    print("Index of mango:", fruits.index("mango"))
    print("Number of oranges:", fruits.count("orange"))

    # Sort without changing the original list.
    sorted_fruits = sorted(fruits)
    print("New sorted list:", sorted_fruits)
    print("Original is unchanged:", fruits)

    # Sort the original list, then reverse it.
    fruits.sort()
    fruits.reverse()
    print("Original sorted in reverse order:", fruits)

    # Slice, transform, and filter.
    numbers = [1, 2, 3, 4, 5, 6]
    print("First three numbers:", numbers[:3])
    print("Squares:", [number ** 2 for number in numbers])
    print("Even numbers:", [number for number in numbers if number % 2 == 0])


# PRACTICE TASKS
# Complete each task by replacing the TODO line. Print your result after each one.


def task_1_add_items():
    """Add 'milk' to the end, then insert 'bread' at the beginning."""
    shopping = ["eggs", "rice"]
    # TODO: Add and insert the requested items.
    shopping.append("milk")
    shopping.insert(0, "bread")
    print("Task 1:", shopping)


def task_2_change_an_item():
    """Change 'blue' to 'purple' using its index."""
    colours = ["red", "blue", "green"]
    # TODO: Change the correct element.
    colours[1] = "purple"
    print("Task 2:", colours)


def task_3_delete_items():
    """Remove 'spam', then remove and save the final element with pop()."""
    foods = ["pasta", "spam", "salad", "soup"]
    removed_item = None
    # TODO: Remove "spam" and assign the popped item to removed_item.
    foods.remove("spam")
    removed_item = foods.pop(2)
    # OLIVER: Az utolsó elem indexe -1, így ezt is lehetne használni, de a feladat szerint a végső elemet kell eltávolítani, így a pop() hívásnál nem kell indexet megadni.
    print("Task 3 popped item:", removed_item)


def task_4_sort_items():
    """Sort scores from lowest to highest, then create a descending copy."""
    scores = [42, 17, 88, 63, 29]
    descending_scores = []
    # TODO: Sort scores and create descending_scores with sorted().
    scores.sort()  # nem kell-e eléírnom egy változót? # OLIVER: A sort függvény a listát módosítja, így nem kell új változót létrehozni. A sorted() viszont egy új listát ad vissza, ezért azt érdemes egy változóba menteni.
    descending_scores = sorted(scores, reverse=True)
    print("Task 4 ascending:", scores)
    print("Task 4 descending:", descending_scores)


def task_5_filter_items():
    """Use a list comprehension to keep only temperatures above 20."""
    temperatures = [12, 25, 18, 31, 20, 27]
    warm_temperatures = []
    # TODO: Replace [] above with a filtering list comprehension.
    warm_temperatures = [temperature for temperature in temperatures if temperature >20] 
    print("Task 5:", warm_temperatures)


def task_6_transform_items():
    """Create a new list containing each price with 20% tax added."""
    prices = [10.00, 25.50, 8.75]
    prices_with_tax = []
    # TODO: Use a list comprehension. Round each result to two decimal places.
    prices_with_tax = [round(price* 1.2, 2) for price in prices]
    print("Task 6:", prices_with_tax)


def task_7_remove_duplicates():
    """Create a new list with duplicates removed while preserving order."""
    names = ["Ana", "Ben", "Ana", "Chen", "Ben"]
    unique_names = []
    # TODO: Loop through names and append a name only if it is not already present.
    for name in names:
        if name not in unique_names:
            unique_names.append(name)
    print("Task 7:", unique_names)


def task_8_challenge():
    """Keep passing grades (>= 50), sort them high-to-low, and find the average."""
    grades = [73, 41, 95, 50, 38, 82, 67]
    passing_grades = []
    average = 0
    # TODO: Filter, sort, and calculate the average of passing_grades.
    passing_grades = sorted([grade for grade in grades if grade >=50], reverse=True) 
    average = sum(passing_grades) / len(passing_grades)
    print("Task 8 passing grades:", passing_grades)
    print("Task 8 average:", average)


if __name__ == "__main__":
    print("=== EXAMPLES ===")
    examples()

    print("\n=== YOUR PRACTICE RESULTS ===")
    task_1_add_items()
    task_2_change_an_item()
    task_3_delete_items()
    task_4_sort_items()
    task_5_filter_items()
    task_6_transform_items()
    task_7_remove_duplicates()
    task_8_challenge()
