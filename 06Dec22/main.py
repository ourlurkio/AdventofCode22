import os
from collections import Counter

#set working filepath for string content
problem_file_path = os.path.join(os.path.dirname(__file__), 'problem.txt')

#functions
def get_signal_string(filepath: str) -> str:
    with open(filepath, 'r') as f:
        contents = f.readline()
        return contents

def check_four_characters(substring: str) -> bool:
    #return a dict with each char as a key with count as value. If len == 4, all chars unique
    frequency = Counter(substring)
    if len(frequency) == 4:
        return True
    else:
        return False

def check_fourteen_characters(substring: str) -> bool:
    #return a dict with each char as a key with count as value. If len == 4, all chars unique
    frequency = Counter(substring)
    if len(frequency) == 14:
        return True
    else:
        return False

def main():
    signal_string = get_signal_string(problem_file_path)
    counter_packet = 4
    loop = True

    #part two loop
    while loop:
        if check_four_characters(signal_string[0:4]):
            break
        else:
            signal_string = signal_string[1:]
            counter_packet += 1
    
    #part two loop
    signal_string = get_signal_string(problem_file_path)
    counter_message = 14
    while loop:
        if check_fourteen_characters(signal_string[0:14]):
            break
        else:
            signal_string = signal_string[1:]
            counter_message += 1
    
    return counter_packet, counter_message

if __name__ == '__main__':
    print(main())
