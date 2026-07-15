#CRUD 
import json
import time
# my_to_do_list = list()
my_to_do_list = []


# my_to_do_list = [
#     {
#         "task_name": "cook",
#         "task_priority": "low",
#         "completed": False
#     }
# ]
to_do_list = []
def create(to_do_list):
   
    with open('TO_DO_LIST.json', 'r') as f:
    #     json.load(my_to_do_list, f, indent=2)
        to_do_list = json.load(f)
    task_name = input(str("Write the name of the task u wanna add: "))
    task_priority = input("what would be the task priority (high, medium, low)?\n")
    new_dict = {
        "task_name" : task_name,
        "task_priority" : task_priority,
        "completed" : False
    }
    to_do_list.append(new_dict) 
    with open('TO_DO_LIST.json', 'w') as f:
        json.dump(to_do_list, f, indent=2)
    

    
    print("----New task is successfully added to TO DO LIST----")
    time.sleep(1.5)
    
def view(my_to_do_list):
    with open('TO_DO_LIST.json', 'r') as f:
    #     json.load(my_to_do_list, f, indent=2)
        to_do_list = json.load(f)
    my_to_do_list = to_do_list
    if not  my_to_do_list:
        print("Empty list")
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

def update(to_do_list):
    view(my_to_do_list)
    task_update = int(input("Enter the number of the task u want to update: "))
    corrected_index = int(task_update) - 1
    task_index = input("Press 1 to mark as completed\nPress 2 to edit the name\nPress 3 to edit priority\n")
    # 1. Open TO_DO_LIST.json in "w" (write) mode ──> 
    # 2. This completely clears the old file on your disk ──> 
    # 3. Python writes the entire updated list (with the [DONE] status) into the file ──> 
    # 4. Close the file
    if task_index == 1:
        my_to_do_list[task_index]["completed"] = True
        with open('TO_DO_LIST.json', 'w') as f:
    #     json.load(my_to_do_list, f, indent=2)
            json.dump(my_to_do_list, f, indent=2)
        print("The task is mark as completed! ")
    elif task_index == 2:
        new_name = input("Enter the updated name: ")
        my_to_do_list[task_index]["task_name"] = new_name

        with open('TO_DO_LIST.json', 'w') as f:
    #     json.load(my_to_do_list, f, indent=2)
            json.dump(my_to_do_list, f, indent=2)
        print("Name is updated")
    if not task_update:
        print("Task don't exist! ")
        return  
    pass
# create()
# print(to_do_list)
# my_to_do_list = []
# view(my_to_do_list)
while True:
    # my_to_do_list = []
    print("-------TO DO LIST-----\n1. ADD A TASK\n2. VIEW A TASK\n3. UPDATE A TASK\n4. DEL A TASK\n5. Exit")
    choice_user = input("Enter the choice: ")
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
        break
    else:
        print("Invalid choice")
        break