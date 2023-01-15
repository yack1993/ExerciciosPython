#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# Inicializando o mixer PyGame
import pygame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()