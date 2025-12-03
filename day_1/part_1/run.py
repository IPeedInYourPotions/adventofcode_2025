from unittest import result

input_file = './input.txt'

def read_input(file_path) -> list[str]:
    with open(file_path, 'r') as f:
        return f.readlines()

def run():
    dial_state = 50
    dial_states_zero = 0
    for line in read_input(input_file):
        orientation = line[0]
        steps = int(line[1:].strip())
        if orientation == 'R':
            dial_state += steps
        elif orientation == 'L':
            dial_state -= steps
        dial_state = dial_state % 100  
        if dial_state == 0:
            dial_states_zero += 1
    print(f"Final dial state: {dial_state}")
    print(f"Number of times dial hit zero: {dial_states_zero}")

if __name__ == "__main__":
    run()
    