# Import `os`
import os
import pandas as pd
import xlrd


# Retrieve current working directory (`cwd`)
cwd = os.getcwd()


# Change directory
os.chdir("C:/Users/kndlovu/Desktop/Excel Documents")

# List all files and directories in current directory
#print(os.listdir('.'))
# Assign spreadsheet filename to `file`
file = 'Site_list.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('All Sites')
