directions = [
        (-1, 0, 0), (1, 0, 0),
        (0, -1, 0), (0, 1, 0),
        (0, 0, -1), (0, 0, 1),
    ]

def read_file(filename: str) -> set[tuple[int, int, int]]:
    '''
    convert the txt to tuple locations and store in a set
    '''

    import os
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)

    cubes = set()

    with open(filepath, 'r') as file:
        for line in file.readlines():
            cube = tuple(map(int, line.split(",")))
            cubes.add(cube)
    return cubes
    
def solve_1(cubes) -> int:

    ans = 0
    for x, y, z in cubes:
        for dx, dy, dz in directions:
            if (x + dx, y + dy, z + dz) not in cubes:
                surface += 1

    return ans

def solve_2(cubes):
    # idea: use air cubes to touch the surfaces
    
    # find the min and max for each direction (could +- a small int for complete inclusion)
    (min_x, max_x), (min_y, max_y), (min_z, max_z) = tuple((min(v) - 2, max(v) + 2) for v in zip(*cubes))

    # start from an outside cube, let's say (max_x, max_y, max_z)
    # create a list and a visited set, and the time to encounter a cube
    # set the condition of the min max as the bounds
    start = max_x, max_y, max_z
    q = [start]
    v = set(start)
    ans = 0

    while q:

        # BFS: last come first out
        x, y, z = q[-1]
        q.pop()

        # DFS: first come first out
        # x, y, z = q[0]
        # q.pop(0)

        # They are the same since need to iterate all the cubes
        
        for dx, dy, dz in directions:
            nx, ny, nz = x - dx, y - dy, z - dz
            # if within the bounds
            if (
                min_x <= nx <= max_x and 
                min_y <= ny <= max_y and 
                min_z <= nz <= max_z
            ):
                if (nx, ny, nz) in cubes:
                    ans += 1
                else:
                    # avoid multiple count and record the visited cube
                    if (nx, ny, nz) not in v:
                        v.add((nx, ny, nz))
                        q.append((nx, ny, nz))
    return ans

if __name__ == "__main__":
    print(solve_2(read_file("input.txt")))
