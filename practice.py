try:
    Name = input("Name: ")
    phone = input("Phone: ")
    
    if len(phone) != 11 :
        print("Phone must be equal to 11")

    elif len(Name) < 2 or len(Name) > 20:
        print("Name must be between 2 to 20 charecters")
    elif Name[0].isupper:
        print("First letter of name must be Chapital")
    else:
        print("Success")

except ValueError:
    print("Phone must be integers")