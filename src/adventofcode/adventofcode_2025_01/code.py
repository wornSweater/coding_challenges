def read_file(filename):

    import os
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)

    o = []
    with open(filepath, 'r') as file:
        for line in file.readlines():
            n = int(line[1:]) if line[0] == "R" else -int(line[1:])
            o.append(n)
    return o
    

def solve_1(o):
    init = 50
    ans = 0

    for i in o:

        init += (i % 100)

        if init > 99:
            init -= 100

        if init == 0:
            ans += 1

    return ans

def solve_2(o):
    ans = 0
    start = 50
    for operation in o:
        if operation > 0:
            for _ in range(operation):
                start += 1
                if start > 99:
                    start = 0
                if start == 0:
                    ans += 1
        else:
            for _ in range(-operation):
                start -= 1
                if start < 0:
                    start = 99
                if start == 0:
                    ans += 1

    return ans

if __name__ == "__main__":
    print(solve_2(read_file("input.txt")))