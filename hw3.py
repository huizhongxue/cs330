import sys
import datetime


"""
Tiago is a dedicated student of comedy. He doesn't like to be late in any way
and always tries to arrive no later than 6:00 pm, which is the start time of comedy class.
Tiago leaves the CDS building at 5:00 pm, and it takes walk_time_to_station minutes
for him to get to the bus stop from his office.
Buses leave from the nearest station to the office
only once at 5:30 and another time at 5:50 PM.
Tiago needs to know when he will arrive at the comedy center by choosing the best route and if he will be late.

Your task is, considering N possible bus connections,
to determine at what time Tiago will arrive at the comedy center taking the fastest route.
His trip starts by a walk from the office to the bus stop.
Then, he takes bus trip starting from the `cds' station at either 5:30 or 5:50.
Assume no walk time between connecting trips.
Note that the time T from station A to station B is not the same as from station B to station A because traffic in the opposite direction may be different.
Assume that Tiago will always reach the bus stop at most 5:50 and that there will always be a route between CDS to the comedy center.

INPUT:
    integer value indicating Tiago's walking time from the office to the station, and
    adjacency list of the graph representing the directed bus connections and time for each connection

OUTPUT:
    Your function should output a pair of string and boolean values.
    The string should be the arrival time at the comedy center in the format HH:MM.
    The boolean value should be True iff Tiago will be late.
"""

#!!!!!!!!You are allowed to import and use datetime Python library!!!!!!!!!

#Test Case 1:
"""
walk_time_to_station = 35
{
'cds': {'harvard': 5, 'comedycenter': 25},
'harvard': {'airport': 5},
'airport': {'comedycenter': 5},
'comedycenter': {}
}

OUTPUT:
(18:05, True)
"""

#Test Case 2:
"""
walk_time_to_station = 15
{
'cds': {'harvard': 10, 'comedycenter': 30},
'harvard': {'airport': 15},
'airport': {'comedycenter': 10},
'comedycenter': {}
}

OUTPUT:
(18:00, False)
"""


"""
This is the function that will be autograded. It computes Tiago's arrival time and whether he will be late.
Parameters:
walk_time_to_station: time Tiago takes to walk from CDS building to CDS station
adj_list: adjacency list of all bus connections
Returns:
pair of values indicating arrival time (HH:MM format) and whether Tiago is late
"""
def compute_arrival_time(walk_time_to_station, adj_list):
    #run shortest path algorithm
    #You do not have to implement this function, but it is encouraged.
    shortest_distances = compute_shortest_distances_with_dijkstra(adj_list, 'cds')
    #look up shortest distance to comedycenter
    time_to_comedy_center = shortest_distances['comedycenter']
    """
    Your code here ....
    these are the variables to be returned
    arrival_time_at_comedycenter_str = ... #string in format HH:MM
    is_late = ... #boolean variable
    """
    return (arrival_time_at_comedycenter_str, is_late)


"""
Compute shortest distances from a starting node in directed graph.
You do not have to implement this function, but it is encouraged.
Parameters:
adj_list: adjacency list of the graph
start: starting vertex
Returns:
table of the shortest paths of all nodes in the graph
"""
def compute_shortest_distances_with_dijkstra(adj_list, start):
    num_vertices = len(adj_list)
    #assign infinity distance to all vertices
    distances = {vertex: sys.maxsize for vertex in adj_list}
    #except for start vertex, assign 0 to it
    distances[start] = 0

    """
    Your code here....
    """

    return distances

def UpdateGraphAndDegrees(adjacency_list):
    indegree = []
    removed = []

    for i in range(0, len(adjacency_list), 1):
        indegree.append(len(adjacency_list[i]))
        if len(adjacency_list[i]) == 0: 
            removed.append(i)
    
    for edge_list in adjacency_list:
        if len(edge_list) == 0:
            adjacency_list.remove(edge_list)
        else: 
            for node in edge_list:
                if node in removed:
                    edge_list.remove(node)

    return indegree
    return adjacency_list