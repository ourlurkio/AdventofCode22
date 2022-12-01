import os

problem_file_path = os.path.join(os.path.dirname(__file__), 'problem.txt')

elf_provision_list = []

with open(problem_file_path, 'r') as f:
    contents = f.read()
    elf_provision_list = contents.split('\n\n')
    elf_provision_list.pop(len(elf_provision_list)-1)
    f.close()

fattest_elf = 0
each_elf_calories_total = []
elf_count_list = []

for count, elf in enumerate(elf_provision_list):
    individual_item_calories = elf.split('\n')
    running_total = 0
    for item in individual_item_calories:
        running_total += int(item)
    each_elf_calories_total.append(running_total)
    elf_count_list.append(count)
    
    
    if running_total >= fattest_elf:
        fattest_elf = running_total
    else:
        pass

print(fattest_elf)

elves_sorted = sorted(zip(each_elf_calories_total, elf_count_list), reverse=True)
top_three_fat_elves = elves_sorted[:3]

top_three_fat_elves_total = 0

for elf in top_three_fat_elves:
    top_three_fat_elves_total += int(elf[0])

print(top_three_fat_elves_total)