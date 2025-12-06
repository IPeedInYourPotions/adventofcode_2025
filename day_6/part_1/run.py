from collections.abc import Generator


day = 6
part = 1
input_file_name = 'input.txt'

input_file = f'./day_{day}/part_{part}/{input_file_name}'

def read_input_line(file_path) -> Generator[str, None, None]:
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()

def run():
    print(f"This is Day {day}, Part {part}!")
    inputs = []
    for line in read_input_line(input_file):
        inputs.append(line.split())
    value_lists = inputs[0:len(inputs)-1]
    operations = inputs[len(inputs)-1]
    print("values:", value_lists)
    print("operations:", operations)
    sum_all_operations = 0
    for index, operation in enumerate(operations):
        if operation == '+':
            result = 0
            for value_list in value_lists:
                result += int(value_list[index])
        elif operation == '*':
            result = 1
            for value_list in value_lists:
                result = result * int(value_list[index])
        else:
            raise ValueError(f"Unknown operation: {operation}")
        sum_all_operations += result
    print(f"Sum of all operations: {sum_all_operations}")

if __name__ == "__main__":
    run()