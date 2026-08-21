#assert keyword is mainly used for debugging cases in developement 
#it checks for the given condition to be validated if condition is true it raises the Assertion error
#assert will give up the condition and throw away the error it is user defined error message
#x=int(input("enter the positive number:"))
#assert x>0,"value should be only +ve"
#x+=2
#print(f"updated value is {x}")
'''assert x in [12,24,23]
print("search found")
help()'''
#nested loops - pattern generation
''' for i in range(outer_loop):
        for j in range(inner_loop):
            #statements
            '''
#every outer loop inner loop is executed
#rows and columns outer and inner loop


'''for i in range(3):
    for j in range(2):
        print(f'value of i is {i},value of j is {j}')
        print(i,j)'''
#number patterns row based number patterns,traingles..
'''1 2 3 
1 2 3 
1 2 3 
'''
'''for i in range(1,4):
    for j in range(1,4):
        print(j,end=" ")
    print()'''
'''
for i in range(1,5):
    for j in range(1,4):
        print(j,end=" ")
    print()

for i in range(1,4):
    for j in range(1,4):
        print(i,end=" ")
    print()

for i in range(ord('A'),ord('A')+3):
    for j in range(1,4):
        print(chr(i),end=" ")
    print()

for i in range(1):
    for j in range(4):
        print("*" * j)
    print()
'''
'''
z=1
for i in range(1,4):
    for j in range(1,4):
        print(z,end=" ")
        z+=1
    print()
for i in range(3):
    for j in range(4):
        print("*",end=" ")
    print()
'''
for i in range(1):
    for j in range(5):
        print("*" * j)
    print()








