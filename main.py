# Importar pygame
import pygame
import sys
from simulation import Simulation

# Initializer pygame
pygame.init()

# Crear pantalla de la aplicacion#
# Definir colores
GREY = (29, 29, 29)
# Definir tamaño de la pantalla
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
# Definir los FPS maximos
FPS = 12
# Deinir tamaño de las grillas
CELL_SIZE = 10
# Crear una pantalla con el tamaño antes creado
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Dar un titulo
pygame.display.set_caption("Game of Life")
# Crear un reloj para la aplicacion(Manejar el frame rate de la aplicacion)
clock = pygame.time.Clock()
simulation = Simulation(WINDOW_HEIGHT, WINDOW_WIDTH, CELL_SIZE)

# Creacion de objeto creado en grid


# Ciclo de la simulacion
while True:
	# Manejador de eventos
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			row = pos[1] // CELL_SIZE
			col = pos[0] // CELL_SIZE
			simulation.toggle_cell(row, col)
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				simulation.start()
				pygame.display.set_caption("Game of Life is Running")
			elif event.key == pygame.K_SPACE:
				simulation.stop()
				pygame.display.set_caption("Game of Life is stopped")
			elif event.key == pygame.K_f:
				FPS += 2
			elif event.key == pygame.K_s:
				if FPS > 5:
					FPS -= 2
			elif event.key == pygame.K_r:
				simulation.create_random_state()
			elif event.key == pygame.K_c:
				simulation.clear()
	
	# Actualizacion de estado
	simulation.update()
	# Dibujar la pantalla
	window.fill(GREY)
	simulation.draw(window)
	# Agregar todo antes de ocupar Update o no estara dentro de la ejecucion
	pygame.display.update()
	# Crear los fps maximos
	clock.tick(FPS)
