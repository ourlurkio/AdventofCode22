import os
import re

#set working filepath for string content
problem_file_path = os.path.join(os.path.dirname(__file__), 'problem.txt')

#functions
def task_one() -> int:
    with open(problem_file_path, 'r') as f:
        all_task_range_raw = f.readlines()
        pairs_overlapping_running_total = 0
        for tasks in all_task_range_raw:
            stripped_tasks = tasks.strip('\n')
            elf_tasks = re.split(r'-|,', stripped_tasks)
            maximum = int(elf_tasks[0])
            minimum = int(elf_tasks[0])
            for elf_task in elf_tasks:
                if int(elf_task) > maximum:
                    maximum = int(elf_task)
                if int(elf_task) < minimum:
                    minimum = int(elf_task)
                        
            if int(elf_tasks[0]) == maximum and int(elf_tasks[1]) == minimum:
                pairs_overlapping_running_total += 1
            elif int(elf_tasks[0]) == minimum and int(elf_tasks[1]) == maximum:
                pairs_overlapping_running_total += 1
            elif int(elf_tasks[2]) == maximum and int(elf_tasks[3]) == minimum:
                pairs_overlapping_running_total += 1
            elif int(elf_tasks[2]) == minimum and int(elf_tasks[3]) == maximum:
                pairs_overlapping_running_total += 1
    
    return pairs_overlapping_running_total

def task_two() -> int:
    with open(problem_file_path, 'r') as f:
        all_task_range_raw = f.readlines()
        pairs_overlapping_running_total = 0
        for tasks in all_task_range_raw:
            stripped_tasks = tasks.strip('\n')
            elf_tasks = re.split(r'-|,', stripped_tasks)
            task_range_one = range(int(elf_tasks[0]), int(elf_tasks[1]) + 1)
            task_range_two = range(int(elf_tasks[2]), int(elf_tasks[3]) + 1)
            range_one = []
            range_two = []
            for item in task_range_one:
                range_one.append(int(item))
            for item in task_range_two:
                range_two.append(int(item))
            
            for task in range_one:
                if task in range_two:
                    pairs_overlapping_running_total += 1
                    break
            
        
    return pairs_overlapping_running_total

def main():
    print(task_one())
    print(task_two())

if __name__ == '__main__':
    main()
