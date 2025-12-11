from collections.abc import Generator
import math
import numpy as np
import heapq

day = 8
part = 1
input_file_name = 'input.txt'

nr_of_iterations = 10 if input_file_name == 'test_input.txt' else 1000

input_file = f'./day_{day}/part_{part}/{input_file_name}'

def read_input_line(file_path) -> Generator[str, None, None]:
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()
            
def get_euclidean_distance(point1: tuple[int, int, int], point2: tuple[int, int, int]) -> float:
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2)

def get_index_minimum_nonzero_value(input_array:np.array):
    min_value = None
    min_index = None
    for idx, value in np.ndenumerate(input_array):
        if value == 0:
            continue
        if min_value is None or value < min_value:
            min_value = value
            min_index = idx
    return min_index

def add_pair_to_circuits(pair: tuple[tuple[int, int, int], tuple[int, int, int]], circuits: list[list[tuple[int, int, int]]]) -> list[list[tuple[int, int, int]]]:
    box1_in_circuit_idx = None
    box2_in_circuit_idx = None
    for circuit_idx, circuit in enumerate(circuits):
        if pair[0] in circuit:
            box1_in_circuit_idx = circuit_idx
        if pair[1] in circuit:
            box2_in_circuit_idx = circuit_idx
    if box1_in_circuit_idx is not None and box2_in_circuit_idx is not None:
        if box1_in_circuit_idx != box2_in_circuit_idx:
            # Merge circuits
            circuits[box1_in_circuit_idx].extend(circuits[box2_in_circuit_idx])
            del circuits[box2_in_circuit_idx]
    elif box1_in_circuit_idx is not None:
        circuits[box1_in_circuit_idx].append(pair[1])
    elif box2_in_circuit_idx is not None:
        circuits[box2_in_circuit_idx].append(pair[0])
    else:
        circuits.append([pair[0], pair[1]])
    return circuits

def run():
    junction_boxes = []
    for line in read_input_line(input_file):
        junction_boxes.append(tuple(int(x) for x in line.split(',')))
    
    distances = np.array([[0 for _ in range(len(junction_boxes))] for _ in range(len(junction_boxes))])
    distances = distances.astype(float)
    distance_heap = []
    
    for index_box1, box1 in enumerate(junction_boxes):
        for index_box2, box2 in enumerate(junction_boxes):
            if index_box1 == index_box2:
                continue
            distance = get_euclidean_distance(box1, box2)
            distances[index_box1][index_box2] = distance
            # Only add each pair once (index_box1 < index_box2)
            if index_box1 < index_box2:
                heapq.heappush(distance_heap, (distance, index_box1, index_box2))
    
    circuits = []
    processed_pairs = set()
    processed_junctions = set()
    
    for _ in range(nr_of_iterations):
        # Get next minimum distance from heap
        while distance_heap:
            _, idx1, idx2 = heapq.heappop(distance_heap)
            # Skip if this pair was already processed
            if (idx1, idx2) not in processed_pairs and (idx2, idx1) not in processed_pairs:
                break
        else:
            print("No more distances available")
            break
            
        processed_pairs.add((idx1, idx2))
        processed_junctions.add(idx1)
        processed_junctions.add(idx2)
        min_distance_pair = (junction_boxes[idx1], junction_boxes[idx2])
        circuits = add_pair_to_circuits(min_distance_pair, circuits)

    print(f'Number of circuits: {len(circuits)}')
    circuit_lengths = []
    for circuit in circuits:
        circuit_lengths.append(len(circuit))
    circuit_lengths.sort()
    print(f'Circuit lengths: {circuit_lengths}')
    result = 1
    for length in circuit_lengths[-3:]:
        result *= length
    print(f'Result (product of lengths of 3 longest circuits): {result}')






if __name__ == "__main__":
    run()