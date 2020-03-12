from CrowdFunding import registration
from CrowdFunding import login


def main_menu():
    while True:
        print("-------- Main Menu ----------")

        choice = int(input("""
        1: Register
        2- LogIn
        3- Exit
        """))

        if choice == 1:
            registration.register()
        elif choice == 2:
            login.login_menu()
        elif choice == 3:
            exit()


print("######## CROWD FUNDING ############")
main_menu()

