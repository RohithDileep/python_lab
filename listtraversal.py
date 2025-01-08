lst = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("\n# Traversing using len():")
for i in range(len(lst)):
    print(lst[i], end=" ")
print()

print("\n# Traversing using range():")
for i in range(len(lst)):
    print(lst[i], end=" ")
print()

print("\n# Traversing using enumerate():")
for index, value in enumerate(lst):
    print(f"Index {index}: {value}")
