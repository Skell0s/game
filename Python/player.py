import pygame


class Player:
    def __init__ (self, x, y):
        self.player = pygame.image.load("Ballon de plage(resized).png").convert()
        self.rect = self.player.get_rect(x=x, y=y)
        self.speed = 5
        self.velocity = [0, 0]

    def move (self):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw (self, screen):
        screen.blit(self.player, self.rect)
