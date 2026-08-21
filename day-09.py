# Nested sequence with list, tuple, set and strings

data = [
    "Python",
    "Codegnan",
    [10, 20, 30, 40],                  # List
    ("ECE", "CSE", "AI"),              # Tuple
    {100, 200, 300},                   # Set
    [
        ("Apple", "Banana"),
        {1, 2, 3},
        ["Java", "Python", "C++"],
        "Nested String"
    ]
]

print("Original Data:")
print(data)

# ----------------------------
# Accessing Elements
# ----------------------------
print("\nAccessing Elements")

print(data[0])               # Python
print(data[2])               # List
print(data[2][1])            # 20
print(data[3][2])            # AI
print(data[5][0][1])         # Banana
print(data[5][2][0])         # Java

# ----------------------------
# List Operations
# ----------------------------
print("\nList Operations")

data[2].append(50)
print("Append:", data[2])

data[2].extend([60, 70])
print("Extend:", data[2])

data[2].insert(1, 15)
print("Insert:", data[2])

data[2].remove(20)
print("Remove:", data[2])

data[2].pop()
print("Pop:", data[2])

data[2].sort()
print("Sort:", data[2])

data[2].reverse()
print("Reverse:", data[2])

# ----------------------------
# Set Operations
# ----------------------------
print("\nSet Operations")

print("Original Set:", data[4])

data[4].add(400)
print("Add:", data[4])

data[4].update([500, 600])
print("Update:", data[4])

data[4].remove(100)
print("Remove:", data[4])

data[4].discard(999)
print("Discard:", data[4])

copy_set = data[4].copy()
print("Copy:", copy_set)

print("Union:", data[4].union({700, 800}))
print("Intersection:", data[4].intersection({200, 500, 900}))
print("Difference:", data[4].difference({200, 300}))
print("Symmetric Difference:", data[4].symmetric_difference({300, 900}))

# ----------------------------
# Tuple Operations
# ----------------------------
print("\nTuple Operations")

print("Tuple:", data[3])
print("Length:", len(data[3]))
print("Index of AI:", data[3].index("AI"))
print("Count of ECE:", data[3].count("ECE"))

# ----------------------------
# String Operations
# ----------------------------
print("\nString Operations")

print(data[0].upper())
print(data[1].lower())
print(data[5][3].replace("Nested", "Deep"))
