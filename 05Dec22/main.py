import os
from collections import defaultdict

#set working filepath for string content
problem_file_path = os.path.join(os.path.dirname(__file__), 'problem.txt')

def get_stacks_instruction(filename: str) -> tuple[dict[int, list[str]], list[list[int]]]:
    with open(filename, "r") as f:
        stacks_str, commands = f.read().split("\n\n")
    stacks_list = stacks_str.split("\n")
    stacks: dict[int, list[str]] = defaultdict(list)
    for stack in stacks_list[-2::-1]:
        for i, box in enumerate(stack[1::4]):
            if box != " ":
                stacks[i + 1].append(box)     
    instructions = []
    for command in commands.strip().split("\n"):
        _, n, _, src, _, dest = command.split()
        instructions.append(list(map(int, [n, src, dest])))

    return stacks, instructions

def move_crates_9000(number_to_move: int, start_stack: list, end_stack: list) -> tuple([list, list]):
    new_stack_start = start_stack
    new_stack_end = end_stack
    for i in reversed(range(len(start_stack) - number_to_move, len(start_stack))):
        new_stack_end.append(start_stack[i])
        new_stack_start.pop()

    return new_stack_start, new_stack_end

def part_one(stacks: dict, instructions: list):
    current_stacks = stacks
    print('Part One:')

    for instruction in instructions:
        new_crates = move_crates_9000(instruction[0], current_stacks[instruction[1]], current_stacks[instruction[2]])
        current_stacks[instruction[1]] = new_crates[0]
        current_stacks[instruction[2]] = new_crates[1]

    for stack in current_stacks:
        print(current_stacks[stack][-1])

def move_crates_9001(number_to_move: int, start_stack: list, end_stack: list) -> tuple([list, list]):
    new_stack_start = start_stack
    new_stack_end = end_stack
    counter = 0
    for i in range(len(start_stack) - number_to_move, len(start_stack)):
        new_stack_end.append(start_stack[i])
    while counter < number_to_move:
        new_stack_start.pop()
        counter += 1
    
    return new_stack_start, new_stack_end

def part_two(stacks: dict, instructions: list):
    current_stacks = stacks
    print('Part Two:')

    for instruction in instructions[0:3]:
        new_crates = move_crates_9001(instruction[0], current_stacks[instruction[1]], current_stacks[instruction[2]])
        current_stacks[instruction[1]] = new_crates[0]
        current_stacks[instruction[2]] = new_crates[1]

    for stack in current_stacks:
        print(current_stacks[stack][-1])
    


def main():
    # get_crates(problem_file_path)
    stacks, instructions = get_stacks_instruction(problem_file_path)[0], get_stacks_instruction(problem_file_path)[1]
    # part_one(stacks, instructions)

    stacks, instructions = get_stacks_instruction(problem_file_path)[0], get_stacks_instruction(problem_file_path)[1]
    part_two(stacks, instructions)
    # print(stacks[8], stacks[9])
    # print(move_crates_9001(7, stacks[8], stacks[9]))

if __name__ == '__main__':
    main()
