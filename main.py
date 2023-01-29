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
        stack_eight = ['D', 'L', 'V', 'Z', 'R', 'H', 'Q']
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
        stack_eight = ['D', 'L', 'V', 'Z', 'R', 'H', 'Q']
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
    with open("advent/input/prob6.txt", "r") as f:
        datastream = f.readline()
        # print(datastream)

        MARKER_SIZE = 4
        MSG_MARKER_SIZE = 14
        found_packet = False
        found_msg = False

        for i in range(len(datastream)-MARKER_SIZE):
            packet = datastream[i:i+MARKER_SIZE]
            # print(packet)
            for char in packet:
                if packet.count(char) > 1:
                    break
            else:
                print(f"starting packet is {packet}")
                found_packet = True
            if found_packet:
                print(f"need to process {i+MARKER_SIZE} characters")
                break

        for i in range(len(datastream)-MSG_MARKER_SIZE):
            packet = datastream[i:i+MSG_MARKER_SIZE]
            # print(packet)
            for char in packet:
                if packet.count(char) > 1:
                    break
            else:
                print(f"message packet is {packet}")
                found_msg = True
            if found_msg:
                print(f"need to process {i+MSG_MARKER_SIZE} characters")
                break


class myPwd:
    SIZE_MAX = 100000
    TOTAL_DISK_SPACE = 70000000
    FREE_SPACE_NEEDED = 30000000
    FILE_SEP = ">"

    def __init__(self, starting_dir):
        self.starting_dir = starting_dir
        self.pwd = starting_dir
        self.dir_sizes = {starting_dir: 0}

    def change_dir(self, dir_name):
        pwd_dirs = self.pwd.split(self.FILE_SEP)
        if dir_name == "..":
            self.pwd = self.FILE_SEP.join(pwd_dirs[:-1])
        else:
            # print(pwd_dirs)
            pwd_dirs.append(dir_name)
            # print(pwd_dirs)
            self.pwd = self.FILE_SEP.join(pwd_dirs)

    def cur_dir(self):
        pwd_dirs = self.pwd.split(self.FILE_SEP)
        return pwd_dirs[-1]

    def count_file_size(self, file_size):
        pwd_dirs = self.pwd.split(self.FILE_SEP)
        for i in range(len(pwd_dirs)):
            self.dir_sizes[self.FILE_SEP.join(pwd_dirs)] += file_size
            pwd_dirs.pop()

    def add_dir(self, dir_name):
        new_path = self.pwd.split(self.FILE_SEP)
        new_path.append(dir_name)
        self.dir_sizes.update({self.FILE_SEP.join(new_path): 0})

    def deletable_files(self):
        total_to_del = 0
        for size in self.dir_sizes.values():
            if size <= self.SIZE_MAX:
                total_to_del += size
        print(f"sum of deletable dirs is {total_to_del}")

    def space_for_update(self):
        unused_space = self.TOTAL_DISK_SPACE - \
            self.dir_sizes[self.starting_dir]
        space_needed = self.FREE_SPACE_NEEDED - unused_space
        min_dir_size = self.TOTAL_DISK_SPACE
        for size in self.dir_sizes.values():
            if size > space_needed and size < min_dir_size:
                min_dir_size = size
        print(f"smallest dir size to delete - {min_dir_size}")


def solve_prob_7():
    with open("advent/input/prob7-format.txt", "r") as f:
        thisPwd = myPwd("/")
        lines = f.readlines()

        for line in lines:
            # line = line[:-1]  # trim trailing \n
            term_disp = line.split()
            if term_disp[0] == "$":
                if term_disp[1] == "cd":
                    thisPwd.change_dir(term_disp[2])
                    # print(thisPwd.pwd)
                elif term_disp[1] == "ls":
                    # list files
                    pass
                else:
                    print(f"unknown command - {term_disp[1]}")
                    return
            elif term_disp[0] == "dir":
                thisPwd.add_dir(term_disp[1])
            elif term_disp[0].isdigit():
                thisPwd.count_file_size(int(term_disp[0]))
            else:
                print(f"unknown line - {line}")
                print(f"term - {term_disp[0]} and int - {int(term_disp[0])}")

        # print(thisPwd.dir_sizes)
        thisPwd.deletable_files()
        thisPwd.space_for_update()


