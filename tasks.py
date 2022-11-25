# Jorge Reyes
# November 15, 2022
# CSS 225
# import random
import random
# import random
item_list = ["pan", "coat", "idea", "rope", "groceries","first aid kit"]
taskList = ["task1", "task2", "task3"]
# create item list and task
# create debuff
debuff_state = ["small"]
your_task = random.choice(taskList)
print(your_task)
# loop with if statements
if your_task == "task1":
    # print("All items are ready")
    if "rope" in item_list and "coat" in item_list and "first aid kit" in item_list:
        print("All items are ready")
        if "small" in debuff_state:
            print("The task’s debuff status has a negative impact on the game character.")
        else:
            print("The games character is not affected by the debuff status")
    else:
        print("Some items are missing")
#         different tasks for differenmt outcomes
elif your_task == "task2":
    # print("All items are ready")
    if "pan" in item_list and "groceries" in item_list:
        print("All items are ready")
        if "slow" in debuff_state:
            print("The task’s debuff status has a negative impact on the game character.")
        else:
            print("The games character is not affected by the debuff status")
    else:
        print("Some items are missing")
elif your_task == "task3":
    # print("All items are ready")
    if "pen" in item_list and "paper" in item_list and "idea" in item_list:
        print("All items are ready")
        if "confusion" in debuff_state:
            print("The task’s debuff status has a negative impact on the game character.")
        else:
            print("The games character is not affected by the debuff status")
    else:
        print("Some items are missing")

# if your_task == "task2":
#     if ""

