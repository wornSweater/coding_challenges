def read_file(filename):

    import os
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)

    bounds = []
    ingred = []

    with open(filepath, 'r') as file:
        for line in file.readlines():
            if "-" in line:
                bounds.append(line.strip().split("-"))
            else:
                ingred.append(line.strip())

    return bounds, ingred

def solve_1(bounds, ingred):
    
    ans = 0
    
    for i in ingred:
        if i == '':
            continue
        else:
            for bound in bounds:
                if int(bound[0]) <= int(i) <= int(bound[1]):
                    ans += 1
                    break # avoid multiple checks plus

    return ans

# def solve_2(bounds): # invalid solution

#     ans = 0

#     bound_max = max(bounds, key=lambda x: int(x[1]))
    
#     for i in range(int(bound_max[1]) + 1):
#         for bound in bounds:
#             if int(bound[0]) <= i <= int(bound[1]):
#                 ans += 1
#                 break # avoid double plus

#     return ans

def solve_2(bounds): 

    bounds = sorted(bounds, key=lambda x: int(x[0]))

    comb = []

    for bound in bounds:

        lb = int(bound[0])
        ub = int(bound[1])

        if not comb:
            comb.append(bound)
        else:
            for index, bound_in in enumerate(comb):
                
                # case 1: if subset
                if lb >= int(bound_in[0]) and ub <= int(bound_in[1]):
                    break
                
                # case 2: if superset
                elif lb <= int(bound_in[0]) and ub >= int(bound_in[1]):
                    bound_in[0] = lb
                    bound_in[1] = ub
                    break

                # case 3: if no intersection              # the biggest problem is here, note that point overlap is also intersection, lb >= int(bound_in[1]) is wrong
                elif lb > int(bound_in[1]):
                    if index < len(comb) - 1:
                        continue
                    else:
                        comb.append(bound)

                # case 4: if intersection
                else:
                    bound_in[0] = min(int(bound_in[0]), int(bound_in[1]), lb, ub)
                    bound_in[1] = max(int(bound_in[0]), int(bound_in[1]), lb, ub)
    
    ans = 0

    for bound in comb:
        ans += int(bound[1]) - int(bound[0]) + 1

    return ans

def solve_2_new(bounds):

    bounds = sorted(bounds, key=lambda x: int(x[0])) # sort to simplify the cases -> only should compare upper bounds

    comb = []

    for bound in bounds:

        lb = int(bound[0])
        ub = int(bound[1])

        if not comb:
            comb.append(bound)
        else:
            if lb > int(comb[-1][1]):
                comb.append(bound)
            else:
                comb[-1][1] = max(ub, int(comb[-1][1])) # the sort is only based on the lb, need to compare the upper bounds -> [3, 10] [7, 9]
    
    ans = 0

    for bound in comb:
        ans += int(bound[1]) - int(bound[0]) + 1

    return ans

if __name__ == "__main__":
    print(solve_2_new(read_file("input.txt")[0]))
