import numpy as np

from pathlib import Path

ADVENT_INPUT_DIR = "c:/Users/johnb/Documents/GitHub/AOC-2022/advent/input/"


def solve_prob_1():
    # base_path = Path(__file__).parent
    # file_path = (base_path / "/advent/input/prob1.txt").resolve()

    # file_path = Path(__file__).parent / "/advent/input/prob1.txt"

    with open(f"{ADVENT_INPUT_DIR}prob1.txt") as f:
        lines = f.readlines()
        elf_calories = []
        most_cal = 0
        most_second_cal = 0
        most_third_cal = 0
        this_cal = 0

        # print(lines)

        for line in lines:
            if line == "\n":
                elf_calories.append(this_cal)
                # if this_cal >= most_cal:
                #     most_third_cal = most_second_cal
                #     most_second_cal = most_cal
                #     most_cal = this_cal
                this_cal = 0
            else:
                # print(f'adding {line[:-2]}')
                this_cal += int(line[:-1])
                # print(f'for a total of {this_cal}')
        elf_calories.append(this_cal)
        # if this_cal >= most_cal:
        #     most_third_cal = most_second_cal
        #     most_second_cal = most_cal
        #     most_cal = this_cal

        most_cal = np.max(elf_calories)
        elf_calories.remove(most_cal)
        most_second_cal = np.max(elf_calories)
        elf_calories.remove(most_second_cal)
        most_third_cal = np.max(elf_calories)
        elf_calories.remove(most_third_cal)

        # print('done')
        # print(elf_calories)

        print(
            f"The elf carrying the most calories is carrying {most_cal} calories!")
        print(
            f"The elf carrying the second most calories is carrying {most_second_cal} calories!")
        print(
            f"The elf carrying the third most calories is carrying {most_third_cal} calories!")
        print(
            f"For a total of {most_cal+most_second_cal+most_third_cal} calories!")


solve_prob_1()
