def view_all_projects():
    f = open("../projects.txt", 'r')
    lines = f.readlines()
    f.close()

    print("-------------- All Projects ----------------")
    counter = 1
    for line in lines:
        if line == '\n':
            break
        line = line.split(":")
        print("Project %d" % counter)
        print("Project Title: %s" % line[0])
        print("Project Description: %s" % line[1])
        print("Total Target: %s" % line[2])
        print("Start Date: %s" % line[3])
        print("End Date: %s" % line[4])
        print("Project Owner: %s" % line[5])
        print("____________________________________________________________")
        counter += 1


def view_user_projects(user_mail):
    f = open("../projects.txt", 'r')
    lines = f.readlines()
    f.close()

    print("-------------- User Projects ----------------")
    counter = 1
    for line in lines:
        line = line.split(":")
        if line[-1] == user_mail:
            print("Project %d" % counter)
            print("Project Title: %s" % line[0])
            print("Project Description: %s" % line[1])
            print("Total Target: %s" % line[2])
            print("Start Date: %s" % line[3])
            print("End Date: %s" % line[4])
            print("Project Owner: %s" % line[5])
            print("____________________________________________________________")
            counter += 1
