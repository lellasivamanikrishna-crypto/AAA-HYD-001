
rows = 5
#diamond shape
# Upper Part
for i in range(1, rows + 1):

    for j in range(rows - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()

# Lower Part
for i in range(rows - 1, 0, -1):

    for j in range(rows - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()

#floyd's traiangle
num = 1

for i in range(1, 6):

    for j in range(i):
        print(num, end=" ")

        num += 1

    print()
#continuous alphabet traingle

ch = 65

for i in range(1, 6):

    for j in range(i):
        print(chr(ch), end=" ")

        ch += 1

    print()
#triangle
rows = 5

for i in range(1, rows + 1):

    for j in range(rows - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()
#inverted traingle

rows = 5

for i in range(rows, 0, -1):

    for j in range(rows - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()
