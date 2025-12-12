from collections.abc import Generator
import math
import numpy as np
import heapq

day = 9
part = 1

input_file_name = 'input.txt'
visualize = False

input_file = f'./day_{day}/part_{part}/{input_file_name}'

def read_input_line(file_path) -> Generator[str, None, None]:
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()

def find_largest_rectangle_area(tiles):
    """Find the largest rectangle that can be formed by any two tiles as opposite corners"""
    max_area = 0
    best_pair = None
    
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            tile1, tile2 = tiles[i], tiles[j]

            width = abs(tile1[0] - tile2[0])
            height = abs(tile1[1] - tile2[1])
            
            area = (width + 1) * (height + 1)
            if area > max_area:
                max_area = area
                best_pair = (tile1, tile2)
    
    return max_area, best_pair

def run():
    red_tiles = []
    max_x = 0
    max_y = 0
    for line in read_input_line(input_file):
        red_tile_coordinate = tuple(int(x) for x in line.split(','))  
        if red_tile_coordinate[0] > max_x:
            max_x = red_tile_coordinate[0]
        if red_tile_coordinate[1] > max_y:
            max_y = red_tile_coordinate[1]
        red_tiles.append(red_tile_coordinate)
    
    if visualize:
        tiles = np.array([["." for _ in range(max_x + 1)] for _ in range(max_y + 1)])  # for visualization
        for tile in red_tiles:
            tiles[tile[1]][tile[0]] = "#"
        print(f"Red tiles grid:\n{tiles}")
    
    max_area, best_pair = find_largest_rectangle_area(red_tiles)

    if visualize:
        tile1, tile2 = best_pair
        for y in range(min(tile1[1], tile2[1]), max(tile1[1], tile2[1]) + 1):
            for x in range(min(tile1[0], tile2[0]), max(tile1[0], tile2[0]) + 1):
                tiles[y][x] = "0"
        print(f"\nLargest rectangle marked with '*':\n{tiles}")

    print(f"\\nLargest rectangle area (integer method): {max_area}")
    if best_pair:
        print(f"Rectangle corners: {best_pair[0]} and {best_pair[1]}")
        
if __name__ == "__main__":
    run()