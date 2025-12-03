from utils import get_puzzle_input

rotations = get_puzzle_input(1).splitlines()
# rotations = '''L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82'''.splitlines()
dial_position = 50
zero_count = 0

def part1(dial_position, zero_count):
    for rotation in rotations:
        rotation_value = int(rotation[1:])

        if rotation[0] == 'L':
            rotation_value *= -1

        dial_position = (dial_position + rotation_value) % 100

        if (dial_position == 0):
            zero_count += 1

    return zero_count

print(part1(dial_position, zero_count))

def part2(dial_position, zero_count):
    for rotation in rotations:
        rotation_value = int(rotation[1:])
        for i in range(rotation_value):
            if (rotation[0] == 'L'):
                dial_position -= 1
            else:
                dial_position += 1

            if dial_position == 0:
                zero_count += 1

        if abs(dial_position) // 100 >= 1:
            zero_count += abs(dial_position) // 100

        dial_position %= 100

    return zero_count

print(part2(dial_position, zero_count))