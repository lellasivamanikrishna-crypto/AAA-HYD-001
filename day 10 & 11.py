'''#using str.format method

name = "codegnan";course = "Python"
print(f"{name} is enrolled in {course} course")

#sequence data types--string--group of characters whcih can be encode in single double or triple code immutable ordered index collection
name="sathwik"
print(name[0])
print(name)
print(len(name))
print(len('saketh aaa'))
#type of the object
print(type(name))
print(type('name'))

#operations on string
#concatenation
x="sathwik"
print(x[0:4:2])
x="codegnan"
print(x[-5:-1])
print(x[:-8])
x="sathwik"
y=""
for i in x:
        y =i+y

    
print(y)

x = "Siva Mani"
y = ""
for i in x:
    y = i + y  # Adds the new letter to the FRONT of the growing string

print(y)  # Prints: "kiwhtas"

x = "Siva Mani 123 !"
y = ""
x="Savi Mani"
print(x.replace("i","y"))

#searching and finding methods find(),index(),count()
place="hyderabad"
print(len(place))
print(place.find('y'))#firsdt occurance of the given character of any word or string
print(place.find('Z'))# it return the -1 when character is not present
print(place.find('d',3))#we can start index of the first occurance from where it wanted to start and then find
place = "hyderabad"
print(place.index("d", 3))
#count() to count the number of times the character is repeated
print(place.count('z'))
print(place.rindex('d',-1))

#testing
print(place.islower())
print(place.isupper())
print(place.isalpha())
print(place.isalnum())
print('12345'.isdigit())
x="sathwik maddali"
print(x.replace(" ",""))
x.strip()
x.rstrip()

#split() strip() replace()
x = "sa th"

# 1. split() breaks the string into a list: ['sa', 'th']
# 2. "".join() glues them together with nothing in between
y = "".join(x.split())

print(y)  
# Output: "sath"
x=["sathwik",23,"sath",24]

print(x[1::2])
print(x[0:3:2])
print(x[-3::2])

data=['codegnan',35,4.56,['Python','java','agnetic ai','da'],100,45]
print(len(data))
print(data[3][:2])
print(data[3][2:])
print(data[3][0][0:3])
data[1]=45
print(data)
data[3][1]="rag"
print(data)
data[1:3]=['java','dsa']
print(data)
data[1:3]=['rag','mcp','agents','lora','gpt','sonet']
print(data)
data=['codegnan',35,4.56,['Python','java','agnetic ai','da'],100,45]
data.insert(1,'sathwik')
data[4][1::2]=['rag','mcp']
print(data)
data=['codegnan',35,4.56,['Python','java','agnetic ai','da'],100,45]
details=['age',32,24]
details.append(data)
print(details)
details.extend(data)
print(details)
details=['age',32,24]
details.insert(-3,['age','name'])
print(details)
details.reverse()
print(details)
'''
'''
#tuples-immutable,ordered,collection and sequence type,hetrogenous type 
data=1,24,5
print(type(data))
# nested tupes and also have lists inside it
details=('codegnan',32,(2,4,5),'saketh',[12,45,'agents','rag'])
print(len(details))
print(details[2])
print(details[4][2])
details[0].replace('n','f')#tuples are immutable and does not get modified
print(details)
details[4][2]=details[4][2].replace('a','A')#here we are using list so its mutable 
print(details)
age=22,21,32,25
ids=231,342,213
print(age+ids)
print(age*2)
deatils=('saketh','codegnan','Agwntic ai',34,23,5.8)
print(list(deatils))
s="sathwik"
print(list(s))
a=set()
print(type(a))
a={123,124,125,126,127,123,124}
print(len(a))
print(a)
#add and update()
a.add(156)
print(a)
a.update((150,128))
print(a)
#pop remove and returns arbitary if set is empty raise an error
#union intersection intersection_update difference symmetric subsets and superset
a={1,2,3}
b={4,5,3}
d=a.symmetric_difference(b)
print(d)
e=a.issubset(b)
print(e)
f=a.issuperset(b)
print(f)
temp_details=frozenset([34,35,34,32,21])
print(temp_details)
print(min(temp_details))
print(max(temp_details))
print(sorted(temp_details))
print("sathwik Maddali")
print(20)
print("vishakapatnam")
print("to become an ai engineer")
print("ECE")
print(2026)
print('kalasalingam academy of research and education')

details={'name':'sathwik','age':3,'place':'hyderaba'}
print(details)
print(details.keys())


#raise keyvalue error as we dont have a brach j
# ==========================================
# Day 10 - Dictionary & Set Operations
# ==========================================

# Dictionary
student = {
    "Name": "Lella Siva Mani Krishna",
    "Role": "Agentic AI Trainee",
    "Organization": "Codegnan"
}

print("Original Dictionary")
print(student)

# Add a new key
student["Course"] = "Python"

# Update a value
student["Role"] = "AI Engineer"

print("\nUpdated Dictionary")
print(student)

# Dictionary Methods
print("\nKeys   :", student.keys())
print("Values :", student.values())
print("Items  :", student.items())

print("\n-----------------------")

# Sets
python = {"Python", "AI", "FastAPI"}
genai = {"AI", "LLMs", "RAG"}

print("Python Set :", python)
print("GenAI Set  :", genai)

# Add & Update
python.add("Machine Learning")
python.update(["Flask"])

print("\nUpdated Set :", python)

# Set Operations
print("\nUnion                :", python.union(genai))
print("Intersection         :", python.intersection(genai))
print("Difference           :", python.difference(genai))
print("Symmetric Difference :", python.symmetric_difference(genai))
'''
#task of the day :

university = {
    "Student1": {
        "Name": "Rahul",
        "Roll_No": "24HU1A4295",
        "Department": "Computer Science",
        "Year": 3,
        "Subjects": {
            "Python": 95,
            "DBMS": 90,
            "Java": 88
        },
        "Contact": {
            "Email": "rahul@gmail.com",
            "Phone": "9876543210"
        }
    },

    "Student2": {
        "Name": "ramya",
        "Roll_No": "24HU1A42N8",
        "Department": "Electronics",
        "Year": 2,
        "Subjects": {
            "Digital Electronics": 91,
            "Microprocessors": 89,
            "Signals": 87
        },
        "Contact": {
            "Email": "ramya@gmail.com",
            "Phone": "6832693147"
        }
    }
}


print("Student Name:", university["Student1"]["Name"])
print("Python Marks:", university["Student1"]["Subjects"]["Python"])
print("Student2 Email:", university["Student2"]["Contact"]["Email"])


university["Student1"]["Subjects"]["Python"] = 98


university["Student1"]["Subjects"]["AI"] = 94


university["Student3"] = {
    "Name": "Kiran",
    "Roll_No": "24HU1A42A9",
    "Department": "Information Technology",
    "Year": 1,
    "Subjects": {
        "Programming": 85,
        "Mathematics": 92
    },
    "Contact": {
        "Email": "ravi@gmail.com",
        "Phone": "9730192738"
    }
}


del university["Student2"]["Contact"]["Phone"]


print("\nUniversity Details:")
for student, details in university.items():
    print(f"\n{student}")
    for key, value in details.items():
        print(f"{key}: {value}")



#control staements --> there are the stateements which control the flow of the execution of the program
#conditional statement if else elif
#repetative statemnets loops for and while loop
#jumping statements -break,pass,continue, assert
''' if condition:'''
#validate
students=['akash','sathwik']
name=input("enter the name:").lower()
if name in student:
    print("student is present")
else:
    print("thestudent is not there in the data given")
