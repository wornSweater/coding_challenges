def read_file(filename):

    import os
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)

    lines = []
    with open(filepath, 'r') as file:
        for line in file.readlines():
            lines.append(list(map(int, line.strip().split(" "))))

    return lines

def solve_1(lines):

    ########################################
    ## don't forget to check the first sign

    def is_safe(levels):

        diffs = [levels[i+1] - levels[i] for i in range(len(levels) - 1)]
    
        return all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)
    
    ans = 0

    for line in lines:
        if is_safe(line):
            ans += 1

    return ans

def solve_2(lines):

    def is_safe(levels):

        diffs = [levels[i+1] - levels[i] for i in range(len(levels) - 1)]
    
        return all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)

    def is_really_safe(levels):

        if is_safe(levels):
            return True
        
        return any(is_safe(levels[:i] + levels[i+1:]) for i in range(len(levels)))

    ans = 0

    for line in lines:
        if is_really_safe(line):
            ans += 1

    return ans

if __name__ == "__main__":
    print(solve_2(read_file("input.txt")))