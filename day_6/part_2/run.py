from collections.abc import Generator


day = 6
part = 2
input_file_name = 'input.txt'

input_file = f'./day_{day}/part_{part}/{input_file_name}'

def read_input_line(file_path) -> Generator[str, None, None]:
    with open(file_path, 'r') as f:
        for line in f:
            yield line
            
def run():
    print(f"This is Day {day}, Part {part}!")
    # Read input, all spaces are relevant also trailing ones !!!
    inputs = []
    for line in read_input_line(input_file):
        inputs.append(line)
    operations = inputs[len(inputs)-1]
    values = inputs[0:len(inputs)-1]
    print("values:", values)
    print("operations:", operations)
    # Decode all input lines into list of values
    decoded_values = []
    for index, value in enumerate(values[0]):
        decoded_value = ""
        for value_line in values:
            decoded_value += value_line[index]
        decoded_value = decoded_value.strip()
        decoded_values.append(decoded_value)
    print(decoded_values)
    # Split decoded values into per operation lists
    values_per_op = []
    op_values = []
    for decoded_value in decoded_values:
        if decoded_value != "":
            op_values.append(int(decoded_value))
        else:
            values_per_op.append(op_values)
            op_values = []
    print("values per op:", values_per_op)
    operations = operations.split()
    print("operations:", operations)
    # Execute operations
    total_result = 0
    for index, operation in enumerate(operations):
        if operation == '+':
            operation_result = 0
            for value in values_per_op[index]:
                operation_result += value
        elif operation == '*':
            operation_result = 1
            for value in values_per_op[index]:
                operation_result *= value
        else:
            raise ValueError(f"Unknown operation: {operation}")
        total_result += operation_result
    print(f"Total result: {total_result}")
        
if __name__ == "__main__":
    run()