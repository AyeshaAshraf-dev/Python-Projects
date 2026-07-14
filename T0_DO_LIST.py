# from tabulate import tabulate 
#CRUD 






to_do_list = list()
def create(to_do_list):
    
    task_name = input(str("Write the name of the task u wanna add: "))
    task_priority = input("what would be the task priority (high, medium, low)?\n")
    new_dict = {
        "task_name" : task_name,
        "task_priority" : task_priority,
        "completed" : False
    }

    to_do_list.append(new_dict) 
    print("----New task is successfully added to TO DO LIST----")
    
def view(to_do_list):
    print(to_do_list)
# create()
# print(to_do_list)
my_to_do_list = []
view(to_do_list)
# while True:
#     my_to_do_list = []
#     print("-------TO DO LIST-----\n1. ADD A TASK\n2. VIEW A TASK\n3. UPDATE A TASK\n4. DEL A TASK\n5. Exit")
#     choice_user = input("Enter the choice: ")
#     if choice_user == '5':
#         print("BYE")
#         break
#     elif choice_user == '1':
#         create(my_to_do_list)
#         continue
#     elif choice_user == '2':
#         view(my_to_do_list)
#         continue
#     else:
#         print("Invalid choice")
#         break