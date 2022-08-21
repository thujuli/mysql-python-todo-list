from db_conf import DBConfig
import os


def start():
    os.system("clear")
    template_str = """What do You want to do Today?
1. See All My Task
2. Add new Task
3. Delete My Task
4. Update My Task (Sucessfull)
"""
    print("-" * 50)
    print(" MY TODO LIST ".center(50, "-"))
    print("-" * 50)
    print(template_str)


def banner(string, *args):
    print("-" * 50)
    print(f" {string} ".center(50, "-"))
    print("-" * 50)

    for value in args:
        if value == template_str:
            print(value)


def get_input():
    while True:
        input_user = input("Input Number type (1 to 4)!: ")

        try:
            if int(input_user) in range(1, 5):
                return int(input_user)
                break
        except Exception as err:
            print("\n {} \n".format(err))
            continue
        else:
            print("Try Again, PLEASE INPUT (1 TO 4)!\n")


def main(func):
    user = DBConfig()
    input_user = func()

    try:
        if input_user in range(1, 5):
            user.fetch_all()

        if input_user == 2:
            task = input("New Task: ")
            user.insert(task)
        elif input_user == 3:
            task_id = int(input("Insert Task ID to Delete: "))
            user.delete(task_id)
        elif input_user == 4:
            update_task = int(input("Insert Task ID to Update: "))
            user.update_finish(update_task)
    except Exception as err:
        print("\n {} \n".format(err))


template_str = """What do You want to do Today?
1. See All My Task
2. Add new Task
3. Delete My Task
4. Update My Task (Sucessfull)
"""

# Main Program
while True:
    banner("TO DO LIST", template_str)
    main(get_input)

    is_repeat = input("\nRepeat (y/n)?: ")
    try:
        if is_repeat.lower() != "y":
            print()
            break
        else:
            continue
    except Exception as err:
        print("\n {} \n".format(err))


banner("Goodbye, have a nice Day!")
