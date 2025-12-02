from utils import get_puzzle_input

# rotations = get_puzzle_input(1).splitlines()
rotations = '''L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82'''.splitlines()
dial_position = 50
pointing_zero_amount = 0

def part1(dial_position, pointing_zero_amount):
    for rotation in rotations:
        rotation_value = int(rotation[1:])

        if rotation[0] == 'L':
            dial_position -= rotation_value
        else:
            dial_position += rotation_value
        
        if dial_position < 0:
            dial_position += 100
        
        dial_position %= 100

        if dial_position == 0:
            pointing_zero_amount += 1

    return pointing_zero_amount

print(part1(dial_position, pointing_zero_amount))


def part2(dial_position, pointing_zero_amount):
    for rotation in rotations:
        rotation_value = int(rotation[1:])

        if rotation[0] == 'L':
            dial_position -= rotation_value
        else:
            dial_position += rotation_value

        if dial_position < 0:
            dial_position += 100
        
        pointing_zero_amount += abs(dial_position) // 100
        dial_position %= 100

        if dial_position == 0:
            pointing_zero_amount += 1

        print(dial_position, pointing_zero_amount)
    return pointing_zero_amount

print(part2(dial_position, pointing_zero_amount))