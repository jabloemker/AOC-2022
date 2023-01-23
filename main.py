import numpy as np

from pathlib import Path

ADVENT_INPUT_DIR = "c:/Users/johnb/Documents/GitHub/AOC-2022/advent/input/"


def solve_prob_1():
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
                this_cal = 0
            else:
                this_cal += int(line[:-1])
        elf_calories.append(this_cal)

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
