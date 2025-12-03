from collections.abc import Generator

input_file = './day_3/part_2/input.txt'

def read_input_line(file_path) -> Generator[str, None, None]:
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()

def get_first_largest_digit(battery_bank: str) -> tuple[int,int]:
    #print(f"Finding largest digit in {battery_bank}")
    max_digit_index = 0
    max_digit_value = int(battery_bank[0])
    for index, character in enumerate(battery_bank):
        if (int(character) > max_digit_value) and (index > max_digit_index):
            max_digit_value = int(character)
            max_digit_index = index
    #print(f"Largest digit is {max_digit_value} at index {max_digit_index}")
    return tuple([max_digit_index,max_digit_value])

def determine_maximum_joltage(battery_bank: str) -> int:
    print(f"Determining maximum joltage for battery bank {battery_bank}")
    print(len(battery_bank))
    nr_of_digits = 12
    digit_indexes = []
    digit_values = []
    for digit_nr in range(0,nr_of_digits,1):
        sub_start_index = digit_indexes[-1] + 1 if digit_indexes else 0
        sub_end_index = len(battery_bank) - (nr_of_digits - digit_nr - 1)
        sub_battery_bank = battery_bank[sub_start_index:sub_end_index]
        digit_index, digit_value = get_first_largest_digit(sub_battery_bank)
        digit_indexes.append(digit_index + sub_start_index)
        digit_values.append(digit_value)
        print(f"Sub battery bank from {sub_start_index} to {sub_end_index}: {sub_battery_bank}")
    maximium_joltage = int(''.join([str(d) for d in digit_values]))
    print(f"Maximum joltage determined: {maximium_joltage}")
    return maximium_joltage

def run():
    print("This is Day 3, Part 1!")
    total_maximum_joltage = 0
    for battery_bank in read_input_line(input_file):
        maximum_joltage = determine_maximum_joltage(battery_bank)
        total_maximum_joltage += maximum_joltage
    print(f"Total maximum joltage: {total_maximum_joltage}")

if __name__ == "__main__":
    run()
    