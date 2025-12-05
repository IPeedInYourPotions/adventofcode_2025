from collections.abc import Generator
from operator import index
import numpy as np
from scipy.signal import convolve2d

input_file = './day_4/part_2/input.txt'

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

def get_neighbor_indices(idx: tuple[int, int]) -> list[tuple[int, int]]:
    neighbor_idxs = [(idx[0]-1, idx[1]-1), (idx[0]-1, idx[1]), (idx[0]-1, idx[1]+1),
                     (idx[0], idx[1]-1),                     (idx[0], idx[1]+1),
                     (idx[0]+1, idx[1]-1), (idx[0]+1, idx[1]), (idx[0]+1, idx[1]+1)]
    return neighbor_idxs

def solve_using_iteration():
    input = []
    for line in read_input_line(input_file):
        input.append(input_line_to_matrix(line))
    role_positions = np.array(input)
    print(f"Initial role positions:\n{role_positions}")
    padded_role_positions = np.pad(role_positions, pad_width=1, mode='constant', constant_values=0)
    print(f"Padded role positions:\n{padded_role_positions}")
    total_removable_roles = 0
    while True:
        removable_roles_idxs = []
        for idx, position in np.ndenumerate(padded_role_positions):
            if position == 0: # edge positions are 0 so are skipped here
                continue
            neighbor_idxs = get_neighbor_indices(idx)
            nr_of_occupied_neighbors = 0
            for neighbor_idx in neighbor_idxs:
                if padded_role_positions[neighbor_idx] == 1:
                    nr_of_occupied_neighbors += 1
            if nr_of_occupied_neighbors < 4:
                removable_roles_idxs.append(idx)
        if len(removable_roles_idxs) == 0:
            break
        else:
            for removable_role_idx in removable_roles_idxs:
                padded_role_positions[removable_role_idx] = 0
                total_removable_roles += 1
            print(f"Removed {len(removable_roles_idxs)} roles, updated positions:\n{padded_role_positions}")
    print(f"Final role positions:\n{padded_role_positions}")
    print(f"Total removable roles: {total_removable_roles}")

def solve_using_convolution():
    role_positions = []
    for line in read_input_line(input_file):
        role_positions.append(input_line_to_matrix(line))
    role_positions = np.array(role_positions)
    total_roles_removed = 0
    while True:
        print(f"Current role positions:\n{role_positions}")
        removable_roles = 0
        kernel = np.array([[1, 1, 1],
                        [1, 0, 1],
                        [1, 1, 1]])
        surroundings = convolve2d(role_positions, kernel, mode='same', boundary='fill', fillvalue=0)
        removable_roles = ((surroundings < 4) & (role_positions == 1)).astype(int)
        nr_removable_roles = np.sum(removable_roles)
        if nr_removable_roles == 0:
            break
        role_positions = role_positions * (1-removable_roles)
        total_roles_removed += nr_removable_roles   
        print(f"Removed roles this iteration: {nr_removable_roles}")
    print(f"Total roles removed: {total_roles_removed}") 

def run():
    print("This is Day 4, Part 2!")
    solve_using_iteration()
    solve_using_convolution()

if __name__ == "__main__":
    run()