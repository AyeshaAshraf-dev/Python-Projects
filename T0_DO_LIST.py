#CRUD 
import json
import time
import os
# my_to_do_list = list()

def load_file():
    filename = 'TO_DO_LIST.json'
    if os.path.exists(filename) and os.path.getsize(filename):
        try:
            with open(filename, 'r') as f:
                json.load(f)
        
        except json.JSONDecodeError:
            print("Error reading JSON file. Starting with an empty list.")
            return []
    return []
# my_to_do_list = [
#     {
#         "task_name": "cook",
#         "task_priority": "low",
#         "completed": False
#     }
# ]
# to_do_list = []
def create(my_to_do_list):
    try:
        with open('TO_DO_LIST.json', 'r') as f:
    #     json.load(my_to_do_list, f, indent=2)
            my_to_do_list = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        []
    task_name = input(str("Write the name of the task u wanna add: "))
    task_priority = input("what would be the task priority (high, medium, low)?\n")
    new_dict = {
        "task_name" : task_name,
        "task_priority" : task_priority,
        "completed" : False
    }
    my_to_do_list.append(new_dict) 
    with open('TO_DO_LIST.json', 'w') as f:
        json.dump(my_to_do_list, f, indent=2)
    

    
    print("----New task is successfully added to TO DO LIST----")
    time.sleep(1.5)
    
def view(my_to_do_list):
    try:
        with open('TO_DO_LIST.json', 'r') as f:
    #     json.load(my_to_do_list, f, indent=2)
            my_to_do_list = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        []
    if not  my_to_do_list:
        print("Empty list! Try to enter the data first ")
        time.sleep(0.7)
        return
    
    # Figure out the task number (e.g., 1).
    for index,task in enumerate(my_to_do_list, start=1):
        if task["completed"]:
            status = "[DONE]"
        else:
            status = "[PENDING]"


        print(f"{index}. {status} | Task Name: {task['task_name'].upper()} (priority: {task['task_priority']})")
    time.sleep(1.5)
    # print(f"{index}. {status_icon} | {task['task_name']} ({task['task_priority']})")

def update(my_to_do_list):
    view(my_to_do_list)
    try:
        with open('TO_DO_LIST.json', 'r') as f:
            my_to_do_list = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        []
    task_update = int(input("Which task do u want to update: \n"))
    corrected_index = task_update - 1
    # print(corrected_index)
    # print(f"DEBUG: Current list contents: {my_to_do_list}")
    # print(f"DEBUG: Current list length: {len(my_to_do_list)}")
    # print(f"DEBUG: Your corrected_index: {corrected_index}")
    if 0 <= corrected_index < len(my_to_do_list):
        task_index = input("Press 1 to mark as completed.\nPress 2 to edit the name.\nPress 3 to edit priority.\n")
        if task_index == "1":
            my_to_do_list[corrected_index]["completed"] = True
            with open('TO_DO_LIST.json', 'w') as f:
    #     json.load(my_to_do_list, f, indent=2)
                json.dump(my_to_do_list, f, indent=2)
            print("The task is mark as completed! ")
        elif task_index == "2":
            new_name = input("Enter the updated name\n: ")
            my_to_do_list[corrected_index]["task_name"] = new_name

            with open('TO_DO_LIST.json', 'w') as f:
    #     json.load(my_to_do_list, f, indent=2)
                json.dump(my_to_do_list, f, indent=2)
            print("Name is updated")
        elif task_index == "3":
            new_priority= input("Enter the updated priority(high, medium, low)?: \n")
            my_to_do_list[corrected_index]["task_priority"] = new_priority

            with open('TO_DO_LIST.json', 'w') as f:
    #     json.load(my_to_do_list, f, indent=2)
                json.dump(my_to_do_list, f, indent=2)
            print("Name is updated")
        else:
            print("invalid action choice ")

    else:
        print("Task does not exist! ")
          
    
# create()
# print(to_do_list)
# my_to_do_list = []
# view(my_to_do_list)
def main():
    try:
        with open('TO_DO_LIST.json', 'r') as f:
    #     json.load(my_to_do_list, f, indent=2)
            my_to_do_list = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        my_to_do_list = []
    my_to_do_list = load_file()
    while True:
        # my_to_do_list = []
        print("-------TO DO LIST-----\n1. ADD A TASK\n2. VIEW A TASK\n3. UPDATE A TASK\n4. DEL A TASK\n5. Exit")
        choice_user = input("Enter the choice: ")
        time.sleep(1)
        if choice_user == '5':
            print("BYE")
            break
        elif choice_user == '1':
            create(my_to_do_list)
            continue
        elif choice_user == '2':
            view(my_to_do_list)
            continue
        elif choice_user == '3':
            update(my_to_do_list)
            continue
        elif choice_user == '4':
            print("i didnt write it yet")
            del(my_to_do_list)
            continue
        else:
            print("Invalid choice")
            break


load_file()
main()

