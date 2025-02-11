import matplotlib.pyplot as plt
import pandas as pd

# Data as an array of dictionaries
fc_porto_stats = [
    {'year': 2000, 'points': 76, 'games': 30},
    {'year': 2001, 'points': 68, 'games': 30},
    {'year': 2002, 'points': 82, 'games': 30},
    {'year': 2003, 'points': 82, 'games': 30},
    {'year': 2004, 'points': 62, 'games': 30},
    {'year': 2005, 'points': 79, 'games': 30},
    {'year': 2006, 'points': 69, 'games': 30},
    {'year': 2007, 'points': 75, 'games': 30},
    {'year': 2008, 'points': 70, 'games': 30},
    {'year': 2009, 'points': 68, 'games': 30},
    {'year': 2010, 'points': 84, 'games': 30},
    {'year': 2011, 'points': 75, 'games': 30},
    {'year': 2012, 'points': 78, 'games': 30},
    {'year': 2013, 'points': 61, 'games': 30},
    {'year': 2014, 'points': 82, 'games': 34},
    {'year': 2015, 'points': 73, 'games': 34},
    {'year': 2016, 'points': 76, 'games': 34},
    {'year': 2017, 'points': 88, 'games': 34},
    {'year': 2018, 'points': 85, 'games': 34},
    {'year': 2019, 'points': 82, 'games': 34},
    {'year': 2020, 'points': 80, 'games': 34},
    {'year': 2021, 'points': 91, 'games': 34},
    {'year': 2022, 'points': 85, 'games': 34},
    {'year': 2023, 'points': 59, 'games': 29}
]

# Convert list of dictionaries to DataFrame
df = pd.DataFrame(fc_porto_stats)

# Calculate the percentage of points
df['percentage_of_points'] = (df['points'] / (df['games'] * 3)) * 100

# Plotting the data
plt.figure(figsize=(10, 5))

# Set colors based on conditions
colors = ['red' if x < 75 else 'green' if x > 85 else 'black' for x in df['percentage_of_points']]

# Plot with colored points and connect them with a line
plt.plot(df['year'], df['percentage_of_points'], marker='p', linestyle='-', color='#00000020')  # Re-added line
for (x, y, color) in zip(df['year'], df['percentage_of_points'], colors):
    plt.scatter(x, y, color=color)
    plt.text(x, y + 0.5, f'{y:.1f}%', ha='center', fontsize=8)  # Smaller font, 1 decimal place

plt.title('Percentage of Points Scored by FC Porto Per Season')
plt.xlabel('Year')
plt.ylabel('Percentage of Points (%)')
plt.grid(True, color='lightgray', alpha=0.5)  # Lighter grid lines
plt.xticks(df['year'])  # Ensure all years are shown as x-ticks
plt.yticks(range(60, 100, 2))  # Setting y-ticks to increment by 5%
plt.show()
