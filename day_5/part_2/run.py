from collections.abc import Generator
from operator import index
import numpy as np
from scipy.signal import convolve2d


day = 5
part = 2
input_file_name = 'input.txt'

input_file = f'./day_{day}/part_{part}/{input_file_name}'

def read_input_line(file_path) -> Generator[str, None, None]:
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()
            
def remove_overlapping_ranges(ranges: list[tuple[int, int]]) -> list[list[tuple[int,int]]]:
    cleaned_ranges = []
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    cleaned_ranges.append(sorted_ranges[0])
    for range in sorted_ranges[1:]:
        if range[0] <= cleaned_ranges[-1][1]:
            cleaned_ranges[-1] = (cleaned_ranges[-1][0], max(cleaned_ranges[-1][1], range[1]))
        else:
            cleaned_ranges.append(range)
    return cleaned_ranges

def run():
    print("This is Day 5, Part 1!")
    id_ranges = []
    for line in read_input_line(input_file):
        if '-' in line:
            id_ranges.append((int(line.split('-')[0]), int(line.split('-')[1])))

    print("Number of ID ranges:", len(id_ranges))
    id_ranges = remove_overlapping_ranges(id_ranges)
    print(f"Number of cleaned ID ranges: {len(id_ranges)}")
    total_fresh_ids = 0
    for id_range in id_ranges:
        total_fresh_ids += id_range[1] - id_range[0] + 1
    print(f"Total fresh IDs in ranges: {total_fresh_ids}")

if __name__ == "__main__":
    run()