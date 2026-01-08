def read_file(filename):

    import os
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)

    matrix = []

    with open(filepath, 'r') as file:
        for line in file.readlines():
            nums = []
            for each in line.strip().split():
                nums.append(each.strip())
            matrix.append(nums)

    return matrix

def solve_1(matrix):

    ans = 0
    
    for j in range(len(matrix[0])):
        if matrix[-1][j] == "+":
            sum = 0
            for i in range(len(matrix) - 1):
                sum += int(matrix[i][j])
            ans += sum
        else:
            mul = 1
            for i in range(len(matrix) - 1):
                mul *= int(matrix[i][j])
            ans += mul
    
    return ans

def solve_2(filename):

    import os
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)

    index_loc = []
    matrix = []
    groups = []
    
    with open(filepath, 'r') as file:
        all_lines = file.readlines()
        final_line = all_lines[-1]
        for i in range(len(final_line)):
            if final_line[i] == "*" or final_line[i] == "+":
                index_loc.append(i)
        index_loc.append(-1)
        
        for line in all_lines:
            nums = []
            for i in range(len(index_loc) - 1):
                if index_loc[i+1] != -1:
                    nums.append(line[index_loc[i]:index_loc[i+1]-1])
                else:
                    nums.append(line[index_loc[i]:index_loc[i+1]])

            matrix.append(nums)

    for j in range(len(matrix[0])):
        group = []
        for i in range(len(matrix)):
            group.append(matrix[i][j])
        groups.append(group)

    ans = 0

    for group in groups:
        if group[-1].strip() == "+":
            for j in range(len(group[0]) - 1, -1, -1):
                start = ""
                for i in range(len(group) - 1):
                    start += group[i][j]
                ans += int(start)
        else:
            mul = 1
            for j in range(len(group[0]) - 1, -1, -1):
                start = ""
                for i in range(len(group) - 1):
                    start += group[i][j]
                mul *= int(start)
            ans += mul

    return ans


if __name__ == "__main__":
    print(solve_2("input.txt"))