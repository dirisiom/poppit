import pygame as pg
import random
import bisect
from src.elements.balloon import Balloon, Color
from collections import deque, defaultdict

# define constants for num of balloons in a row (15) and num in a column (10)
ROW_LEN = 15  # num of columns
COL_LEN = 10  # num of rows


# "game board" that contains all the balloons, as well as powerups (Eventually)
def create_balloon(index):
    return Balloon(random.choice(list(Color)), index=index)


class Board:
    def __init__(self):
        self.table = []
        self.gifts = set()

        for i in range(COL_LEN):
            self.table.append([])
            for j in range(ROW_LEN):
                self.table[i].append(create_balloon((i, j)))

        for i in range(15):
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 14)
                if (x, y) not in self.gifts:
                    self.gifts.add((x, y))
                    break

    def draw(self, screen):
        gift_img = pg.image.load("src/assets/gift-box.svg")
        gift_img = pg.transform.scale(gift_img, (20, 20))

        for row in range(COL_LEN):
            for col in range(ROW_LEN):
                balloon = self.table[row][col]
                if balloon:
                    balloon.draw(screen)
                if (row, col) in self.gifts:
                    screen.blit(gift_img, (120 + col * 50 - 10, 50 + row * 50 - 10))

    def get_group(self, index: tuple):
        start = self.table[index[0]][index[1]]
        target = start.color

        result = set()

        queue = deque([start.index])
        discovered = {start.index}

        while queue:
            curr = queue.popleft()
            r, c = curr
            result.add(curr)

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = r + dr, c + dc

                # Check if the new position is within the board and not discovered
                if ((new_row, new_col) not in discovered and
                        0 <= new_row < COL_LEN and 0 <= new_col < ROW_LEN):

                    balloon = self.table[new_row][new_col]
                    if balloon and balloon.color == target:
                        queue.append(balloon.index)
                        discovered.add((new_row, new_col))

        return result

    def hit_test(self, pos):
        x, y = pos

        row_idxs = [25 + i * 50 for i in range(COL_LEN)]
        row_index = bisect.bisect_left(row_idxs, y) - 1

        if row_index < 0 or row_index >= COL_LEN:
            return None

        col_idxs = [120 - 35 / 2 + j * 50 for j in range(ROW_LEN)]
        col_index = bisect.bisect_left(col_idxs, x) - 1

        if col_index < 0 or col_index >= ROW_LEN:
            return None

        balloon = self.table[row_index][col_index]
        if balloon and balloon.rect.collidepoint(pos):
            return balloon
        return None

    def check_gifts(self):
        to_delete = set()
        for gift in self.gifts:
            if not self.table[gift[0]][gift[1]]:
                to_delete.add(gift)
        for gift in to_delete:
            self.gifts.remove(gift)


    def pop(self, group):
        for r, c in group:
            self.table[r][c] = None
        self.float(group)

    def float(self, popped):
        done = set()
        for r, c in popped:
            if c in done:
                continue
            done.add(c)

            shifts = dict()

            for i in range(COL_LEN-1, -1, -1):
                if self.table[i][c]:
                    shifts[self.table[i][c]] = 0
                else:
                    for k in shifts:
                        shifts[k] += 1


            # iterate over the dictionary in reverse order
            for curr, spaces in reversed(shifts.items()):
                old_index = curr.index
                curr.move_up(spaces)
                new_index = curr.index
                self.table[old_index[0]][old_index[1]] = None
                self.table[new_index[0]][new_index[1]] = curr

        self.check_gifts()



