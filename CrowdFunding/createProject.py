import datetime


def validate_datetime(input_date):
    try:
        day, month, year = input_date.split('/')
        valid_date = True
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        valid_date = False

    if valid_date:
        return input_date
    else:
        print("In-valid date!")
        return 0


def save_project(**kwargs):
    f = open("../projects.txt", 'a')
    f.write(":".join([kwargs["Title"],
                      kwargs["Details"],
                      kwargs["Total_Target"],
                      kwargs["Start_Time"],
                      kwargs["End_Time"],
                      kwargs["User"]]))
    f.write('\n')
    f.close()
    print("Project Created!")


def validate_project(user_mail):
    title = input("Project Title: ")
    if ":" in title:
        pass
    if title:
        details = input("Project Details: ")
        total_target = input("Total Target: ")
        if total_target:
            start_date = validate_datetime(input("Start Time (dd/mm/yy): "))
            if start_date:
                end_date = validate_datetime(input("End Time (dd/mm/yy): "))
                if end_date:
                    project = {"Title": title,
                               "Details": details,
                               "Total_Target": total_target,
                               "Start_Time": start_date,
                               "End_Time": end_date,
                               "User": user_mail}
                    return project
    else:
        print("Title can not be empty!")
    return False


def create_project(user_mail):
    project = validate_project(user_mail)

    if project:
        save_project(**project)
    else:
        print("Project creation failed!")




