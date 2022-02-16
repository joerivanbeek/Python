master = input("What is the master password?")

def view():
    with open("Passwords.txt","r") as f: 
        for line in f.readlines():
            data = (line.rstrip()) #skips breaklines
            user, pwd = data.split("|") #split based on character
            print("User:",user,"| Password:",pwd)
            
def add():
    name = input("Account name: ")
    password = input("Password: ")
    
    with open("Passwords.txt","a") as f: #opens and closes file // a for append // w for write // r for read // can do file and file close
        f.write(name + "|" + password + "\n") #breakline

while True:
    mode = input("Would you like to add a new password or view excisting ones (view/add), press q to quit?").lower()
    if mode == "q":
        break   
     
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue