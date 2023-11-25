import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd


# style.use("dark_background")

bait = pd.read_csv(r'C:\Users\3iintr00209\Desktop\Bait.csv')

task_durations = bait.groupby('Task')['Task Duration in Minutes'].sum()

# Explode_var = bait.groupby('Task')['Task Duration In Minutes'].sum()
explode = [0] * len(task_durations)  
explode[4] = 0.1

plt.figure(1)
plt.pie(task_durations, labels=task_durations.index, autopct='%1.1f%%', startangle=90 ,explode=explode)
maxval =(max(task_durations))

plt.title('Task Distribution based on Duration')
plt.axis('equal')
plt.show()

# ===============================================Bar ===============================
bait['Date'] = pd.to_datetime(bait['Date'])

# Group by Date and Task and sum the durations
task_duration_pivot = bait.groupby(['Date', 'Task'])['Task Duration in Minutes'].sum().unstack().fillna(0)

plt.figure(2)
task_duration_pivot.plot(kind='bar', stacked=True)
plt.xlabel('Date')
plt.ylabel('Total Time Spent (minutes)')
plt.title('Time Spent on Each Task per Day')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(title='Task', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
