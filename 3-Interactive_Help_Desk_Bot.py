# Task 1: Command Parser

user = input("What do you need today?: ") # get input from the user
answer = user.lower() # lower case the user response for easier comparison
keywords = ["login", "performance", "display", "sound", "keyboard", "mouse"]
keywords_detected = []

if (answer.find("help") > 0): # if the user mentions "help" the following is printed.
    print("Help is on the way! Please select from on the the option below.")
elif (answer.find("issue") > 0): # if the user mentions "issue" the following is printed.
    print("Seems you are having an issue. You should try restarting you computer to resolve the problem.")
    for k in keywords: # loop to categorize the type of issue if it is detected in the answer
        if (answer.find(k) > 0):
            keywords_detected.append(k)
    print("For the support team: {}".format(keywords_detected)) # print all detected issues for support team
elif (answer.find("contact support") > 0): # if the user mentions "contact support" the following is printed.
    print("If you'd like to contact support, you can call (123)-456-7890 to recieve assistance.")
else: # if the user doesn't mention a command the following is printed
    print("I am unsure how to help you.")

# Task 2: Issue Categorizer
# Shown on line 15