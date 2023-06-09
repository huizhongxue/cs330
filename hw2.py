"""
Consider the Car manufacturing problem with N steps as defined in the PDF of hw2.
Assume that each step takes one hour. Knowing which steps depend on which, write a program
that calculates how many hours it will take to manufacture a car.

!!!!!!!!!!!!!!!!!!!! DO NOT IMPORT PYTHON LIBRARIES TO SOLVE THE PROBLEM !!!!!!!!!!!!!!!!!!!!

Input:
The input is given as a LIST of N SETS.
For i = 0 .... N-1,
the ith set is a set of indices (from 0 to N-1) of steps that step i depend on.
If ith step does not depend on any other step, the ith set is empty.

Output
Return the total time, in hours, it will take to manufacture
a car. If it is impossible to manufacture it, return -1.

Sample Test Case 1

task_dependencies_list1 = [{1}, {0}]
find_hours_needed(task_dependencies_list1) SHOULD return -1
In this test case, steps with indices 0 and 1 have 1 dependency each. Step 0 depends on step 1 and step 1
depends on step 0, therefore, it is impossible to manufacture a car.

Sample Test Case 2
task_dependencies_list2 = [{}, {2}, {}]
find_hours_needed(task_dependencies_list2) SHOULD return 2
hour 1: execute steps at indices 0 and 2
hour 2: execute step at index 1


Sample Test Case 3
task_dependencies_list3 = [{1, 2}, {}, {}, {0}, {0}]
find_hours_needed(task_dependencies_list3) #should return 3
hour 1: execute steps 1, 2
hour 2: execute step 0
hour 3: execute steps 3, 4

"""


""" Finds the number of hours needed to manufacture a care given dependency information if possible.
Parameters
----------
task_dependencies_list: LIST of N SETS
    For i = 0 .... N-1,
        the ith set is a set of indices (from 0 to N-1) of steps that step i depend on.
        If ith step does not depend on any other step, the ith set is empty.
Returns
-------
the total time, in hours, it will take to manufacture
a car. If it is impossible to manufacture it, return -1.
"""
def find_hours_needed(task_dependencies_list):
    N = len(task_dependencies_list)
    hours_needed = 0
    visited = []
    current = []

    if N == 0: return 0
    for i in range(0, N, 1):
        if not task_dependencies_list[i]: 
            current.append(i)
            visited.append(i)
    if not visited: return -1
    hours_needed = hours_needed + 1

    while current:
        current = []
        for i in range(0, N, 1):
            if i not in visited: 
                if task_dependencies_list[i].issubset(visited):
                    current.append(i)
        if current: 
            hours_needed = hours_needed + 1
            visited.extend(current)

    return hours_needed



#sample test cases

#sample test case 1
#task_dependencies_list1 = [{1}, {0}]
#find_hours_needed(task_dependencies_list1) #should return -1
"""
In this test case, steps with indices 0 and 1 have 1 dependency each. Step 0 depends on step 1 and step 1
depends on step 0, therefore, it is impossible to manufacture a car.
"""

#sample test case 2
#task_dependencies_list2 = [{}, {2}, {}]
#find_hours_needed(task_dependencies_list2) #should return 2
"""
should return 2
hour 1: execute steps at indices 0 and 2
hour 2: execute step at index 1
"""

#sample test case 3
#task_dependencies_list3 = [{1, 2}, {}, {}, {0}, {0}]
#find_hours_needed(task_dependencies_list3) #should return 3
"""
hour 1: execute steps 1, 2
hour 2: execute step 0
hour 3: execute steps 3, 4
"""
