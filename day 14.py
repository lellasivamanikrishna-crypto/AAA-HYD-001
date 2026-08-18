'''
#repetition statements --> for, while

#while --> checks untill and unless the given condition is satisfied (True)

syntax:

while condition:
      statement(s)..
      ...

#Simple usage to understand while
count = 0
while count < 5:
    print("okey you have acc")
    a=[]
    a.append("codegnan")
    print(a)
    count = count+1 #Addition Assignment operator

#Checking the valid attempts
count = 5
while count >= 1:
    print(count)
    count = count -1

#To find a valid password
password = input("Enter the password:")
while password != "Nani":
    password = input("Enter the correct password:")

print(f'correct password--> Access Granted')


#Give user a chance to type password again until he gives correct password
#Now give only 3 chances for password check
password = input("Enter the password: ")
attempt = 1
while password != "Nani":
    print(f"Attempts left: {3 - attempt}")   
    if attempt >= 3:
        print("Your 3 Attempts are over.")
        print("Account Freezed")
        break   
    password = input("Enter the correct password: ")
    attempt += 1
else:
    print("Login Successfull")



#for with else,while with else -->else will be executed only when loop is completely done
#Search for a product in the store

search = input("Enter the search item: ")
store = ["Mobile,Laptop,Charger,Powerbank"]
for item in store:
    if item in store:
        print("item is found")
        break
else:
    print("item is missing")


#task: PIN Verification user should be given 3 chances if 3rd chance is over
#it should return Account Locked for 24hours -->balance, withdrawl,show the number of chances you have
#Push it to Github and Linkdin post


#break,continue,pass -->Jumping statements
#break -->it terminates the loop once the given condition is satisfied
#continue --> it basically skips the current iteration and gets back to the next iteration

for i in "codegnan":
    if i == "g":
        continue
        #break
    print(i)


#pass -->It is generally used as a placeholder (to have any syntax matches)

for i in range(10)
    pass
    #print("Hello")
    
'''




