class treeCount:
    def __init__(self):
        self.treelist = []
        self.tree_grid = []

    def add_tree(self, tree_coord):
        if tree_coord not in self.treelist:
            self.treelist.append(tree_coord)

    def is_visible(self, tree_coord):
        y, x = tree_coord
        tree_height = self.tree_grid[y][x]

        for j in range(0, y):
            if self.tree_grid[j][x] >= tree_height:
                break
        else:
            return True

        for j in range(y+1, len(self.tree_grid)):
            if self.tree_grid[j][x] >= tree_height:
                break
        else:
            return True

        for i in range(0, x):
            if self.tree_grid[y][i] >= tree_height:
                break
        else:
            return True

        for i in range(x+1, len(self.tree_grid)):
            if self.tree_grid[y][i] >= tree_height:
                break
        else:
            return True

        return False

    def scenic_score(self, tree_coord):
        y, x = tree_coord
        tree_height = self.tree_grid[y][x]

        up_view = left_view = right_view = down_view = 0

        if y != 0:
            for j in range(y-1, -1, -1):
                if self.tree_grid[j][x] >= tree_height:
                    up_view += 1
                    break
                else:
                    # if self.tree_grid[j][x] != 0:
                    up_view += 1

        for j in range(y+1, len(self.tree_grid)):
            if self.tree_grid[j][x] >= tree_height:
                down_view += 1
                break
            else:
                # if self.tree_grid[j][x] != 0:
                down_view += 1

        if x != 0:
            for i in range(x-1, -1, -1):
                if self.tree_grid[y][i] >= tree_height:
                    left_view += 1
                    break
                else:
                    # if self.tree_grid[y][i] != 0:
                    left_view += 1

        for i in range(x+1, len(self.tree_grid)):
            if self.tree_grid[y][i] >= tree_height:
                right_view += 1
                break
            else:
                # if self.tree_grid[y][i] != 0:
                right_view += 1

        scenic_score = up_view*right_view*left_view*down_view
        # print(
        #     f"view up: {up_view} - view right: {right_view} - view left: {left_view} - view down: {down_view}")
        # print(f"scenic socre of {scenic_score}")
        return scenic_score

    def count(self):
        return(len(self.treelist))

    def print_count(self):
        print(f"Number of visible trees is {self.count()}")


def print_grid(grid):
    # taks grid as input, a list of lists i.e [[0,1,2],[3,4,5],[6,7,8]]
    for row in grid:
        print(row)


def on_edge(coord_pair, grid_size):
    a, b = coord_pair
    size_a, size_b = grid_size
    if a == 0 or b == 0:
        return True
    elif a == size_a-1 or b == size_b-1:
        return True
    else:
        return False


def solve_prob_8():
    with open("advent/input/prob8.txt", "r") as f:
        lines = f.readlines()
        trees = treeCount()
        trees.tree_grid = []
        grid_row = 0
        for line in lines:
            trees.tree_grid.append([])
            for tree in line:
                if tree != "\n":
                    trees.tree_grid[grid_row].append(int(tree))
            grid_row += 1
        # print_grid(trees.tree_grid)

        for y in range(len(trees.tree_grid)):
            for x in range(len(trees.tree_grid[y])):
                tree_coord = (y, x)
                if on_edge(tree_coord, (len(trees.tree_grid), len(trees.tree_grid[y]))):
                    trees.add_tree(tree_coord)
                if trees.is_visible(tree_coord):
                    trees.add_tree(tree_coord)

        # print(
        #      f"grid size should be {len(tree_grid)} x {len(tree_grid[0])} with a border of {2*len(tree_grid)+2*len(tree_grid[0])-4}")
        trees.print_count()

        max_scenic_score = 0
        for y in range(len(trees.tree_grid)):
            for x in range(len(trees.tree_grid[y])):
                if trees.tree_grid[y][x] != 0:
                    score = trees.scenic_score((y, x))
                    if score > max_scenic_score:
                        max_scenic_score = score

        print(f"max scenic score is {max_scenic_score}")


