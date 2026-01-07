def read_file(filename):

    import os
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)

    matrix = []

    with open(filepath, 'r') as file:
        for row in file.readlines():
            matrix.append(list(row.strip()))

    return matrix

def solve_1(matrix):

    directions = [
        (-1,-1), (-1,0), (-1,1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]
    
    ans = 0
    takens = []

    shape = (len(matrix), len(matrix[0]))
    for i in range(shape[0]): 
        for j in range(shape[1]): # for each point in the matrix

            if matrix[i][j] == "@":  # make sure this point is a target

                neighbors = 0

                for di, dj in directions:  # iterate the 8 neighboring points
                    if 0 <= i + di < shape[0] and 0 <= j + dj < shape[1] and matrix[i + di][j + dj] == "@": # if not out of the bound
                        neighbors += 1

                if neighbors < 4:
                    ans += 1
                    takens.append((i, j))

    for i, j in takens:
        matrix[i][j] = "x"

    return ans

def solve_2(matrix):

    directions = [
        (-1,-1), (-1,0), (-1,1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]

    def scan(matrix_example):

        takens = []
        shape = (len(matrix_example), len(matrix_example[0]))

        for i in range(shape[0]): 
            for j in range(shape[1]): # for each point in the matrix

                if matrix_example[i][j] == "@":  # make sure this point is a target

                    neighbors = 0

                    for di, dj in directions:  # iterate the 8 neighboring points
                        if 0 <= i + di < shape[0] and 0 <= j + dj < shape[1] and matrix_example[i + di][j + dj] == "@": # if not out of the bound
                            neighbors += 1

                    if neighbors < 4:
                        takens.append((i, j))
        return takens
    
    # record the number of paper rolls
    ans = 0

    while scan(matrix):

        takens = scan(matrix)
        ans += len(takens)

        for i, j in takens:
            matrix[i][j] = "x"

    print(matrix)

    return ans

if __name__ == "__main__":
    print(solve_2(read_file("input.txt")))