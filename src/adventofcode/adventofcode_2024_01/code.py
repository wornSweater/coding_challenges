def read_file(filename):

    import os
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)

    left_list = []
    right_list = []

    with open(filepath, 'r') as file:
        for line in file.readlines():
            left = int(line.strip().split("   ")[0])
            right = int(line.strip().split("   ")[1])

            left_list.append(left)
            right_list.append(right)

    return left_list, right_list

def solve_1(left_list, right_list):

    # be careful to use the string [] index, the number is multiple digitis, better to use split
    # be careful when add a number into the dict the number is 1 not 0

    left_list = sorted(left_list)
    right_list = sorted(right_list)

    ans = 0
    for i in range(len(left_list)):
        ans += abs(left_list[i] - right_list[i])

    return ans

def solve_2(left_list, right_list):

    # better to use dict (hashmap)

    right_dict = {}
    
    for num in right_list:
        if num in right_dict.keys():
            right_dict[num] += 1
        else:
            right_dict[num] = 1

    ans = 0
    for num in left_list:
        if num in right_dict.keys():
            ans += num * right_dict[num]
        else:
            continue

    return ans

print(solve_1(*read_file("input.txt")))
print(solve_2(*read_file("input.txt")))