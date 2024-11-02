Original file is located at
    https://colab.research.google.com/drive/15qRM9sMuqS0QostsefKfWrJCW3eLBBfE

TASK 1
"""

import matplotlib.pyplot as plt

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time, revenue, label='Revenue')
plt.plot(time, costs, label='Costs')

plt.xlabel('Time')
plt.ylabel('Amount')
plt.title('Revenue and Costs over Time')
plt.legend()

plt.show()

"""Task 2"""

import matplotlib.pyplot as plt

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time, revenue, color='purple', linestyle='--', label='Revenue')
plt.plot(time, costs, color='#82edc9', marker='s', label='Costs')

plt.xlabel('Time')
plt.ylabel('Amount')
plt.title('Revenue and Costs over Time')
plt.legend()

plt.show()

"""Task 3"""

import matplotlib.pyplot as plt

time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
spending_on_coffee = [3000, 2950, 2980, 3050, 3100, 3000, 3020, 3080, 3060, 3030, 3005, 3080]

plt.plot(time, spending_on_coffee, color='purple', linestyle='--', label='Spending on Coffee')

plt.xlabel('Years')
plt.ylabel('Spending ($)')

plt.title('Coffee Spending Over 12 Years')
plt.legend()

plt.axis([0, 12, 2900, 3100])

plt.show()

"""Task 4"""

from matplotlib import pyplot as plt

x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]

plt.plot(x, y, color='purple', linestyle='--', label='Spending on Coffee')

plt.xlabel('Time')
plt.ylabel('Dollars spent on coffee')

plt.title('My Last Twelve Years of Coffee Drinking')
plt.legend()

plt.show()

"""Task 5"""

import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
temperature = [30, 32, 35, 40, 45, 50]
flights_to_hawaii = [120, 130, 150, 180, 200, 250]

plt.subplot(1, 2, 1)
plt.plot(months, temperature, 'o-', color='blue')
plt.xlabel('Months')
plt.ylabel('Temperature (F)')
plt.title('Temperature vs Months')

plt.subplot(1, 2, 2)
plt.plot(temperature, flights_to_hawaii, 'o-', color='green')
plt.xlabel('Temperature (F)')
plt.ylabel('Flights to Hawaii')
plt.title('Flights to Hawaii vs Temperature')

plt.tight_layout()

plt.show()

"""Task 6"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
straight_line = x
parabola = x**2
cubic = x**3

plt.figure(figsize=(8, 6))

plt.subplot(2, 1, 1)
plt.plot(x, straight_line)

plt.subplot(2, 2, 3)
plt.plot(x, parabola)

plt.subplot(2, 2, 4)
plt.plot(x, cubic)

plt.subplots_adjust(hspace=0.35, bottom=0.2)

plt.show()

"""Task 6-02"""

import matplotlib.pyplot as plt

hyrule = [75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130]
kakariko = [70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
gerudo = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135]

legend_labels = ["Hyrule", "Kakariko", "Gerudo Valley"]

plt.plot(hyrule, label=legend_labels[0])
plt.plot(kakariko, label=legend_labels[1])
plt.plot(gerudo, label=legend_labels[2])

plt.legend(loc='lower center')
plt.xlabel('Months')
plt.ylabel('Temperature (F)')
plt.title('Temperature Over the Past Year')

plt.show()

"""Task 7"""

import matplotlib.pyplot as plt

months = range(1, 13)
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
subscription_proportion = [0.12, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.6, 0.7, 0.75]

fig, ax = plt.subplots()
ax.plot(months, subscription_proportion)

ax.set_xticks(months)
ax.set_xticklabels(month_names)

ax.set_yticks([0.10, 0.25, 0.5, 0.75])
ax.set_yticklabels(['10%', '25%', '50%', '75%'])

ax.set_xlabel('Months')
ax.set_ylabel('Subscription Proportion')
ax.set_title('Dinnersaur Subscription Over the Year')

plt.show()

"""Task 8"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 15, 20, 18, 25]
y2 = [5, 8, 12, 10, 15]

plt.plot(x, y1, 'o-', color='pink', label='Metric 1')
plt.plot(x, y2, 'o-', color='gray', label='Metric 2')

plt.title('Two Lines on One Graph')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')

plt.legend(loc='lower right')

plt.show()

"""Task 9"""

import matplotlib.pyplot as plt

drink_categories = ['Cappuccino', 'Latte', 'Espresso', 'Macchiato', 'Mocha']
drink_sales = [120, 150, 90, 80, 110]

plt.bar(range(len(drink_categories)), drink_sales)

plt.xlabel('Drink Categories')
plt.ylabel('Number of Drinks Sold')
plt.title('Monthly Sales by Drink Category')

plt.show()

"""Task 9"""

import numpy as np
import pandas as pd

gradebook = pd.read_csv('your_gradebook.csv')

print(gradebook)

assignment1 = gradebook[gradebook['assignment_name'] == 'Assignment 1']
print(assignment1)

asn1_median = np.median(assignment1['grade'])
print('Median grade on Assignment 1:', asn1_median)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('your_survey_data.csv')

print(df)

sns.barplot(data=df, x='Gender', y='Response', estimator=len)
plt.show()

sns.barplot(data=df, x='Gender', y='Response', estimator=np.median)
plt.show()
