#Import the Pandas module
import pandas as pd

#Set Pandas settings to see all rows and columns of dataFrame
pd.set_option("display.max_rows", None, "display.max_columns", None)

#Read the Excel file using pandas and Normalize the date columns in the standard date format
emp_df = pd.read_excel('C:\krunal.maniar\Python\employee__1_.xls',parse_dates=['Date of Birth', 'Date of Joining'])
emp_df.head()

#Sort the data in ascending order based on Date of Birth
sorteddataFrame = emp_df.sort_values('Date of Birth') 

#Group the data based on Quarter of Joining and Prepare a dictionary with key as Quarter an value as list of First Employee name
groupedbyQuarterofJoining = sorteddataFrame.groupby('Quarter of Joining')['First Name'].apply(lambda g: g.values.tolist()).to_dict()
