from utils import get_puzzle_input

paper_roll_map = get_puzzle_input(4).splitlines()
# paper_roll_map = '''..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.'''.splitlines()

# Part 1

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = paper_roll_map[x][y]
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

def is_paper_roll(point: Point):
    return point.value == '@'

def is_accessible_by_forklift(point: Point):
    return sum([is_paper_roll(point) for point in get_adjacent_positions(point)]) < 4

def get_adjacent_positions(point: Point):
    positions = []

    is_not_top_border = point.x != 0
    is_not_bottom_border = point.x != len(paper_roll_map) - 1
    is_not_left_border = point.y != 0
    is_not_right_border = point.y != len(paper_roll_map) - 1

    if (is_not_top_border):
        positions.append(Point(point.x - 1,  point.y))
    
    if (is_not_left_border):
        positions.append(Point(point.x, point.y - 1))
    
    if (is_not_bottom_border):
        positions.append(Point(point.x + 1, point.y))
    
    if (is_not_right_border):
        positions.append(Point(point.x, point.y + 1))

    if (is_not_top_border and is_not_left_border):
        positions.append(Point(point.x - 1, point.y - 1))

    if (is_not_top_border and is_not_right_border):
        positions.append(Point(point.x - 1, point.y + 1))

    if (is_not_bottom_border and is_not_left_border):
        positions.append(Point(point.x + 1, point.y - 1))

    if (is_not_bottom_border and is_not_right_border):
        positions.append(Point(point.x + 1, point.y + 1))

    return positions

def get_accessible_paper_rolls_sum():
    accessible_paper_rolls = 0

    for line_index in range(len(paper_roll_map[0])):
        for column_index in range(len(paper_roll_map)):
            point = Point(int(line_index), int(column_index))
            if (is_paper_roll(point)):
                if (is_accessible_by_forklift(point)):
                    accessible_paper_rolls += 1
    
    return accessible_paper_rolls

print(get_accessible_paper_rolls_sum())