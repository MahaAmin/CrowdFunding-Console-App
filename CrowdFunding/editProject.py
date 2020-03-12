from CrowdFunding import createProject


def edit_project(user_mail):
    print("--------------- Edit Project --------------------")
    project_title = input("Project Title: ")

    project = {"Title": input("New Project Title: "),
               "Details": input("New Project Details: "),
               "Total_Target": input("New Total Target: "),
               "Start_Time": createProject.validate_datetime(input("New Start Time (dd/mm/yy): ")),
               "End_Time": createProject.validate_datetime(input("New End Time (dd/mm/yy): ")),
               "User": user_mail
               }

    f = open("../projects.txt", 'r')
    lines = f.readlines()
    f.close()

    new_lines = []
    for line in lines:
        line = line.split(":")
        if line[0] == project_title and line[-1].strip('\n') == user_mail:
            line[1] = project["Details"]
            line[2] = project["Total_Target"]
            line[3] = project["Start_Time"]
            line[4] = project["End_Time"]
            line[5] = project["User"]+'\n'
            line = ":".join(line)
            new_lines.append(line)
        else:
            line = ":".join(line)
            new_lines.append(line)

    f = open("../projects.txt", 'w')
    f.writelines(new_lines)
    f.close()
    print("Project Saved!")



