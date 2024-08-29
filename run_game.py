import pygame as pg

def main():
    pg.init()
    screen = pg.display.set_mode((800, 600), pg.SCALED)
    pg.display.set_caption("Poppit")

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 128))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
