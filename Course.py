import pygame
import gym
from time import sleep
class ObstacleCourse(gym.Env):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Obstacle Course RL Algorithm")
        self.board = pygame.display.set_mode((500, 500))
