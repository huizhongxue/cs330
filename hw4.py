"""
Thanks to your great solution to Homework 3, Tiago finished the comedy course with honors.

Besides being a lecturer at BU, he now has a second job at GIGGLE (GIGGLE - Gigglesome Institute Generating Genuine Laughter and Entertainment).

His first job is to make BU students laugh more.
To do this, he plans to install Joke Teller Machines (JTM) along Commonwealth Avenue.
He has a list of potential points where the JTMs can be installed.
Each JTMs has an associated joke energy (to understand this, please watch Monsters, Inc.).
It is well known that the distance between two JTMs cannot be less than k, otherwise, students will not laugh.

Given the list of points and their joke energy, your task is
to help Tiago choose the points to install the JTMs in a way that maximizes the sum of joke energy.
Output the selected points and the maximum sum of joke energy!

!!!!!!!!!!!!!!!!!!!! DO NOT IMPORT PYTHON LIBRARIES TO SOLVE THE PROBLEM !!!!!!!!!!!!!!!!!!!!

For example, consider JTMs at positions 1, 2, and 3, with joke energy of 2, 5, and 3, respectively.
If k equals 2, an optimal solution would be to choose the JTMs at positions 1 and 3, resulting in a total joke energy of 5.

Input:

The input is:
    n = integer value indicating the number of points available to install a JTM
    k = integer value indicating the minimum distance required between two JTMs
    points = a list of integer points where JTM can be installed
    energy = a list of integers indicating the joke energy that is produced at each point

Output:

Your function should output an integer: the maximum joke energy.

Sample Test case 1
n = 13
k = 7
points = [2, 7, 12, 13, 18, 23, 24, 25, 30, 33, 38, 41, 43]
energy = [6, 6,  7,  9, 10,  6,  2,  6,  4,  6,  3,  9,  9]

OUTPUT:
37
by selecting: [2, 18, 25, 33, 41]

Sample Test Case 2

n = 17
k = 18
points = [4, 8, 9, 10, 13, 16, 17, 21, 23, 25, 28, 32, 35, 36, 39, 41, 44]
energy = [1, 1, 5,  2, 10,  4,  9,  1,  2,  4,  5,  2,  5,  7,  3,  4,  2]

OUTPUT:
17
by selecting: [13, 36]
"""


"""
Computes maximum energy
Parameters:
    n = integer value indicating the number of points available to install a JTM
    k = integer value indicating the minimum distance required between two JTMs
    points = a list of integer points where JTM can be installed
    energy = a list of integers indicating the joke energy that is produced at each point
Returns:
s: maximum joke energy
"""
def max_energy(points, energy, k, n):

    if n == 1: return energy[0]
    max = [0] * (n-1)
    max.append(energy[n-1])

    for i in range(n-2, -1, -1):
        j = i + 1
        while j < n and points[j] - points[i] < k:
            j = j + 1
        if j >= n: 
            if points[n-1] - points[i] < k:
                if energy[i] > max[i+1]:
                    max[i] = energy[i]
                else:
                    max[i] = max[i+1]
        else:
            if max[i+1] > energy[i] + max[j]:
                max[i] = max[i+1]
            else:
                max[i] =  energy[i] + max[j]

    return max[0]