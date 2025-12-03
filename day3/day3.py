from utils import get_puzzle_input

battery_banks = get_puzzle_input(3).splitlines()

# battery_banks = '''987654321111111
# 811111111111119
# 234234234234278
# 818181911112111'''.splitlines()

def get_highest_joltage_battery_pair(battery_bank):
    first_highest_joltage_battery_index = battery_bank.index(max(battery_bank))
    second_highest_joltage_battery_index = 1

    if (first_highest_joltage_battery_index == len(battery_bank) - 1):
        second_highest_joltage_battery_index = first_highest_joltage_battery_index
        first_highest_joltage_battery_index = battery_bank.index(max(battery_bank[:second_highest_joltage_battery_index]))

    second_highest_joltage_battery_index = battery_bank.index(max(battery_bank[first_highest_joltage_battery_index + 1:]))

    return int(battery_bank[first_highest_joltage_battery_index] + battery_bank[second_highest_joltage_battery_index])

def get_battery_pair_joltage_sum():
    return sum([get_highest_joltage_battery_pair(battery_bank) for battery_bank in battery_banks])

print(get_battery_pair_joltage_sum())