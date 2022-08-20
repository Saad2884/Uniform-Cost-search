graph = {
  'S' : [('A',2),('B',5)],
  'A' : [('C',2),('D',4)],
  'B' : [('G',5)],
  'C' : [('D',3)],
  'D' : [('G',2)],
  'G' : []
}

def ucs(G, start, goal):

    # Initialize empty queue
    queue = []
    
    # Add start node to queue with cost 0
    queue.append(([start], 0))

    print('-----------------------')
    print('Starting state of queue')
    print('-----------------------')
    print(queue)
    print('-----------------------')
    print() 

    iter = 0

    minIndex = 0

    # Repeat until queue is empty
    while queue :
        iter = iter + 1
        
        # Pop the path from queue with minimum cost
        currentPath = queue.pop(minIndex)

        # If current path is goal, solution found, stop the while loop
        if currentPath[0][0] == goal:
            break

        # For current path access each child node from graph
        for child in graph[currentPath[0][0]]:
            childNode = child[0]
            childCost = child[1]
                    
            newPath = currentPath[0].copy()
            newPath.insert(0, childNode)
            newCost = currentPath[1] + childCost

            # Add new path to the queue
            queue.append((newPath, newCost))

        print('-----------------------')
        print('Queue after iteration {}:'.format(iter))
        print('-----------------------')
        print(queue)
        print('-----------------------')
        print() 

        # Find path with minimum cost
        minIndex = 0
        minCost = queue[minIndex][1]

        for i in range(1, len(queue)):
            if queue[i][1] < minCost:
                minIndex = i
                minCost = queue[i][1]

        
    print('-----------------------')
    print('Minimum path:')
    print('-----------------------')
    print(currentPath)
    print('-----------------------')


ucs(graph, 'S', 'G')