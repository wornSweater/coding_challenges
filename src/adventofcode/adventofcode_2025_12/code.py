def read_file(filename):

    import os
    base_dir = os.path.dirname(__file__)
    filepath = os.path.join(base_dir, filename)
    
    shapes = {}
    regions = []
    
    current_id = None
    current_coords = []
    y_offset = 0
    
    with open(filepath, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line: continue # skip the space

        # if this is the region grid
        if 'x' in line.split(':')[0] and ':' in line:
            dim_part, qty_part = line.split(':')
            width, height = map(int, dim_part.lower().split('x'))
            quantities = list(map(int, qty_part.strip().split()))
            regions.append({
                'width': width,
                'height': height,
                'needed_shapes': quantities
            })
            continue

        # if this is the shape
        if ':' in line and 'x' not in line:
            # store the previous shape
            if current_id is not None:
                shapes[current_id] = current_coords
            
            current_id = int(line.replace(':', ''))
            current_coords = []
            x_offset = 0
            continue

        # deal with the shapes
        if '#' in line or '.' in line:
            for y_offset, char in enumerate(line):
                if char == '#':
                    current_coords.append((x_offset, y_offset))
            x_offset += 1

    # store the last shape
    if current_id is not None and current_id not in shapes:
        shapes[current_id] = current_coords

    return shapes, regions

def solve_1(shapes, regions):
    
    count = 0

    for region in regions:

        count += sum(region["needed_shapes"]) * 8 < region["width"] * region["height"]

    return count
                
if __name__ == "__main__":

    shapes, regions = read_file('input.txt')
    print(solve_1(shapes, regions))