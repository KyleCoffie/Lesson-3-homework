#Task 1 Find out which students both submitted their assignments and attended the class.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
if "Alice" in attended and "Alice" in submitted:
    print("true")
else: print ("false")

if "Bob" in attended and "Bob" in submitted:
    print("true")
else: print ("false")

if "Charlie" in attended and "Charlie" in submitted:
    print("true")
else: print ("false")

if "David" in attended and "David" in submitted:
    print("true")
else: print ("false")

if "Eve" in attended and "Eve" in submitted:
    print("true")
else: print ("false")

if "Frank" in attended and "Frank" in submitted:
    print("true")
else: print ("false")

# Task 2 Check if the two lists are identical in terms of their content, regardless of order.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
print(submitted is not attended) 

#Task 3 Using list methods, remove any student from the attended list who did not submit their assignment.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

attended.remove("Charlie")
attended.remove("Eve")
attended.remove("Frank")
print(attended)


