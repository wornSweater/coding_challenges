def read_file(filename):

    import os
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)

    locs = []
    with open(filepath, 'r') as file:
        for line in file.readlines():
            locs.append((int(line.strip().split(",")[0]), int(line.strip().split(",")[1])))

    return locs
    
def solve_1(locs):
    
    ans = 0

    for i in range(len(locs)):
        for j in range(i+1, len(locs)):
            new_area = (abs(locs[j][0] - locs[i][0]) + 1) * (abs(locs[j][1] - locs[i][1]) + 1)
            if new_area >= ans:
                ans = new_area

    return ans

def points_on_edges(locs):
    
    points = []

    for i in range(len(locs)):
        point_1 = locs[i]
        point_2 = locs[(i+1) % len(locs)]  # wrap around

        if point_1[0] == point_2[0]:  # vertical
            x = point_1[0]
            y_start = min(point_1[1], point_2[1])
            y_end = max(point_1[1], point_2[1])
            for y in range(y_start, y_end + 1):
                points.append((x, y))

        elif point_1[1] == point_2[1]:  # horizontal
            y = point_1[1]
            x_start = min(point_1[0], point_2[0])
            x_end = max(point_1[0], point_2[0])
            for x in range(x_start, x_end + 1):
                points.append((x, y))

    return list(set(points))  # remove duplicates

def solve_2(locs):

    edge_points = points_on_edges(locs)

    # define the bounds
    upper = max([loc[0] for loc in locs])
    lower = min([loc[0] for loc in locs])
    right = max([loc[1] for loc in locs])
    left = min(loc[1] for loc in locs)

    print((upper - lower) * (right - left))

    # by using BFS or DFS to get all the non-red non-green tiles

    # 
    start = (upper, right)

    for i in range(len(locs)):
        point_1 = locs[i]
        point_2 = locs[(i+1) % len(locs)]  # wrap around

        if point_1[0] == point_2[0] == upper:
            inter = (upper-1, int((point_1[1] + point_2[1])/2))
            if inter not in edge_points:
                start = inter
    
    print(start)
            

    queue = [start]
    visited = set([start])

    # define the directions to iterate
    directions = [
        (1, 0), (-1, 0),
        (0, 1), (0, -1),
    ]

    while queue:
        
        point = queue.pop()

        for dx, dy in directions:
            nx = point[0] + dx
            ny = point[1] + dy

            # check if the new point touches the edge
            if (
                lower <= nx <= upper and
                left <= ny <= right and
                (nx, ny) not in edge_points
            ):
                
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    
    visited = visited.union(set(edge_points))

    ans = 0

    for i in range(len(locs)):
        for j in range(i+1, len(locs)):
            if locs[i][0] >= locs[j][0] and locs[i][1] >= locs[j][1]:
                if any((x, y) not in visited for x in range(locs[j][0], locs[i][0] + 1) for y in range(locs[j][1], locs[i][1] + 1)):
                    continue
            if locs[i][0] >= locs[j][0] and locs[i][1] <= locs[j][1]:
                if any((x, y) not in visited for x in range(locs[j][0], locs[i][0] + 1) for y in range(locs[i][1], locs[j][1] + 1)):
                    continue
            if locs[i][0] <= locs[j][0] and locs[i][1] >= locs[j][1]:
                if any((x, y) not in visited for x in range(locs[i][0], locs[j][0] + 1) for y in range(locs[j][1], locs[i][1] + 1)):
                    continue
            if locs[i][0] <= locs[j][0] and locs[i][1] <= locs[j][1]:
                if any((x, y) not in visited for x in range(locs[i][0], locs[j][0] + 1) for y in range(locs[i][1], locs[j][1] + 1)):
                    continue
            
            new_area = (abs(locs[j][0] - locs[i][0]) + 1) * (abs(locs[j][1] - locs[i][1]) + 1)
            if new_area > ans:
                ans = new_area

    return ans 

if __name__ == "__main__":
    from itertools import combinations

    import numpy as np
    import shapely

    points = np.genfromtxt(r"src\adventofcode\adventofcode_2025_09\input.txt", dtype=np.int64, comments=None, delimiter=",")

    polygon = shapely.Polygon(points)

    largest_area_p1 = 0
    largest_area_p2 = 0

    for p1, p2 in combinations(points, 2):
        x_min, x_max = min(p1[0], p2[0]), max(p1[0], p2[0])
        y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])

        area = (x_max - x_min + 1) * (y_max - y_min + 1)
        largest_area_p1 = max(largest_area_p1, area)

        if polygon.contains(shapely.box(x_min, y_min, x_max, y_max)):
            largest_area_p2 = max(largest_area_p2, area)

    print(largest_area_p1, largest_area_p2)