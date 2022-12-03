import os

def make_elf_selection(comp_choice: str, required_result: str) -> str:
    #comp_choice rock
    if comp_choice == 'A' and required_result == 'X':
        return 'Z'
    elif comp_choice == 'A' and required_result == 'Y':
        return 'X'
    elif comp_choice == 'A' and required_result == 'Z':
        return 'Y'    
    #comp_choice paper
    elif comp_choice == 'B' and required_result == 'X':
        return 'X'
    elif comp_choice == 'B' and required_result == 'Y':
        return 'Y'
    elif comp_choice == 'B' and required_result == 'Z':
        return 'Z'    
    #comp_choice scissors
    elif comp_choice == 'C' and required_result == 'X':
        return 'Y'
    elif comp_choice == 'C' and required_result == 'Y':
        return 'Z'
    elif comp_choice == 'C' and required_result == 'Z':
        return 'X' 

def get_elf_selection_score(elf_choice: str) -> int:
    if elf_choice == 'X':
        return 1
    elif elf_choice =='Y':
        return 2
    else:
        return 3

def get_result_score(elf_choice: str, comp_choice: str) -> int:
    #elf choice rock
    if elf_choice == 'X' and comp_choice == 'B':
        return 0
    elif elf_choice == 'X' and comp_choice == 'A':
        return 3
    elif elf_choice == 'X' and comp_choice == 'C':
        return 6
    #elf choice paper
    elif elf_choice == 'Y' and comp_choice == 'C':
        return 0
    elif elf_choice == 'Y' and comp_choice == 'B':
        return 3
    elif elf_choice == 'Y' and comp_choice == 'A':
        return 6
    #elf choice scissors
    elif elf_choice == 'Z' and comp_choice == 'A':
        return 0
    elif elf_choice == 'Z' and comp_choice == 'C':
        return 3
    elif elf_choice == 'Z' and comp_choice == 'B':
        return 6

def main():
    problem_file_path = os.path.join(os.path.dirname(__file__), 'problem.txt')
    with open(problem_file_path, 'r') as f:
        game_combinations = f.readlines()
        running_score = 0
        for game in game_combinations:
            elf_selection = make_elf_selection(game[0], game[2])
            print(elf_selection)
            running_score += get_elf_selection_score(elf_selection)
            running_score += get_result_score(elf_selection, game[0])
        return running_score

if __name__ == '__main__':
    print(main())
