
input_file = './input.txt'

def read_input(file_path) -> list[str]:
    with open(file_path, 'r') as f:
        return f.readlines()
    
def is_valid_id(id: int) -> bool:
    str_id = str(id)
    if len(str_id) % 2 != 0:
        return True
    elif str_id[:len(str_id)//2] == str_id[len(str_id)//2:]:
            print(f"Invalid ID found: {id}")
            return False
    else:
        return True

def get_invalid_ids(id_range: str) -> list[str]:
    print(f"Analysing ID range: {id_range}")
    range_start, range_end = map(int, id_range.split('-'))
    ids = list(range(range_start, range_end + 1))
    invalid_ids = []
    for id in ids:
        if not is_valid_id(id):
            invalid_ids.append(id)
    return invalid_ids

def run():
    print("This is Day 2, Part 1!")
    input = read_input(input_file)[0]
    id_ranges = input.strip().split(',')
    sum_invalid_ids = 0
    for id_range in id_ranges:
        invalid_ids = get_invalid_ids(id_range)
        for invalid_id in invalid_ids:
            sum_invalid_ids += int(invalid_id)
    print("Sum of all invalid IDs: " + str(sum_invalid_ids))


if __name__ == "__main__":
    run()
    