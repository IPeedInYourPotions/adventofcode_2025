from collections.abc import Generator
from operator import index
import numpy as np
from scipy.signal import convolve2d

input_file = './day_4/part_1/input.txt'

def read_input_line(file_path) -> Generator[str, None, None]:
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()

def input_line_to_matrix(line: str) -> list[int]:
    output = []
    for _, char in enumerate(line):
        if char == '@':
            output.append(1)
        else:
            output.append(0)
    return output

def run():
    print("This is Day 4, Part 1!")
    role_positions = []
    for line in read_input_line(input_file):
        role_positions.append(input_line_to_matrix(line))
    input_matrix = np.array(role_positions)
    print(f"Input matrix:\n{input_matrix}")
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])
    print(f"Kernel:\n{kernel}")
    output_matrix = convolve2d(input_matrix, kernel, mode='same', boundary='fill', fillvalue=0)
    print(f"Output matrix:\n{output_matrix}")
    role_suroundings = output_matrix * input_matrix
    print(f"Role surroundings:\n{role_suroundings}")
    number_of_movable_roles = role_suroundings[(role_suroundings<4) & (role_suroundings>0)].size
    print(f"Number of movable roles: {number_of_movable_roles}")

if __name__ == "__main__":
    run()