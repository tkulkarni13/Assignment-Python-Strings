# Task 1: Input Length Validator

first_name = "Tejas"
last_name = "Kulkarni"

def verifyNameLength(first, last): # make sure both first and last names are longer than 2 characters
    if (len(first) < 2 or len(last) < 2): # compare lengths of both names to make sure they are both long than 2 characters
        print("Error! Names must have at least 2 characters") # print error if any name is too short
        return False
    else:
        return True
    
verifyNameLength(first_name, last_name)

# Task 2: Password Complexity Checker

def verifyPasswordComplexity(password): # verify that a password is complex enough
    if (len(password) < 8): # check if password is at least than 8 characters
        print("Your password must be at least 8 characters long, contain 1 uppercase, 1 lowercase letter, and 1 number.")
        return False
    elif (not any(c.isupper() for c in password)): # check if at least one character capitalized
        print("Your password must be at least 8 characters long, contain 1 uppercase, 1 lowercase letter, and 1 number.")
        return False
    elif (not any(c.islower() for c in password)): # check if at least one character is lowercase
        print("Your password must be at least 8 characters long, contain 1 uppercase, 1 lowercase letter, and 1 number.")
        return False
    elif (not any(c.isdigit() for c in password)): # check if at least one character is a digit
        print("Your password must be at least 8 characters long, contain 1 uppercase, 1 lowercase letter, and 1 number.")
        return False
    else: # return true for a valid password if all above requirements are complete
        return True

# Tests to make sure password verification works
print(verifyPasswordComplexity("ThatIsInsane123"))
print(verifyPasswordComplexity("Tha123"))
print(verifyPasswordComplexity("thatisinsane123"))
print(verifyPasswordComplexity("THATISINSANE123"))
print(verifyPasswordComplexity("ThatIsInsane"))
print()

# Task 3: Email Formatter

def verifyEmail(email): # function to verify a proper email address
    if (not (email[-4:] == ".com" or email[-4:] == ".edu")): # check if the email address ends with a .com or .edu
        print("Invalid email.")
        return False
    elif (not any (c == "@" for c in email)): # check if the email address contains "@"
        print("Invalid email.")
        return False
    elif ("@" == email[0]): # check that the email address starts with a valid character
        print("Invalid email.")
        return False
    else: # return true for a valid email if it passes the above requirements
        return True

# Testing email verification
print(verifyEmail("tejas.pie@gmail.com"))
print(verifyEmail("professor@university.edu"))
print(verifyEmail("hello"))
print(verifyEmail("tubby@yahoo.cmo"))
print(verifyEmail("@hotels.com"))