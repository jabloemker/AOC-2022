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


def solve_prob_3():
    with open("advent/input/prob3.txt") as f:
        lines = f.readlines()
        total_priority = 0
        badge_priority = 0

        for line in lines:
            line = line[:-1]  # remove trailing \n
            rucksize = len(line)
            if rucksize % 2 != 0:
                print("bad ruck")
                return
            comp_one_ruck = line[:rucksize//2]
            comp_two_ruck = line[rucksize//2:]

            for char in comp_one_ruck:
                if char in comp_two_ruck:
                    total_priority += get_priority(char)
                    break

        for group_num in range(len(lines)//3):
            line_one = lines[3*group_num]
            line_two = lines[3*group_num + 1]
            line_three = lines[3*group_num + 2]

            for char in line_one:
                if char in line_two:
                    if char in line_three:
                        badge_priority += get_priority(char)
                        break

            # print(f"comp1 = {comp_one_ruck}\ncomp2 = {comp_two_ruck}")
        print(f"Total priority is {total_priority}")
        print(f"Badge priority is {badge_priority}")


def get_priority(char):
    priority_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26,
                     "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46, "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52}
    return priority_dict[char]


def solve_prob_4():
    with open("advent/input/prob4.txt") as f:
        lines = f.readlines()

        fully_contained_pairs = 0
        overlapping_pairs = 0

        for line in lines:
            elf_one, elf_two = line[:-1].split(',')
            elf_one_min, elf_one_max = elf_one.split('-')
            elf_two_min, elf_two_max = elf_two.split('-')

            elf_one_min = int(elf_one_min)
            elf_one_max = int(elf_one_max)
            elf_two_min = int(elf_two_min)
            elf_two_max = int(elf_two_max)
            elf_one_range = range(elf_one_min, elf_one_max+1)
            elf_two_range = range(elf_two_min, elf_two_max+1)

            range_one = elf_one_max - elf_one_min
            range_two = elf_two_max - elf_two_min

            if range_one > range_two:
                if elf_two_max <= elf_one_max and elf_two_min >= elf_one_min:
                    fully_contained_pairs += 1
                for i in elf_two_range:
                    if i in elf_one_range:
                        overlapping_pairs += 1
                        break
            else:
                if elf_two_max >= elf_one_max and elf_two_min <= elf_one_min:
                    fully_contained_pairs += 1
                for i in elf_one_range:
                    if i in elf_two_range:
                        overlapping_pairs += 1
                        break

        print(f"There are a total of {fully_contained_pairs} bad pairs")
        print(f"There are a total of {overlapping_pairs} overlapping pairs")


def solve_prob_5():
    with open("advent/input/prob5-format.txt") as f:
        lines = f.readlines()

        stack_one = ["H", "T", "Z", "D"]
        stack_two = ["Q", "R", "W", "T", "G", "C", "S"]
        stack_three = ["P", "B", "F", "Q", "N", "R", "C", "H"]
        stack_four = ['L', 'C', 'N', 'F', 'H', 'Z']
        stack_five = ['G', 'L', 'F', 'Q', 'S']
        stack_six = ['V', 'P', 'W', 'Z', 'B', 'R', 'C', 'S']
        stack_seven = ['Z', 'F', 'J']
        stack_eight = ['D', 'L', 'V', '', 'R', 'H', 'Q']
        stack_nine = ['B', 'H', 'G', 'N', 'F', 'Z', 'L', 'D']

        stack_dict = {1: stack_one, 2: stack_two, 3: stack_three, 4: stack_four,
                      5: stack_five, 6: stack_six, 7: stack_seven, 8: stack_eight, 9: stack_nine}

        for line in lines:
            vars = line.split()
            num_to_move = int(vars[1])
            stack_from = stack_dict[int(vars[3])]
            stack_to = stack_dict[int(vars[5])]
            for i in range(num_to_move):
                crate = stack_from.pop()
                stack_to.append(crate)

        final_crate_msg = ""
        for i in range(1, 10):
            final_crate_msg += stack_dict[i][-1]

        print(f"The top crates spell the message {final_crate_msg}")


def solve_prob_5b():
    with open("advent/input/prob5-format.txt") as f:
        lines = f.readlines()

        stack_one = ["H", "T", "Z", "D"]
        stack_two = ["Q", "R", "W", "T", "G", "C", "S"]
        stack_three = ["P", "B", "F", "Q", "N", "R", "C", "H"]
        stack_four = ['L', 'C', 'N', 'F', 'H', 'Z']
        stack_five = ['G', 'L', 'F', 'Q', 'S']
        stack_six = ['V', 'P', 'W', 'Z', 'B', 'R', 'C', 'S']
        stack_seven = ['Z', 'F', 'J']
        stack_eight = ['D', 'L', 'V', '', 'R', 'H', 'Q']
        stack_nine = ['B', 'H', 'G', 'N', 'F', 'Z', 'L', 'D']

        stack_dict = {1: stack_one, 2: stack_two, 3: stack_three, 4: stack_four,
                      5: stack_five, 6: stack_six, 7: stack_seven, 8: stack_eight, 9: stack_nine}

        counter = 0

        for line in lines:
            vars = line.split()
            num_to_move = int(vars[1])
            stack_from = stack_dict[int(vars[3])]
            stack_to = stack_dict[int(vars[5])]

            # print(line[:-1])
            # print(f"moving from {stack_from} to {stack_to}")

            crates_moving = stack_from[len(stack_from)-num_to_move:]
            # print(f"moving {crates_moving}")
            for crate in crates_moving:
                stack_from.reverse()
                stack_from.remove(crate)
                stack_from.reverse()
                stack_to.append(crate)
            # print(f"moved from {stack_from} to {stack_to}\n")

            # counter += 1
            # if counter > 5:
            #     break

        final_crate_msg = ""
        for i in range(1, 10):
            # if len(stack_dict[i]) > 0:
            final_crate_msg += stack_dict[i][-1]

        print(f"The top crates spell the message {final_crate_msg}")


def solve_prob_6():
    with open("advent/input/prob6.txt") as f:
        lines = f.readlines()


#### run solve_prob() ####
# solve_prob_1()
# solve_prob_2b()
# solve_prob_3()
# solve_prob_4()
# solve_prob_5()
# solve_prob_5b()
solve_prob_6()
