import selectionsort
import copy
from selectionsort import data_list

sorted_data = sorted(data_list)
reverse_data = list(reversed(data_list))
duplicate_data = copy.copy(data_list)

def test_unsorted():
    unsorted_list = data_list.copy()
    assert selectionsort.selection_sort(unsorted_list) == sorted_data
    
def test_sorted():
    sorted_list = sorted_data.copy()
    assert selectionsort.selection_sort(sorted_list) == sorted_data
    
def test_reverse():
    reverse_list = reverse_data.copy()
    assert selectionsort.selection_sort(reverse_list) == sorted_data
    
def test_empty():
    empty_list = []
    assert selectionsort.selection_sort(empty_list) == []

def test_duplicate():
    duplicate_list = duplicate_data.copy()
    assert selectionsort.selection_sort(duplicate_list) == sorted_data