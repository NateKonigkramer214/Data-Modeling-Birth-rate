import pandas as pd

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n -i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr 


def read_excel(filepath, columns):
    dataframe = pd.read_excel(filepath, usecols=columns)
    return dataframe


columns = [0,5]

filepath = 'D:\Advanced_Programming_Part_A\BirthWeight.xlsx'

dataframe = read_excel(filepath, columns)

print("Excel Data: ")
print(dataframe)
print("")

column = "BirthWeight"
data_list = dataframe[column].tolist()

print(" ")
#print(data_list)
print(" ")

bubble_sort(data_list)

sorted_dataframe = pd.DataFrame(data_list)
print("Bubble Sorted Data:")
print(sorted_dataframe)