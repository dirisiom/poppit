import pygame as pg

from src.board import Board
from src.elements.narrator import Narrator

BACKGROUND_COLOR = (50, 50, 50)


def draw_elements(screen, bg, board, sparty):
    screen.blit(bg, (0, 0))
    board.update()
    board.draw(screen)
    sparty.draw(screen)
    pg.display.flip()


def main():
    pg.init()
    screen = pg.display.set_mode((960, 800), display=0)
    pg.display.set_caption("Poppit")

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill(BACKGROUND_COLOR)

    sparty = Narrator()
    board = Board(sparty)

    draw_elements(screen, background, board, sparty)

    going = True
    while going:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False

            # click event handler that calls hit test on the board for the clicked location
            if event.type == pg.MOUSEBUTTONDOWN:
                # sparty.move_towards(pg.mouse.get_pos())
                pos = pg.mouse.get_pos()
                hit = board.hit_test(pos)
                if hit:
                    match_group = board.get_group(hit.index)
                    if len(match_group) > 1:
                        board.pop(match_group)
                        # refresh the drawing so elements are drawn in their new location
                        draw_elements(screen, background, board, sparty)


        draw_elements(screen, background, board, sparty)
    pg.quit()


if __name__ == '__main__':
    main()
