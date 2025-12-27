
#entities/enemy.py
import pygame 
from config import VERDE


class Enemy:
    def __init__(self, x, y ):
        """Constructor del enemigo 
        x , y = posicion inicial en la pantalla"""
        self.rect = pygame.Rect(x, y, 50, 50) # tamano del enemigo 
        self.velocidad = 2 # Velocidad de movimiento
        self.direccion = 1 # 1 = derecha , -1 = izquierda

    def update(self):
        """Movimiento automatico del enemigo """
        self.rect.x += self.velocidad * self.direccion

        #Cambia de direccion cuando toca los bordes
        if self.rect.x <=  0 or  self.rect.x >= 750:
            self.direccion *= -1

            def draw(self, pantalla):
                """Dibuja el enemigo en la pantalla"""
                pygame.draw.rect(pantalla, VERDE, self.rect)
                