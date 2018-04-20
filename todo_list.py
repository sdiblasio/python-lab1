
close = True
tasks = list()


def insert():
    task = input("Insert your new task: ")
    tasks.append(task)


def delete():
    task = input("Write the task to be deleted> ")
    if task not in tasks:
        print("The task inserted was not in memorized tasks.\n")
    else:
        tasks.remove(task)


def show():
    print("\n")
    for task in tasks:
        print(task )
    print("\n")


print("Insert the number corresponding to the action you want to perform>:\n")
print("\t1. insert a new task;\n")
print("\t2. remove a task;\n")
print("\t3. show all the tasks;\n")
print("\t4. close the program.\n")

while close:
    action = int(input("Your choise: "))
    if action == 1:
        insert()
    elif action == 2:
        delete()
    elif action == 3:
        show()
    elif action == 4:
        close = False
    else:
        print("Non valid command.\n")