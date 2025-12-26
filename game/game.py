
# Archivo de mecanica del juego 
import pygame
import sys
from config import ANCHO, ALTO, FPS, NEGRO
from entities.player import Player 
from entities.enemy import Enemy
 
class Game:   
    def __init__(self):
        pygame .init()
        self.pantalla = pygame.display.set_model((ANCHO, ALTO))
        pygame.display.set_caption("Stranger Things - Upside Down")
        self.reloj = pygame.time.Clock()
        self.running = True

        
