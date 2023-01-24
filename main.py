import numpy as np


def solve_prob_1():
    with open("advent/input/prob1.txt") as f:
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


def solve_prob_2():
    WIN_POINTS = 6
    DRAW_POINTS = 3
    LOSE_POINTS = 0

    ROCK_POINTS = 1
    PAPER_POINTS = 2
    SCISSOR_POINTS = 3

    with open("advent/input/prob2.txt") as f:
        lines = f.readlines()

        my_score = 0

        for line in lines:
            opponent_choice, my_choice = line.split()
            if my_choice == 'X':
                my_score += ROCK_POINTS
                my_choice = "A"
            elif my_choice == 'Y':
                my_score += PAPER_POINTS
                my_choice = "B"
            else:
                my_score += SCISSOR_POINTS
                my_choice = "C"

            if opponent_choice == my_choice:
                # draw
                my_score += DRAW_POINTS
            elif opponent_choice == "A":
                if my_choice == "B":
                    # paper beats rock
                    my_score += WIN_POINTS
                else:
                    my_score += LOSE_POINTS
            elif opponent_choice == "B":
                if my_choice == "C":
                    # scissor beats paper
                    my_score += WIN_POINTS
                else:
                    my_score += LOSE_POINTS
            else:
                # opponent chosses "C"
                if my_choice == "A":
                    # rock beats scissor
                    my_score += WIN_POINTS
                else:
                    my_score += LOSE_POINTS

        print(f"I should get a total of {my_score} points with this plan")


def solve_prob_2b():
    WIN_POINTS = 6
    DRAW_POINTS = 3
    LOSE_POINTS = 0

    ROCK_POINTS = 1
    PAPER_POINTS = 2
    SCISSOR_POINTS = 3

    with open("advent/input/prob2.txt") as f:
        lines = f.readlines()

        my_score = 0

        for line in lines:
            opponent_choice, my_plan = line.split()
            if my_plan == "X":
                # must lose
                if opponent_choice == "A":
                    my_score += SCISSOR_POINTS
                elif opponent_choice == "B":
                    my_score += ROCK_POINTS
                else:
                    my_score += PAPER_POINTS
                my_score += LOSE_POINTS
            elif my_plan == "Y":
                # must draw
                if opponent_choice == "A":
                    my_score += ROCK_POINTS
                elif opponent_choice == "B":
                    my_score += PAPER_POINTS
                else:
                    my_score += SCISSOR_POINTS
                my_score += DRAW_POINTS
            else:
                # must win
                if opponent_choice == "A":
                    my_score += PAPER_POINTS
                elif opponent_choice == "B":
                    my_score += SCISSOR_POINTS
                else:
                    my_score += ROCK_POINTS
                my_score += WIN_POINTS

        print(
            f"I should get a total of {my_score} points with this corrected plan")


#### run solve_prob() ####
# solve_prob_1()
solve_prob_2b()
