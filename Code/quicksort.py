import pandas as pd

# Read CSV file function
def read_excel(filepath, columns):
    dataframe = pd.read_excel(filepath, usecols=columns)
    return dataframe

# Quick Sort
def quick_sort(sequence):
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence[len(sequence) // 2]

    items_greater = [item for item in sequence if item > pivot]
    items_lower = [item for item in sequence if item < pivot]
    items_equal = [item for item in sequence if item == pivot]

    return quick_sort(items_lower) + items_equal + quick_sort(items_greater)


# Column names you want to read from the CSV file
columns = [0, 5]

# Escaping the backslashes
filepath = 'D:\Advanced_Programming_Part_A\BirthWeight.xlsx'

# Read the specified columns from the CSV file into a DataFrame
dataframe = read_excel(filepath, columns)

# Print the original Excel Data:
print("Excel Data: ")
print(dataframe)
print("")

# Defining Column
column = "BirthWeight"

# Convert DataFrame column to a list
data_list = dataframe[column].tolist()

# Applying quick sort and printing sorted data
data_list = quick_sort(data_list)
sorted_data = pd.DataFrame(data_list, columns=[column])
print("Quick Sorted Data: ")
print(sorted_data)