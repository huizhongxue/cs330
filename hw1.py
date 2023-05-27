"""
Problem Statement (available also in PDF):
At Boston University, the lecture recess is the most awaited time by most students.
Not just because the classes sometimes are tiring, but because the Dining Service is very good.
When the morning lectures end, all the students run from their classes to arrive
as early as possible at the nearest dining location. Tiago noticed that there was an opportunity there.
Using a reward system, Tiago decided that the order in which the students would be
served would not be given by the arrival time, but by the sum of grades obtained in CS330.
In this way, those with higher grades can be served before those with lower grades.
Your task is simple: given the arrival time of the students, and their respective grades in the CS330,
write an efficient program to reorder the queue according to their grades, and say how many students DO NOT need to change place in this reordering.

!!!!!!!!!!!!!!!!!!!! DO NOT USE PYTHON STANDARD LIBRARIES TO SORT THE INPUT !!!!!!!!!!!!!!!!!!!!

@@@@@@@@@@@ INPUT:

Your code will be run for several test cases. Each test case starts with an integer M (1 <= M <= 1000), indicating the number of students.
Following, there will be M distinct integers P[i] (1 <= P[i] <= 1000)$, where the i-th integer indicates the grade of the i-th student.

The above integers are given in the arrival order, or in other words,
the first integer is from the first student to get to the queue, the second integer is from the second student, and so on.
@@@@@@@@@@@ OUTPUT:
For each test case return the number of students that don't need to change their places even after the queue being reordered.

@@@@@@@@@@@ Test Case 1:

INPUT:
3
100 80 90
OUTPUT:
1

@@@@@@@@@@@ Test Case 2:

INPUT:
4
100 120 30 50

OUTPUT:
0


@@@@@@@@@@@ Test Case 3:

INPUT:
4
100 90 30 25

OUTPUT:
4
"""


"""
=========================================================================================
=========== you do not have to use this sorting function but it canhelp you ===========
=========================================================================================
"""

"""Sorts an array of integers
Parameters
----------
array: array to be sorted
does not return anything but sorts the given array
"""
def sort(array):
    #Hint: you can implement the insertion sort from hw0
    #Hint: test your sorting function before calling it from the homework function


"""
=========================================================================================
=========== you have to implement this function to be graded by autograder ===========
=========================================================================================
"""


"""Counts the number of students who DO NOT need to change their places to reorder the students.

Parameters
----------
m : the number of students
grades : array of m integers containing the grades of the students
Returns
-------
the number of students who DO NOT need to change their places to reorder the students.
"""
def count_students_already_in_place(m, grades):
    #the function .copy() performs a deep copy of the array
    grades_before_sorting = grades.copy()
    counter = 0
    """
        Insert your code here. You are also free to edit the above two lines,
        but you must keep the function signature as is.
    """
    return counter
