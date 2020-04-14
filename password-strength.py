def passwdCheck():
    match ='false'
    #continue until the passwords match
    while match == 'false':
        passwd1 = input("Please enter a new password ")
        passwd2 = input("Please re-enter your password ")
        if passwd1 == passwd2:
            print("Great, those passwords match")
            match = 'true'
        else:
            print("Sorry, your passwords don't match, please try again")
    return passwd2
def passwdStrength(pwd):
    #if the password is either all numbers or letters of the alphabet - weak
    if (pwd.isalpha()) or (pwd.isnumeric()):
        print("Your password is weak")
    #if the password is alphanumeric - medium
    elif (pwd.isalnum()):
        print("Your password is medium strength")
    #else password contains other characters - strong
    else:
        print("Your password is strong")
passwd = passwdCheck()
passwdStrength(passwd)

