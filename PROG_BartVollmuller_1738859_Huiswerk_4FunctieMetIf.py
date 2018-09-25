def new_password(oldpassword, newpasword):
    if str(oldpassword) != str(newpasword) and len(newpasword) >6:
        print("True")
    else:
        print("False")
new_password("bartvollmuller", "jonathan")
