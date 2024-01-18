# import pandas as pd
# import matplotlib.pyplot as md


# # md.style.use('dark_background')
# # Reading a csv local
# file = pd.read_csv('jan 1_15.csv')
# # Getting emp id from user
# empcode = input("Enter the employee code : ")
# # converting csv empid as upper and store it in empid array
# file['EmployeeID'] = file['EmployeeID'].str.upper()
# # convert input as upper also
# empcode == empcode.upper()
# # cross check a user inp = csv
# empdata = file[file['EmployeeID'] == empcode]
# # groupby using 1003820('taskname')    for that emp code it will get sum task's
# task_durations = empdata.groupby('TaskName')['TaskDuration'].sum()
# # my referencees
# print(task_durations/60)
# print(task_durations.index)
# print(f"Task durations for Employee {empcode}:\n{task_durations}")
# # plotting use time and task
#     # md.bar(task_durations.index,task_durations , color="#073259",width=0.3 )
# md.barh(task_durations.index,task_durations/60 , color="#073259")
# # xaxis label
# md.xlabel('Task Duration' , fontweight='bold', color='Green')
# # md.ylabel('Task Duration', fontweight='bold', color='Green')

# md.xticks(fontsize=8 )
# md.yticks(fontsize=8)
# # giving a emp code titles
# md.title(f'Task Durations for Employee {empcode}')
# md.spines['left'].set_position(('outward', 40)) 
# md.show()


import pandas as pd
import matplotlib.pyplot as plt

# Reading a csv local
file = pd.read_csv('jan 1_15.csv')

# Getting emp id from user
empcode = input("Enter the employee code: ")

# Converting csv empid as upper and store it in empid array
file['EmployeeID'] = file['EmployeeID'].str.upper()

# Convert input as upper also
empcode = empcode.upper()

# Cross-check a user input with csv
empdata = file[file['EmployeeID'] == empcode]

# Groupby using 1003820('taskname') for that emp code to get sum task's
task_durations = empdata.groupby('TaskName')['TaskDuration'].sum()

# Convert task durations from seconds to minutes
task_durations_minutes = task_durations / 60

# Plotting task durations using time and task
fig, ax = plt.subplots()

# Horizontal bar plot
ax.barh(task_durations.index, task_durations_minutes, color="#073259")

# Setting the x-axis label
ax.set_xlabel('Task Duration (hours)', fontweight='bold', color='Green')

# Tick configurations for the x-axis
ax.tick_params(axis='x', labelcolor='green', labelsize=8)

# Adjust the position of the y-axis
ax.spines['left'].set_position(('outward', 40))  # Change the value 40 as needed

# Giving an employee code title
plt.title(f'Task Durations for Employee {empcode}')

plt.show()
