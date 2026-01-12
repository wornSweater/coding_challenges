import re

def parse_line(line):
    # 1. Extract the Target Diagram content [ ... ]
    target_str = re.search(r'\[(.*?)\]', line).group(1)
    
    # 2. Extract all Buttons ( ... ) as a list of strings
    button_groups = re.findall(r'\((.*?)\)', line)
    
    # --- Convert to Numbers ---
    
    # Target: Convert "#" to 1 and "." to 0 bits
    target_mask = 0
    for i, char in enumerate(target_str):
        if char == '#':
            target_mask |= (1 << i)
            
    # Buttons: Convert comma-separated indices to a single integer mask
    button_masks = []
    for group in button_groups:
        mask = 0
        indices = map(int, group.split(','))
        for idx in indices:
            mask |= (1 << idx)
        button_masks.append(mask)
            
    return target_mask, button_masks

def parse_part2_line(line):
    # 1. Extract the target values {3,5,4,7} -> (3, 5, 4, 7)
    target_match = re.search(r'\{(.*?)\}', line)
    if not target_match:
        return None, None
    target_vector = tuple(map(int, target_match.group(1).split(',')))

    # 2. Extract button groups (1,3) (2) etc.
    button_matches = re.findall(r'\((.*?)\)', line)

    num_counters = len(target_vector)
    button_vectors = []

    for group in button_matches:
        # Create a "zero vector" for this button
        btn_vec = [0] * num_counters
        
        # Mark a 1 for every counter this button increments
        indices = map(int, group.split(','))
        for idx in indices:
            if idx < num_counters:
                btn_vec[idx] = 1
        
        # Convert to tuple for consistency
        button_vectors.append(tuple(btn_vec))
            
    return target_vector, button_vectors

def read_file(filename):
    
    #########################################################################################
    # can not use dict since the target will be the same and miss some lines
    #########################################################################################

    import os
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)

    manual = []
    with open(filepath, 'r') as file:
        for line in file.readlines():
            target_mask, button_masks = parse_line(line)
            manual.append((target_mask, button_masks))

    return manual

def read_file_part_2(filename):

    import os
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)

    manual = []
    with open(filepath, 'r') as file:
        for line in file.readlines():
            target_vector, button_vectors = parse_part2_line(line)
            manual.append((target_vector, button_vectors))

    return manual
    
def bfs(target, buttons):

    from collections import deque

    queue = deque([(0, 0)])
    visited = {0}
    
    while queue:

        current_state, current_count = queue.popleft()

        for button in buttons:

            next_state = current_state ^ button

            if target == next_state:
                return current_count + 1
            
            else:
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, current_count + 1))

    return 0

def bfs_vector(target_vector, button_vectors):
    from collections import deque

    start = tuple([0] * len(target_vector))
    if start == target_vector:
        return 0
        
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        current_state, current_count = queue.popleft()

        for button_vector in button_vectors:
            # 1. Fast vector addition
            next_state = tuple(map(sum, zip(current_state, button_vector)))

            # 2. Check if we won
            if next_state == target_vector:
                return current_count + 1
            
            # 3. CRITICAL PRUNING: Only proceed if we haven't overshot the target
            # If any counter > target, we can never fix it (since buttons only add)
            is_valid = True
            for i in range(len(target_vector)):
                if next_state[i] > target_vector[i]:
                    is_valid = False
                    break
            
            if is_valid and next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, current_count + 1))
    
    return 0

def solve_1(manual):

    return sum(bfs(k, v) for k, v in manual)

def solve_2(manual):

    for k, v in manual:
        print(bfs_vector(k, v))

    return sum(bfs_vector(k, v) for k, v in manual)

def solve_2_opt(manual):

    import gurobipy as gp
    from gurobipy import GRB
    
    ans = 0

    for k, v in manual:
        
        m = gp.Model()
        m.setParam('OutputFlag', 0)

        vars = []

        # the num of vars = num of buttons
        for _ in range(len(v)):
            var = m.addVar(lb=0, vtype=GRB.INTEGER)
            vars.append(var)

        # the num of constraints = dimension of tar
        for i in range(len(k)):
            sum = 0
            for j in range(len(v)):
                sum += vars[j] * v[j][i]
            m.addConstr(sum == k[i])

        vars_sum = 0
        for var in vars:
            vars_sum += var

        m.setObjective(vars_sum, GRB.MINIMIZE)
        
        m.optimize()

        if m.status == GRB.OPTIMAL:
            ans += m.ObjVal
        else:
            raise ValueError
        
    return ans

# Example Usage
line = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
target, buttons = parse_part2_line(line)

print(f"Target Vector: {target}")
for i, btn in enumerate(buttons):
    print(f"Button {i} Vector: {btn}")


print(solve_2(read_file_part_2("test.txt")))
print(solve_2_opt(read_file_part_2("input.txt")))
