from random import choice
from copy import deepcopy
import math


def contract(vert1, vert2, G):

    """
    Contracts two vertices from a randomly chosen edge in a graph into a single vertices
    vert1 = the first vertex
    vert2 = the second vertex which will contract into vert1
    G = input graph represented by dictionary
    """

    G[vert1].extend(G[vert2])#append the values from vert2 list to the values of vert1
    for adj_vert in G[vert2]: #for every adjacent node of vert2
        lst = G[adj_vert]
        for i in range(0, len(lst)): #scan its list and replace vert2 with vert1 
            if lst[i] == vert2:
                lst[i] = vert1

    while vert1 in G[vert1]: #remove self-loops in vert1

        G[vert1].remove(vert1)

    del G[vert2] #remove vert2 and its list from graph

def findMinCut(G):
    """
    Find the minimum cut in graph G using Kargers algorithm
    G = dictionary to represent a graph
    key: vertex, values = adjacent vertices
    """

    while len(G) > 2: #while there are more than two vertices in G
        vert1 = choice(list(G.keys())) #choose a random vertex and set its value to vert1
        vert2 = choice(G[vert1]) #from the list of vertices, choose another random vertex and set it to vert2
        contract(vert1, vert2, G)#contract along that edge, contract vert2 into vert1
    return len(G.popitem()[1])#pop one of the two remaining elements and take its length. This will be the min cut
def main():

    """
    Find min cut in graph G using Kargers Min Cut algorithm.
    We will conduct repeated trials in order to increase our probability
    of finding the min cut. After n*n*logn repated trials
    our probability of failure is reduced to 1/n
    """

    f = open('kargerMinCut.txt', 'r')
    line_list = f.readlines()
    #Use a dictionary to represent the graph
    G = {int(line.split()[0]): [int(val) for val in line.split()[1:] if val] for line in line_list if line}

    mincut = float("inf")

    n = 200*200*math.log(200)
    for _ in range(int(n)):
        current = findMinCut(deepcopy(G))
        if current < mincut:
            mincut = current

    print("The min cut is:", mincut)

if __name__ == '__main__':
    main()

