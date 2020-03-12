from CrowdFunding import createProject
from CrowdFunding import viewProjects
from CrowdFunding import editProject
from CrowdFunding import deleteProject

def get_user(email,password):
    f = open("../users.txt", 'r')
    lines = f.readlines()
    f.close()
    found = False
    for line in lines:
        tmp = line.split(':')
        if tmp[2] == email and tmp[3] == password and tmp[5] == "True\n":
            found = True
            user = {"First_Name": tmp[0],
                    "Last_Name": tmp[1],
                    "Email": tmp[2],
                    "Password": tmp[3],
                    "Mobile": tmp[4],
                    "Activated": tmp[5]}

    if found:
        return user
    return {}


def login():
    email = input("Email: ")
    password = input("Password: ")
    user = get_user(email, password)
    if user:
        print("Login Succeeded!")
        return email
    else:
        print("Login Failed!")
        return 0


def login_menu():
    print("--------------- Log-In --------------------")
    user_mail = login()
    if user_mail:
        while True:
            choice = int(input("""
                1- Create new project
                2- View all projects
                3- Edit project
                4- Delete project
                5- Search for a project
                6- Exit
                """))

            if choice == 1:
                createProject.create_project(user_mail)
            elif choice == 2:
                viewProjects.view_all_projects()
            elif choice == 3:
                editProject.edit_project(user_mail)
            elif choice == 4:
                deleteProject.delete_project(user_mail)
            elif choice == 5:
                print("In search for a project")
            elif choice == 6:
                return 0


