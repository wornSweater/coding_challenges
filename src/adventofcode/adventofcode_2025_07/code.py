def read_file(filename):

    import os
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)

    space = []

    with open(filepath, 'r') as file:
        for line in file.readlines():
            line_list = []
            for obj in line.strip():
                line_list.append(obj)
            space.append(line_list)
            
    return space

def vis_space(space):
    for line in space:
        print("".join(line) + "\n")

def solve_1(space):
    #####################################################################################
    # cannot combine ^ and | together as one situation, | may already exist for next line
    # be careful to make every case clear
    #####################################################################################

    for j in range(len(space[0])):
        if space[0][j] == "S":
            space[0][j] = "|"
    
    ans = 0

    for i in range(len(space) - 1):
        for j in range(len(space[0])):
            
            # if this is the beam
            if space[i][j] == "|":
                # if the next line is "."
                if space[i+1][j] == ".":
                    space[i+1][j] = "|"

                # if the next is a spliter
                elif space[i+1][j] == "^":
                    ans += 1
                    # consider the bounds
                    if j == 0:
                        space[i+1][j+1] = "|"
                    elif j == len(space[0]) - 1:
                        space[i+1][j-1] = "|"
                    else:
                        space[i+1][j+1] = "|"
                        space[i+1][j-1] = "|"
                
                # if next is a beam

    return ans, space

def solve_2(space):

    # determine the location and children (index, index): []
    # assume the middle line is only for light transmission

    # set the dict to store all the points:
    tree = {}

    for i in range(0, len(space) - 2, 2):

        for j in range(len(space[0])):

            if space[i][j] == "|": # if this is the light source

                tree[(i, j)] = []

                # iterate to find if there is spliter
                for k in range(i + 1, len(space)):

                    if space[k][j] == "^":
                        if j == 0:
                            tree[(i, j)] = [(k, j + 1)]
                            tree[(k, j + 1)] = []
                        elif j == len(space[0]) - 1:
                            tree[(i, j)] = [(k, j - 1)]
                            tree[(k, j - 1)] = []
                        else:
                            tree[(i, j)] = [(k, j + 1), (k, j - 1)]
                            tree[(k, j + 1)] = []
                            tree[(k, j - 1)] = []

                        break # has to break avoiding penetrating the spliter

                    # if there is no spliter, we already keep the children list empty

    # if multiple sources, we just sum them all, but just assume there is only one light source

    start = (0, 0)

    # queue = []
    # print(tree)

    for j in range(len(space[0])):
        if space[0][j] == "|":
            start = (0, j)

    # queue.append(start)

    # while queue:

    #     removed = queue.pop()
    #     if tree[(removed)]:
    #         for child in tree[(removed)]:
    #             queue.append(child)

    #     else:
    #         ans += 1

    # return ans

    #########################################
    # BFS not good, enumerate all the paths, the total is 171692855075500
    # dynammic programming is the best
    #########################################

    for i in range(len(space) - 1, -1, -1):
        for j in range(len(space[0])):
            if (i, j) in tree:
                if not tree[(i, j)]:
                    tree[(i, j)] = [[], 1]
                else:
                    tree[(i, j)] = [tree[i, j], sum(tree[child][1] for child in tree[(i, j)])]

    print(tree)
    
    return tree[start][1]

visited = {}

# def solve_2_new(x, y, space):
    
#     # recursion

#     if (x, y) in visited:
#         return visited[(x, y)]
    
#     else:
    
#     # if we dive some lines, and encouter the first spliter
#         for i in range(2, len(space) - x, 2):
#             if space[x + i][y] == "^":
#                 if (x + i, y - 1) in visited and (x + i, y + 1) in visited:
#                     return visited[(x + i, y - 1)] + visited[(x + i, y + 1)]
#                 elif (x + i, y - 1) in visited and (x + i, y + 1) not in visited:
#                     return visited[(x + i, y - 1)] + solve_2_new(x + i, y + 1, space)
#                 elif (x + i, y - 1) not in visited and (x + i, y + 1) in visited:
#                     return solve_2_new(x + i, y - 1, space) + visited[(x + i, y + 1)]
#                 else:
#                     return solve_2_new(x + i, y - 1, space) + solve_2_new(x + i, y + 1, space)
#             else:
#                 continue

#         visited[(x, y)] = 1

#         return 1

if __name__ == "__main__":
    ans, space = solve_1(read_file("input.txt"))
    print(solve_2(space))