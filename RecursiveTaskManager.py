def init_tasks():
    return [
        {'id': 1, 'description': "Complete Project Proposal", 'assigned_to': "John Doe", "subtasks": [
            {'id': 2, 'description': "Research", 'assigned_to': "Alice Brown", 'time_estimate': 5},
            {'id': 3, 'description': "Outline", 'assigned_to': "Bob Johnson", 'subtasks': [
                {'id': 4, 'description': "Introduction", 'assigned_to': "Jane Smith", 'time_estimate': 3},
                {'id': 5, 'description': "Body", 'assigned_to': "Jane Smith", 'time_estimate': 6},
                {'id': 6, 'description': "Conclusion", 'assigned_to': "David Wilson", 'time_estimate': 2}
                ]}
        ]}]
# this func is to determine the id
def count_elements(my_list,id):
    counter = 0
    for task in my_list:
        counter += 1
        if "subtasks" in task:
            counter += count_elements(task["subtasks"],id)
        if task["id"] == id:
            break
    return counter
# after change with using this func ı can set ids
def setIds(my_list,id,found = False):
    for task in my_list:
        if found:
            task['id'] += 1
        if task['id'] == id:
            found = True
        if 'subtasks' in task:
            found = setIds(task['subtasks'], id, found)
    return found
#this is for simple printing before choosing id
def print_tasks(my_list,depth=0):
    for task in my_list:
        indent_symbol = "--" * depth
        id = task["id"]
        description = task["description"]
        assign_to = task["assigned_to"]
        print(f"{indent_symbol}{id}. {description} ({assign_to})")
        if "subtasks" in task:
            print_tasks(task["subtasks"],depth+1)
def add_task_recursive(my_list,id,new_task):
    if id == 0:
        my_list.append(new_task)
    else:
        for task in my_list:
            if task["id"] == id:
                if "subtasks" in task:
                    task["subtasks"].append(new_task)
                else:
                    # we dont need time_estimate properties if it has subtasks so I remove it
                    task.pop("time_estimate")
                    task["subtasks"] = []
                    task["subtasks"].append(new_task)
            elif "subtasks" in task:
                    add_task_recursive(task["subtasks"],id,new_task)   

def assign_task(my_list,id,person):
    for task in my_list:
        if task["id"] == id:
            task["assigned_to"] = person
        elif "subtasks" in task:
            assign_task(task["subtasks"],id,person)
def complete_task_recursive(my_list,id,found = False):
    description = None
    for task in my_list:
        if task["id"] == id:
            task["is_completed"] = True
            description = task["description"]
            if "subtasks" in task:
                # If I found correct task and task has subtasks I must change subtasks too. For this I use flag.
                found = True
                complete_task_recursive(task["subtasks"],id,found)
                break
        elif "subtasks" in task:
            description = complete_task_recursive(task["subtasks"],id,found)
        elif found:
            task["is_completed"] = True
    return description

def calculate_time_recursive(my_dict):
    result = 0
    completed_time = 0
    if "time_estimate" in my_dict:
        result = my_dict["time_estimate"]
        if "is_completed" in my_dict:
            completed_time = my_dict["time_estimate"]
    else:
        for task in my_dict["subtasks"]:
            result_temp,completed_time_temp = calculate_time_recursive(task)
            result += result_temp
            completed_time += completed_time_temp
    return result,completed_time

def generate_report_recursive(my_list,depth=0):
    total_time = 0
    total_completed_time = 0
    for task in my_list:
        indent_symbol = "--" * depth
        id = task["id"]
        description = task["description"]
        assign_to = task["assigned_to"] 
        task_total_time,completed_time = calculate_time_recursive(task)
        is_completed = "Completed" if (task_total_time-completed_time) == 0 else "Pending"
        total_time += task_total_time
        total_completed_time += completed_time
        print(f"{indent_symbol}{id}. {description} ({assign_to}) --Estimated Time to Finish: {task_total_time-completed_time} out of {task_total_time} hours, {is_completed}")
        if "subtasks" in task:
            generate_report_recursive(task["subtasks"],depth+1)
    return total_time,total_completed_time
def main():
    tasks = init_tasks()
    while True:
        print("""\n1.Add a new task\n2.Assign a task to a team member\n3.Complete a task\n4.Generate report\n5.Exit""")
        user_input = input("Please select an operation:")
        if user_input == "1":
            print_tasks(tasks)
            id = int(input("To add a new task, enter 0. To add a subtask, select the task ID: "))
            description = input("Please enter the task description: ")
            assign_to = input("Please enter the task responsible: ")
            time_estimate = int(input("Please enter the estimated time for the task: "))
            new_task = {}
            new_task["id"] = id+1 if id != 0 else count_elements(tasks,id)+1
            new_task["description"] = description 
            new_task["assigned_to"] = assign_to
            new_task["time_estimate"] = time_estimate
            add_task_recursive(tasks,id,new_task)
            setIds(tasks,new_task["id"])
            print("new task added!")
            input("Please press enter to continue...")
        elif user_input == "2":
            print_tasks(tasks)
            id = int(input("Please select a task: "))
            person = input("Please enter the new team members name: ")
            assign_task(tasks,id,person)
            print(f"Task New task assigned to {person}.")
            input("Please press enter to continue...")
        elif user_input == "3":
            print_tasks(tasks)
            id = int(input("Enter task id: "))
            description = complete_task_recursive(tasks,id)
            print(f"Task '{description}' marked as completed.")
            input("Please press enter to continue...")
        elif user_input == "4":
            total_time,total_completed_time = generate_report_recursive(tasks)
            print(f"\n\nThe total time of the project is:{total_time}\nThe remaining time of the tasks to finish the project is:{total_time-total_completed_time}\n")
            input("Please press enter to continue...")
        elif user_input == "5":
            break
        
if __name__ == "__main__":
    main()