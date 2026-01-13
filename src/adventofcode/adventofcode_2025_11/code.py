def read_file(filename):

    import os
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)

    with open(filepath, 'r') as file:
        
        graph = {}
        for line in file.readlines():
            chars = line.strip().split(":")
            current = chars[0]
            next_str = chars[1]
            nexts = next_str.strip().split(" ")

            graph[current] = nexts
    
    return graph

def solve_1(graph):

    ########################################################################################
    # no need to use visited, since one node can be visited multiple time in different ways
    ########################################################################################

    from collections import deque
        
    ans = 0
    queue = deque(["you"])

    while queue:

        current = queue.pop()

        for next in graph[current]:
            if next == "out":
                ans += 1
            else:
                queue.append(next)

    return ans

def solve_1_new(graph):

    visited = {}

    def count_paths(current, target, count=0):

        for next in graph[current]:

            if next in visited.keys():
                count += visited[next]
                continue
            
            if next == target:
                count += 1

            else:
                count += count_paths(next, target)

        visited[current] = count  

        return count
    
    return count_paths("you", "out")


# def solve_2(graph):

#     # split the path into 3 segments
#     # svr
#     # dac fft
#     # out

#     from collections import deque
        
#     # the first segment, if svr -> fft
#     queue = deque(["svr"])
#     svr_fft = 0

#     while queue:

#         current = queue.pop()

#         for next in graph[current]:
#             if next == "fft":
#                 svr_fft += 1
#             else:
#                 if next != "dac" and next != "out":
#                     queue.append(next)

#     # the first segment, if svr -> dac
#     queue = deque(["svr"])
#     svr_dac = 0

#     while queue:

#         current = queue.pop()

#         for next in graph[current]:
#             if next == "dac":
#                 svr_dac += 1
#             else:
#                 if next != "fft" and next != "out":
#                     queue.append(next)

#     # the second segment, if fft -> dac
#     queue = deque(["fft"])
#     fft_dac = 0

#     while queue:

#         current = queue.pop()

#         for next in graph[current]:
#             if next == "dac":
#                 fft_dac += 1
#             else:
#                 if next != "out":
#                     queue.append(next)

#     # the second segment, if dac -> fft
#     queue = deque(["dac"])
#     dac_fft = 0

#     while queue:

#         current = queue.pop()

#         for next in graph[current]:
#             if next == "fft":
#                 dac_fft += 1
#             else:
#                 if next != "out":
#                     queue.append(next)

#     # the third segment, if dac -> out
#     queue = deque(["dac"])
#     dac_out = 0

#     while queue:

#         current = queue.pop()

#         for next in graph[current]:
#             if next == "out":
#                 dac_out += 1
#             else:
#                 if next != "fft":
#                     queue.append(next)

#     # the third segment, if fft -> out
#     queue = deque(["fft"])
#     fft_out = 0

#     while queue:

#         current = queue.pop()

#         for next in graph[current]:
#             if next == "out":
#                 fft_out += 1
#             else:
#                 if next != "dac":
#                     queue.append(next)
    
#     return svr_fft * fft_dac * dac_out + svr_dac * dac_fft * fft_out

def solve_2(graph):

    # from bottom to top, we can directly start
    # from top to botton, we should use recursion
    # idea: split into 3 independent segments, get the product of them

    # for this question, you can prove that, "you can always find a node that points only to the target";
    # otherwise the recursion will never stop for a basic case / or basic case never exist

    visited = {}

    def count_paths(current, target, incorrect_1, incorrect_2, count=0):

        for next in graph[current]:

            if next in visited.keys():
                count += visited[next]
                continue

            else:

                if next == target:
                    count += 1
                else:
                    if next != incorrect_1 and next != incorrect_2:
                        count += count_paths(next, target, incorrect_1, incorrect_2, count=0)

        visited[current] = count

        return count
    
    x1 = count_paths("svr", "fft", "dac", "out")
    visited = {}
    x2 = count_paths("fft", "dac", "out", None)
    visited = {}
    x3 = count_paths("dac", "out", "fft", None)
    visited = {}

    y1 = count_paths("svr", "dac", "fft", "out")
    visited = {}
    y2 = count_paths("dac", "fft", "out", None)
    visited = {}
    y3 = count_paths("fft", "out", "dac", None)

    return x1 * x2 * x3 + y1 * y2 * y3
    

if __name__ == "__main__":
    print(solve_2(read_file("input.txt")))