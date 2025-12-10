from collections.abc import Generator


day = 7
part = 2
input_file_name = 'input.txt'

input_file = f'./day_{day}/part_{part}/{input_file_name}'

def read_input_line(file_path) -> Generator[str, None, None]:
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()
            
def walk(tachyon_manifold, stage_idx, char_idx, memo=None) -> int:
    if memo is None:
        memo = {}
    
    # Create a key for memoization
    key = (stage_idx, char_idx)
    if key in memo:
        return memo[key]
    
    if stage_idx >= len(tachyon_manifold):
        memo[key] = 1
        return 1
    
    if char_idx < 0 or char_idx >= len(tachyon_manifold[stage_idx]):
        memo[key] = 0
        return 0
    
    stage = tachyon_manifold[stage_idx]
    char = stage[char_idx]
    
    result = 0
    if char == '|':
        result = walk(tachyon_manifold, stage_idx + 1, char_idx, memo)
    elif char == '^':
        walk_left = walk(tachyon_manifold, stage_idx + 1, char_idx - 1, memo)
        walk_right = walk(tachyon_manifold, stage_idx + 1, char_idx + 1, memo)
        result = walk_left + walk_right
    else:
        result = 0
    
    memo[key] = result
    return result
            
def run():
    tachyon_manifold = []
    for line in read_input_line(input_file):
        tachyon_manifold.append(list(line))
    start_index = 0
    nr_of_splits = 0
    for stage_idx, stage in enumerate(tachyon_manifold):
        if stage_idx == 0:
            for char_idx, char in enumerate(stage):
                if char == 'S':
                    tachyon_manifold[stage_idx+1][char_idx] = '|'
                    start_index = char_idx
                    break
        for char_idx, char in enumerate(stage):
            if char == "." and tachyon_manifold[stage_idx-1][char_idx] == '|':
                tachyon_manifold[stage_idx][char_idx] = '|'
            if char == '^' and tachyon_manifold[stage_idx-1][char_idx] == '|':
                tachyon_manifold[stage_idx][char_idx-1] = '|'
                tachyon_manifold[stage_idx][char_idx+1] = '|'
                nr_of_splits += 1
    print(f'Number of splits: {nr_of_splits}')
    for stage in tachyon_manifold:
        print(''.join(stage))

    walked_paths = walk(tachyon_manifold, 1, start_index)
    print(f'Number of walkers: {walked_paths}')

if __name__ == "__main__":
    run()