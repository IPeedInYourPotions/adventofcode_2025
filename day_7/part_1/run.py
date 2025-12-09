from collections.abc import Generator


day = 7
part = 1
input_file_name = 'input.txt'

input_file = f'./day_{day}/part_{part}/{input_file_name}'

def read_input_line(file_path) -> Generator[str, None, None]:
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()
            
def run():
    split_number = 0
    beams = []
    for line in read_input_line(input_file):
        chars = list(line)
        if beams == []:
            for index, char in enumerate(chars):
                if char == 'S':
                    beams = ['.' for _ in range(len(chars))]
                    beams[index] = '|'
                    break
        for index, char in enumerate(chars):
            if char == '^' and beams[index] == '|':
                split_number += 1
                beams[index] = '.'
                beams[index-1] = '|'
                beams[index+1] = '|'
    print(f'Split number: {split_number}')

if __name__ == "__main__":
    run()