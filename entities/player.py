
# entities/player.py 
import pygame
from config import ROJO

class Player:
    def__init__(self, x, y):
    """Constructor del jugador 
    x , y  = posicion inicial en la pantalla"""
    self.rect = pygame.Rect(x, y , 50, 50 )# tamano del jugador 
    self.velocidad = 5  # Velocidad de movimiento 

    def update(self):
        """ Se ejecuta en cada frame 
             Maneja la logica del jugador 
        """
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_a]: #Mover a la izquierda
            self.rect.x.y -= self.velocidad

        if teclas[pygame.K_d]: #Mover  a la derecha
            self.rect.x.y += self.velocidad

        if teclas[pygame.K_w]: #Mover arriba 
            self.rect.y -= self.velocidad

        if teclas[pygame.K_s]: #Mover abajo
            self.rect.y += self.velocidad


            def draw(self, pantalla):
                """Dibuja el jugador en la pantalla"""
                pygame.draw.rect(pantalla, ROJO, self.rect)
        
