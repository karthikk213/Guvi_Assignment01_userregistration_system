def register():
    import re
    
    _email = input("Enter correct format email id :")
    
    regex = r'\b[A-Za-z_][A-Za-z0-9._%+:]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    def _check(email):
            if(re.fullmatch(regex, email)):
                f = open("c:/Users/admin/Documents/Guvi asignmenets/data.txt", 'a')
                f.write("\n")
                f.write(email)
                f.close()
                return email
            else:
                print("Email Format is wrong, start new registration")
                quit()
    _check(_email)

    import re

    _pswd = input("Enter correct format password:")

    reg = r"\b(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?& ])[A-Za-z\d@$!#%*?&]{5,16}\b"

    def _checkk(pswd):
        match_re = re.compile(reg)
        res = re.search(match_re, pswd)
        if res:
            f = open("c:/Users/admin/Documents/Guvi asignmenets/data.txt", 'a')
            f.write("\n")
            f.write(pswd)
            f.close()
            print("Registration success")
            return pswd
        else:
            print("Password Format is wrong, start new registartion")
            quit()
    _checkk(_pswd)


def login():
    x = input("Registered Username:")
    y = input("Registred Password:")
    with open(r'c:/Users/admin/Documents/Guvi asignmenets/data.txt') as f_obj:
        usr = f_obj.read()
        if x and y in usr:
            print("Credentials exist!. Login successfully")
        else:
            print("Start new registration")

def forgot_password():
    k = input("Registered Username:")
    infile = open('c:/Users/admin/Documents/Guvi asignmenets/data.txt','r')
    for line in infile:
        if k in line:
            print("Your username:", line, end=' ')
            print("Your Password:", next(infile), end=' ')
            return
    else:
        print("username not exist, start new registration")

    infile.close()

Q = int(input("Give 1 for Registraion or Give 2 for Login or Give 3 for Forgot Password:"))

if Q == 1:
    register()
elif Q == 2:
    login()
elif Q == 3:
    forgot_password()
else:
    print("""Your input is wrong, kindly Give 1 for Registraion or Give 2 for Login or Give 3 for Forgot Password:""")




