from time import time

def read_file(filename):

    import os
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)

    ns = []

    with open(filepath, 'r') as file:
        for line in file.readlines():
            ns.append(line.strip())

    return ns

def solve_1(ns):

    #### two pointers, linear time

    #################################################################################
    # The biggest problem for this one is the equality missing in int(n[cur]) >= int(n[nex]), for example missing 99
    ##################################################################################
    
    ans = 0

    for n in ns:
        cur, nex = 0, 1 # set the two pointers
        max_cur = 10 * int(n[cur]) + int(n[nex]) # set the current max
        while nex < len(n) - 1:
            if int(n[cur]) >= int(n[nex]):
                nex += 1
                if max_cur < 10 * int(n[cur]) + int(n[nex]):
                    max_cur = 10 * int(n[cur]) + int(n[nex])
            else:
                cur = nex
                nex += 1
                max_cur = 10 * int(n[cur]) + int(n[nex])

        ans += max_cur

    return ans

def solve_1_new(ns):

    ### combinations, polynomial time, both are 20 times solution time
    
    ans = 0

    for n in ns:
        coms = []
        for i in range(len(n) - 1):
            for k in range(i + 1, len(n)):
                coms.append(10 * int(n[i]) + int(n[k]))
        ans += max(coms)

    return ans 

def solve_2(ns, digits=12):

    #######################################################################
    # 1. remember to update the max value to compare and figure out where to start to compare (from cur + 1)
    # 2. figure out the condition for len(n) - i>= digits - len(res)
    # 3. this method is a general one that can solve both questions 1 and 2

    ans = 0

    # first, we need to set the num of digits

    for n in ns:

        cur = 0 # index to loop 
        max_index = cur # max index
        res = ""

        while len(res) < digits:

            max_value = int(n[max_index]) # remember to update the max value

            for i in range(cur + 1, len(n)): # start searching from the next one
                if max_value < int(n[i]) and len(n) - i >= digits - len(res): # attention to the left digits num
                    max_value = int(n[i])
                    max_index = i
            
            res += n[max_index]
            max_index += 1
            cur = max_index

        ans += int(res)

    return ans

if __name__ == "__main__":

    print(solve_2(read_file("input.txt")))
