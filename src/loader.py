import pygame, requests
import io

class Loader():
    def __init__(self):
        self.image_cache = {}

    def load_image(self, url):
        if url in self.image_cache:
            return self.image_cache[url]
        response = requests.get(url)
        image = pygame.image.load(io.BytesIO(response.content))
        self.image_cache[url] = image
        return image