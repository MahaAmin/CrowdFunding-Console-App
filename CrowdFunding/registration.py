import re


def validate_name(is_last):
    if is_last:
        name = input("Last Name: ")
    else:
        name = input("First Name: ")

    if name.replace(" ", "").isalpha():
        return name
    else:
        print("In-valid name!")
        return 0


def validate_email():
    email = input("Email: ")
    email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if email_regex.search(email):
        return email
    else:
        print("In-valid email!")
        return 0


def validate_password():
    '''
    Password Validation:
        1- At least one number
        2- At least one lower case and one upper case letters
        3- At least one special symbol
        4- Between 6 and 20 characters
    :return:    password
    '''

    password = input("Password: ")
    special_symbols = ['$', '@', '#', '%', '!']
    valid = True

    if len(password) < 6:
        print("In-valid password: password should be at least 6 characters long")
        valid = False
    if len(password) > 20:
        print("In-valid password: password should be at most 20 characters long")
        valid = False
    if not any(char.isdigit() for char in password):
        print("In-valid password: password should contain at least one digit")
        valid = False
    if not any(char.isupper() for char in password):
        print("In-valid password: password should contain at least one upper-case character")
        valid = False
    if not any(char.islower() for char in password):
        print("In-valid password: password should contain at least one lower-case character")
        valid = False
    if not any(char in special_symbols for char in password):
        print("In-valid password: password should contain at least one special character")
        valid = False

    if valid:
        if confirm_password(password):
            return password
        else:
            print("Passwords do not match!")
            return 0
    return 0


def confirm_password(correct_password):
    confirmed_password = input("Confirm Password: ")
    if confirmed_password == correct_password:
        return True
    return False


def validate_phone():
    mobile_phone = input("Mobile Phone: ")
    mobile_regex = re.compile(r"^020?[10,11,12]\d{8}")
    if mobile_regex.search(mobile_phone):
        return mobile_phone
    else:
        print("In-valid phone number!")
        return 0


def add_user(**kwargs):
    f = open("../users.txt", 'a')
    f.write(":".join([kwargs["First_Name"],
                      kwargs["Last_Name"],
                      kwargs["Email"],
                      kwargs["Password"],
                      kwargs["Mobile"],
                      str(kwargs["Activated"])]))
    f.write('\n')
    f.close()


def get_user_name():
    pass


def create_user():
    first_name = validate_name(0)

    if first_name:
        last_name = validate_name(1)
        if last_name:
            email = validate_email()
            if email:
                password = validate_password()
                if password:
                    phone = validate_phone()
                    if phone:
                        new_user = {"First_Name": first_name,
                                    "Last_Name": last_name,
                                    "Email": email,
                                    "Password": password,
                                    "Mobile":phone,
                                    "Activated": True}
                        return new_user
    return False


def register():
    user_data = create_user()
    if user_data:
        add_user(**user_data)
        print(user_data)
        print("Registration Succeeded!")
    else:
        print("Registration Failed!")


