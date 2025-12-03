from collections.abc import Generator

input_file = './day_3/part_1/input.txt'

def read_input_line(file_path) -> Generator[str, None, None]:
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()

def get_first_largest_digit(battery_bank: str) -> tuple[int,int]:
    print(f"Finding largest digit in {battery_bank}")
    max_digit_index = 0
    max_digit_value = int(battery_bank[0])
    for index, character in enumerate(battery_bank):
        if (int(character) > max_digit_value) and (index > max_digit_index):
            max_digit_value = int(character)
            max_digit_index = index
    print(f"Largest digit is {max_digit_value} at index {max_digit_index}")
    return tuple([max_digit_index,max_digit_value])

def determine_maximum_joltage(battery_bank: str) -> int:
    print(f"Determining maximum joltage for battery bank {battery_bank}")
    first_sub_battery_bank = battery_bank[:-1] # fist digit cannot be the last digit
    first_digit_index, first_digit_value = get_first_largest_digit(first_sub_battery_bank)
    second_sub_battery_bank = battery_bank[first_digit_index + 1 :]
    _, second_digit_value = get_first_largest_digit(second_sub_battery_bank)
    result = int(f"{first_digit_value}{second_digit_value}")
    print(f"Maximum joltage determined: {result}")
    return result

def run():
    print("This is Day 3, Part 1!")
    total_maximum_joltage = 0
    for battery_bank in read_input_line(input_file):
        maximum_joltage = determine_maximum_joltage(battery_bank)
        total_maximum_joltage += maximum_joltage
    print(f"Total maximum joltage: {total_maximum_joltage}")

if __name__ == "__main__":
    run()
    