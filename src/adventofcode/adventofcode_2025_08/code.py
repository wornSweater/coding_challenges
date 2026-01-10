def read_file(filename):
    import os
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)

    boxes = []

    with open(filepath, 'r') as file:
        for line in file.readlines():
            boxes.append(tuple(line.strip().split(",")))
    
    return boxes

def cal_distance(x, y):
    return (int(x[0]) - int(y[0]))**2 + (int(x[1]) - int(y[1]))**2 + (int(x[2]) - int(y[2]))**2

def solve_1(boxes, edges=1000):

    ##########################################################
    # Graph theorey, a root to represent a whole tree or block
    ##########################################################
    
    # calculate all distances
    # create the dict to store the nodes and parents and size
    # define fn to find the root
    parent = {}
    size = {}

    def find_root(x):

        while x != parent[x]:
            x= parent[x]

        return x

    distances = []
    
    for i in range(len(boxes)):
        parent[boxes[i]] = boxes[i] # without connnecting, every node is the root
        size[boxes[i]] = 1

        for j in range(i + 1, len(boxes)):
            
            distances.append([cal_distance(boxes[i], boxes[j]), boxes[i], boxes[j]])
    
    distances = sorted(distances, key=lambda x: x[0])

    distances = distances[:edges]

    # update the size and parents
    for dis in distances:

        # if roots are different
        root1 = find_root(dis[1])
        root2 = find_root(dis[2])
        
        if root1 != root2:
            parent[root1] = root2
            size[root2] += size[root1]
            size[root1] = 0
        
    sorted_size = sorted([v for k, v in size.items()], reverse=True)

    return sorted_size[0] * sorted_size[1] * sorted_size[2]



def solve_2(boxes, N=999):

    #############################################################################################################
    # Graph theorey, true connection: in the spinning tree, #Edeges = # Nodes - 1
    # true connection and pseudo connection, we can ignore all the circles and only focus on spinning tree edges
    #############################################################################################################
    
    # calculate all distances
    # create the dict to store the nodes and parents and size
    # define fn to find the root
    parent = {}
    size = {}

    def find_root(x):

        while x != parent[x]:
            x= parent[x]

        return x

    distances = []
    
    for i in range(len(boxes)):
        parent[boxes[i]] = boxes[i] # without connnecting, every node is the root
        size[boxes[i]] = 1

        for j in range(i + 1, len(boxes)):
            
            distances.append([cal_distance(boxes[i], boxes[j]), boxes[i], boxes[j]])
    
    distances = sorted(distances, key=lambda x: x[0])

    ans = 0
    # update the size and parents
    for dis in distances:
            
        if N > 0:

            # if roots are different
            root1 = find_root(dis[1])
            root2 = find_root(dis[2])
            
            if root1 != root2:
                parent[root1] = root2
                size[root2] += size[root1]
                size[root1] = 0
                N -= 1
                ans = int(dis[1][0]) * int(dis[2][0])
        
        else:
            return ans
    
    return -1

if __name__ == "__main__":
    print(solve_2(read_file("input.txt")))

    

