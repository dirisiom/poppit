import pygame as pg
import random
import bisect
from src.elements.balloon import Balloon, Color
from collections import deque
from typing import List, Optional, Set, Tuple

ROW_LEN: int = 15  # num of columns
COL_LEN: int = 10  # num of rows

GIFT_SIZE: Tuple[int, int] = (20, 20)
BALLOON_SIZE: Tuple[int, int] = (25, 35)

X_START: int = 120
Y_START: int = 50

SPACE: int = 50


def create_balloon(index: Tuple[int, int]) -> Balloon:
    return Balloon(random.choice(list(Color)), index=index)


class Board:
    def __init__(self, narrator: pg.sprite.Sprite) -> None:
        self.table: List[List[Optional[Balloon]]] = [[None for _ in range(ROW_LEN)] for _ in range(COL_LEN)]
        self.narr: pg.sprite.Sprite = narrator
        self.popped: Optional[Set[Tuple[int, int]]] = None
        self.gifts: Set[Tuple[int, int]] = set()

        for i in range(COL_LEN):
            for j in range(ROW_LEN):
                self.table[i][j] = create_balloon((i, j))

        for _ in range(15):
            while True:
                x = random.randint(0, COL_LEN - 1)
                y = random.randint(0, ROW_LEN - 1)
                if (x, y) not in self.gifts:
                    self.gifts.add((x, y))
                    break

    def update(self) -> None:
        self.narr.update()
        if self.popped:
            self.float(self.popped)
            self.popped = None

    def draw(self, screen: pg.Surface) -> None:
        def gift_location(index: Tuple[int, int]) -> Tuple[float, float]:
            return (X_START + index[1] * SPACE - GIFT_SIZE[0] / 2,
                    Y_START + index[0] * SPACE - GIFT_SIZE[1] / 2)

        gift_img = pg.image.load("src/assets/gift-box.svg")
        gift_img = pg.transform.scale(gift_img, GIFT_SIZE)

        for row in range(COL_LEN):
            for col in range(ROW_LEN):
                balloon = self.table[row][col]
                if balloon:
                    balloon.draw(screen)
                if (row, col) in self.gifts:
                    screen.blit(gift_img, gift_location((row, col)))

    def get_group(self, index: Tuple[int, int]) -> Set[Tuple[int, int]]:
        start = self.table[index[0]][index[1]]
        if not start:
            return set()
        target = start.color

        result: Set[Tuple[int, int]] = set()
        queue: deque[Tuple[int, int]] = deque([start.index])
        discovered: Set[Tuple[int, int]] = {start.index}

        while queue:
            curr = queue.popleft()
            r, c = curr
            result.add(curr)

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = r + dr, c + dc

                if ((new_row, new_col) not in discovered and
                        0 <= new_row < COL_LEN and 0 <= new_col < ROW_LEN):

                    balloon = self.table[new_row][new_col]
                    if balloon and balloon.color == target:
                        queue.append(balloon.index)
                        discovered.add((new_row, new_col))
        return result

    def hit_test(self, pos: Tuple[int, int]) -> Optional[Balloon]:
        x, y = pos
        balloon_width, balloon_height = BALLOON_SIZE

        row_idxs = [Y_START - balloon_height / 2 + i * SPACE for i in range(COL_LEN)]
        row_index = bisect.bisect_left(row_idxs, y) - 1

        if row_index < 0 or row_index >= COL_LEN:
            return None

        col_idxs = [X_START - balloon_width / 2 + j * SPACE for j in range(ROW_LEN)]
        col_index = bisect.bisect_left(col_idxs, x) - 1

        if col_index < 0 or col_index >= ROW_LEN:
            return None

        balloon = self.table[row_index][col_index]
        if balloon and balloon.rect.collidepoint(pos):
            return balloon
        return None

    def check_gifts(self) -> None:
        to_delete: Set[Tuple[int, int]] = set()
        for gift in self.gifts:
            if not self.table[gift[0]][gift[1]]:
                to_delete.add(gift)
        for gift in to_delete:
            self.gifts.remove(gift)

    def pop(self, group: Set[Tuple[int, int]]) -> None:
        for r, c in group:
            self.table[r][c] = None
        self.popped = group

    def float(self, popped: Set[Tuple[int, int]]) -> None:
        done: Set[int] = set()
        for r, c in popped:
            if c in done:
                continue
            done.add(c)

            shifts: dict[Balloon, int] = {}

            for i in range(COL_LEN - 1, -1, -1):
                if self.table[i][c]:
                    shifts[self.table[i][c]] = 0
                else:
                    for k in shifts:
                        shifts[k] += 1

            for curr, spaces in reversed(shifts.items()):
                old_index = curr.index
                curr.move_up(spaces)
                new_index = curr.index
                self.table[old_index[0]][old_index[1]] = None
                self.table[new_index[0]][new_index[1]] = curr

        self.check_gifts()