#Eric Daily
#Github Username: edaily00
#7/30/2022
#The program generates a graph with the times used for sorting a list with insertion and bubble sort
import time
import random
from functools import wraps
from matplotlib import pyplot

def sort_timer(a_function):
    @wraps(a_function)
    def wrapper_function(*args):
        """This method times the sort method"""
        start_time = time.perf_counter()
        a_function(*args)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        return total_time
    return wrapper_function


@sort_timer
def bubble_sort(a_list):
  """
  Sorts a_list in ascending order
  """
  for pass_num in range(len(a_list) - 1):
    for index in range(len(a_list) - 1 - pass_num):
      if a_list[index] > a_list[index + 1]:
        temp = a_list[index]
        a_list[index] = a_list[index + 1]
        a_list[index + 1] = temp


@sort_timer
def insertion_sort(a_list):
  """
  Sorts a_list in ascending order
  """
  for index in range(1, len(a_list)):
    value = a_list[index]
    pos = index - 1
    while pos >= 0 and a_list[pos] > value:
      a_list[pos + 1] = a_list[pos]
      pos -= 1
    a_list[pos + 1] = value





list1 = [1, 5, 6, 8, 7, 6]


def compare_sorts(bubble, insert):
#Creating empty lists to hold all the data
    list_a = []
    bubble_time = []
    insert_time = []
    x_values = []
#This while loop will go up to 10,000 and take time in 1,000 increments
    x = 1000
    while x <= 10000:
        for i in range(x):
            num = random.randint(1, 10000)
            list_a.append(num)

        list_b = list_a

        bubble_time.append(bubble(list_a))
        insert_time.append(insert(list_b))
        x_values.append(x)
        list_a.clear()
        x += 1000



    pyplot.plot(x_values, bubble_time, 'ro--', linewidth=2, label='Bubble Sort')
    pyplot.plot(x_values, insert_time, 'go--', linewidth=2, label='Insertion Sort')
    pyplot.xlabel("Amount of Numbers Sorted")
    pyplot.ylabel("Time Taken to Sort")
    pyplot.legend(loc='upper left')
    pyplot.show()


compare_sorts(bubble_sort, insertion_sort)
