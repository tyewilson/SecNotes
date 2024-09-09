Login = open ("login.txt", "w+" )

Pass = input (f"""

Would you like to create a new password?: """)

Pass = Pass.lower()

if Pass == "yes":
    print ("ello")