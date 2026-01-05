def read_file(filename):

    import os
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)

    bounds = []

    with open(filepath, 'r') as file:
        for line in file.readlines():
            bounds += line.strip()[:-1].split(",") if line.strip()[-1] == "," else line.strip().split(",")
    
    return bounds

def solve_1(bounds):
    
    ans = 0

    for bound in bounds:
        lb, up = int(bound.split("-")[0]), int(bound.split("-")[1])
        for i in range(lb, up + 1):
            if len(str(i)) % 2 == 0:
                x, y = int(str(i)[:int(len(str(i)) / 2)]), int(str(i)[int(len(str(i)) / 2):])
                if x == y:
                    ans += i
            else:
                continue
    
    return ans

def solve_2(bounds):

    ################################################################################################################################
    # the bug will happen in ilne 41, if we set the chucksize too large, exceeding half (e.g half + 1), then the set len is also 1 #
    ################################################################################################################################

    ans = 0

    for bound in bounds:
        lb, up = int(bound.split("-")[0]), int(bound.split("-")[1])
        for num in range(lb, up + 1): # here the num is an int, need to convert to str
            for k in range(1, int(len(str(num)) / 2) + 1): # here the k is the chunck size
                p = set()
                for i in range(0, int(len(str(num))), k): # here, we split the whole str into pieces based on the chunck size
                    p.add(str(num)[i: i+k])
                if len(p) == 1: # if they are all the same
                    ans += num
                    break
    
    return ans

if __name__ == "__main__":
    print(solve_2(read_file("input.txt")))