class PlanckRope:
    def __init__(self):
        self.tail_positions = []
        self.head_coord = (0, 0)
        self.tail_coord = (0, 0)

    def update_tail(self):
        xh, yh = self.head_coord
        xt, yt = self.tail_coord

        if (abs(xh-xt) > 1) and yt == yh:
            # y axis is lined up, x axis is off by 2
            if xh-xt < 0:
                self.tail_coord = (xt-1, yt)
            else:
                self.tail_coord = (xt+1, yt)
        elif (abs(yh-yt) > 1) and xt == xh:
            if yh-yt < 0:
                self.tail_coord = (xt, yt-1)
            else:
                self.tail_coord = (xt, yt+1)
        elif abs(yh-yt) > 0 and abs(xh-xt) > 0:
            if abs(xh-xt) > 1 and abs(yh-yt) == 1:
                if yh-yt < 0:
                    # move tail down
                    if xh-xt < 0:
                        self.tail_coord = (xt-1, yt-1)
                    else:
                        self.tail_coord = (xt+1, yt-1)
                else:
                    if xh-xt < 0:
                        self.tail_coord = (xt-1, yt+1)
                    else:
                        self.tail_coord = (xt+1, yt+1)
            elif abs(yh-yt) > 1 and abs(xh-xt) == 1:
                if xh-xt < 0:
                    if yh-yt < 0:
                        self.tail_coord = (xt-1, yt-1)
                    else:
                        self.tail_coord = (xt-1, yt+1)
                else:
                    if yh-yt < 0:
                        self.tail_coord = (xt+1, yt-1)
                    else:
                        self.tail_coord = (xt+1, yt+1)

    def record_tail_pos(self):
        if self.tail_coord not in self.tail_positions:
            self.tail_positions.append(self.tail_coord)

    def count_tail_pos(self):
        total = len(self.tail_positions)
        print(f"The tail has visited {total} total positions")

    def move_up(self):
        x, y = self.head_coord
        self.head_coord = (x, y+1)
        self.update_tail()
        self.record_tail_pos()
        self.print_coords()

    def move_down(self):
        x, y = self.head_coord
        self.head_coord = (x, y-1)
        self.update_tail()
        self.record_tail_pos()
        self.print_coords()

    def move_left(self):
        x, y = self.head_coord
        self.head_coord = (x-1, y)
        self.update_tail()
        self.record_tail_pos()
        self.print_coords()

    def move_right(self):
        x, y = self.head_coord
        self.head_coord = (x+1, y)
        self.update_tail()
        self.record_tail_pos()
        self.print_coords()

    def print_coords(self):
        print(f"head is at {self.head_coord} and tail is at {self.tail_coord}")


def solve_prob_9():
    with open("advent/input/prob9.txt", "r") as f:
        lines = f.readlines()

        rope = PlanckRope()
        rope.print_coords()

        for line in lines:
            cmd, amount = line.split()
            if cmd == "D":
                for i in range(int(amount)):
                    rope.move_down()
            elif cmd == "U":
                for i in range(int(amount)):
                    rope.move_up()
            elif cmd == "R":
                for i in range(int(amount)):
                    rope.move_right()
            elif cmd == "L":
                for i in range(int(amount)):
                    rope.move_left()
            else:
                print("unknown command")
                return

        # print(rope.tail_positions)
        rope.count_tail_pos()


#### run solve_prob() ####
# solve_prob_1()
# solve_prob_2b()
# solve_prob_3()
# solve_prob_4()
# solve_prob_5()
# solve_prob_5b()
# solve_prob_6()
# solve_prob_7()
# solve_prob_8()
solve_prob_9()
