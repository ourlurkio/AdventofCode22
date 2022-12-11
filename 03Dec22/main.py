import os
import string

#set working filepath for string content
problem_file_path = os.path.join(os.path.dirname(__file__), 'problem.txt')

#create dictionaries for lower and upper case mapped to priority and then combine
lower_case_priorities = {string.ascii_lowercase[i]: i+1 for i in range(26)}
upper_case_priorities = {string.ascii_uppercase[i]: i+27 for i in range(26)}
all_priorities = {**lower_case_priorities, **upper_case_priorities}

#functions
def get_pack_contents() -> list:
    with open(problem_file_path, 'r') as f:
        all_pack_contents = f.readlines()
        for count, pack in enumerate(all_pack_contents):
            new_pack = pack.strip('\n')
            all_pack_contents[count] = new_pack
        return all_pack_contents

def split_each_pack(individual_pack: str) -> tuple:
    length = len(individual_pack) // 2
    pack_tuple = (individual_pack[:length], individual_pack[length:])
    return pack_tuple

def group_elves_contents(list_of_elves_contents: list) -> list:
    groups = [list_of_elves_contents[elf:elf + 3] for elf in range(0, len(list_of_elves_contents), 3)]
    return groups

def main():
    all_pack_contents = get_pack_contents()
    split_contents_list = []
    running_total_by_elf = 0
    running_total_badge = 0
    for pack in all_pack_contents:
        split_pack_contents = (split_each_pack(pack))
        split_contents_list.append(split_pack_contents)     
        common_items = set(split_pack_contents[0]).intersection(split_pack_contents[1])
        for item in common_items:
            running_total_by_elf += all_priorities[item]

    elf_groups = group_elves_contents(all_pack_contents)
    for group in elf_groups:
        badge_set = [set(elf) for elf in group]
        badge_item = set.intersection(*badge_set)
        for badge in badge_item:
            running_total_badge += all_priorities[badge]

    return running_total_by_elf, running_total_badge

if __name__ == '__main__':
    print(main())
