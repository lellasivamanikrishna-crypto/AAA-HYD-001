'''
regular expression --> re module -->re.search() --> 

re.compile(pattern) --> when we want to use the pattern multiple times we can use compile the pattern
'''
data = "Codegnan marks its 8 anniversary,founded in 2018"
import re
pattern = re.compile(r'\d+')
print(pattern)
result = pattern.findall(data)
print(result)
f = pattern.search(data)
print(f)
print(f.group())

#re.escape() --> we use this to escape the special character such as (.,*,?..) to treat as normal characters
#add backslash before the special characters
import re
file_name = "data.txt"
g = re.escape(file_name)
print(g)

#Form validation using re -->Email validation,mobile number validation,Pan card validation,adhar card validation,url validation,ip address validation,username validation,password validation
#Email validation
#sivamanikrishna@gmail.com, manikrishna1801@yahoo.in,18s01e200609@rvir.edu.in
import re
email = input("Enter your email: ")
pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
if pattern.fullmatch(email):
    print("Valid email")
else:
    print("Invalid email")
#mobile number validation
#10 digit number starting with 6,7,8,9
mobile = input("Enter your mobile number: ")
pattern = re.compile(r'^[6-9]\d{9}$')
if pattern.fullmatch(mobile):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
#Pan card validation
#5 letters,4 digits,1 letter
pan = input("Enter your PAN card number: ")
pattern = re.compile(r'^[A-Z]{5}[0-9]{4}[A-Z]$')
if pattern.fullmatch(pan):
    print("Valid PAN card number")
else:
    print("Invalid PAN card number")
#Adhar card validation
#12 digit number
adhar = input("Enter your Adhar card number: ")
pattern = re.compile(r'^\d{12}$')
if pattern.fullmatch(adhar):
    print("Valid Adhar card number")
else:
    print("Invalid Adhar card number")
#URL validation
#http://www.NJCodeX.com, https://Codegnan.com, www.sivamani.com
url = input("Enter the URL: ")
pattern = re.compile(r'^(https?://)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$')
if pattern.fullmatch(url):
    print("Valid URL")
else:
    print("Invalid URL")
#username validation
#username should be 5-15 characters long and can contain letters, digits, underscores,
#and should not start with a digit
username = input("Enter your username: ")
pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]{4,14}$')
if pattern.fullmatch(username):
    print("Valid username")
else:
    print("Invalid username")
#password validation
#password should be 8-20 characters long and must contain at least one uppercase letter,
#one lowercase letter, one digit, and one special character
password = input("Enter your password: ")
pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$')
if pattern.fullmatch(password):
    print("Valid password")
else:
    print("Invalid password")

