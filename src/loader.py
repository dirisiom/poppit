import pygame, requests
import io
from src.elements.balloon import Color
from src.secrets import getS3


def build_url(file):
    return f'{getS3()}/{file}'


class Loader:
    def __init__(self):
        self.image_cache = {}
        self.balloon_map = {
            Color.red: 'red.png',
            Color.blue: 'blue.png',
            Color.green: 'green.png',
            Color.purple: 'purple.png',
            Color.pink: 'pink.png'
        }

    def load_image(self, file):
        if file in self.image_cache:
            return self.image_cache[file]
        response = requests.get(file)
        image = pygame.image.load(io.BytesIO(response.content))
        self.image_cache[file] = image
        return image

    def get_balloon(self, color):
        return self.load_image(build_url(self.balloon_map[color]))

    def get_gift(self, gift):
        return self.load_image(build_url(gift))

    def get_narrator(self):
        return self.load_image(build_url('sparty.png'))

    def get_box(self):
        return self.load_image(build_url('gift-box.svg'))