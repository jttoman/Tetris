import pygame
import button

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')

easy_img = pygame.image.load('easy.png').convert_alpha()
medium_img = pygame.image.load('medium.png').convert_alpha()
hard_img = pygame.image.load('hard.png').convert_alpha()
exit_img = pygame.image.load('exit.png').convert_alpha()

easy_button = button.Button(85, 50, easy_img, 0.4)
medium_button = button.Button(85, 150, medium_img, 0.4)
hard_button = button.Button(85, 250, hard_img, 0.4)
exit_button = button.Button(85, 350, exit_img, 0.4)

run = True
while run:

	screen.fill((255, 255, 255))

	if easy_button.draw(screen):
		import tetris1
	if medium_button.draw(screen):
		import tetris2
	if hard_button.draw(screen):
		import tetris3
	if exit_button.draw(screen):
		pygame.quit()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()