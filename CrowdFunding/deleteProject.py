def delete_project(user_mail):
    print("-------------- Delete Project ---------------------")
    project_title = input("Project Title: ")

    f = open("../projects.txt", 'r')
    lines = f.readlines()
    f.close()

    new_lines = []
    for line in lines:
        line = line.split(":")
        if not (line[0] == project_title and line[-1].strip('\n') == user_mail):
            line = ":".join(line)+'\n'
            new_lines.append(line)

    f = open("../projects.txt", 'w')
    f.writelines(new_lines)
    f.close()
