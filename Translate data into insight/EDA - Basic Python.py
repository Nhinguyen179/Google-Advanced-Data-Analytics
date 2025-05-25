import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Task 1: Set your folder path
file_directory = r'C:\Users\Nhi\Desktop\Coursera\EDA\\'
#Task 2: Read the file
file_name = 'eda_using_basic_data_functions_in_python_dataset1.csv'
df = pd.read_csv(file_directory + file_name)
#Task 3: Discover at a high level
print(df.head(10))
df.info()
print(df.describe())
#4 Convert data into datatime
df['date'] = pd.to_datetime(df['date'])
print(df.head(10))
#Task 4:Calculate the date the the most strikes
##Method 1: pivot table
pivot = pd.pivot_table(df,
                        index = 'date',
                        values = 'number_of_strikes',
                        aggfunc = 'sum'
                        )
sorted_pivot = pivot.sort_values(by=['number_of_strikes'],ascending=True)

##Method 2: group by
sorted_table = df.groupby(['date']).sum().sort_values('number_of_strikes',ascending=False).head(10)

#Task 5: Extract the month and add it into a new column using dt.month_name()
df['month'] = df['date'].dt.month_name().str.slice(stop=3)
#Task 6: Create a new df to plot no of strikes per month as a bar graph
df_by_month = df.groupby(['month']).sum('number_of_strikes').reset_index()
#use reset.index() to refer to 'month' column name

#Task 7: Bar chart
plt.bar(x=df_by_month['month'],height=df_by_month['number_of_strikes'],label='Number of strikes per month',color='green')
plt.xlabel('Month')
plt.ylabel('Number of strikes')
plt.title('Number of strikes per month')
plt.show()
