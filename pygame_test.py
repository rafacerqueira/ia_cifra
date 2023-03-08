import pygame
import random
import math

# definir o tamanho da janela
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

# inicializar o Pygame
pygame.init()

# criar a janela
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# definir as cores do tabuleiro
DARK_BLUE = (0, 50, 130)
WHITE = (255, 255, 255)
GREY = (153, 153, 153)
YELLOW = (255, 255, 0)
LIGHT_BLUE = (115, 169, 255)
LIGHT_DARK = (204, 209, 217)


#lista de pecas
pieces = []

# criar uma lista de 24 quadrados
squares = []

for i in range(4):
    squares.append({'color': WHITE, 'rect': pygame.Rect(0, 0, 100, 100)})
    squares.append({'color': DARK_BLUE, 'rect': pygame.Rect(0, 0, 100, 100)})
    


random.shuffle(squares)

squares.insert(3,{'color': GREY, 'rect': pygame.Rect(0, 0, 100, 100)})
squares[3]['color'] = GREY

# desenhar um tabuleiro de 5x5 com quadrados aleatórios
square_size = 100 # cada quadrado terá 100 pixels de largura e altura
square_spacing = 2
x = 50 # posição x do canto superior esquerdo do primeiro quadrado
y = 50 # posição y do canto superior esquerdo do primeiro quadrado
for row in range(3): # loop pelas 5 linhas do tabuleiro
    for col in range(3): # loop pelas 5 colunas do tabuleiro
        
        square = squares[row * 3 + col -1 ]
        # atualizar a posição do quadrado para a posição atual do loop
        square['rect'].x = x + col * (square_size + square_spacing)
        square['rect'].y = y + row * (square_size + square_spacing)
        # desenhar o quadrado atual
        pygame.draw.rect(window, square['color'], square['rect'])
        
        if row == 0:
            center_x = square['rect'].x + square_size // 2
            center_y = square['rect'].y + square_size // 2
            
            # desenhar um círculo amarelo no centro do quadrado atual
            pygame.draw.circle(window, LIGHT_DARK, (center_x, center_y), square_size // 2 - 5)
            
            circle = {'color': LIGHT_DARK, 'center': (center_x, center_y)}
            
            pieces.append(circle)
            
        if row == 2:
            center_x = square['rect'].x + square_size // 2
            center_y = square['rect'].y + square_size // 2
            
            # desenhar um círculo amarelo no centro do quadrado atual
            pygame.draw.circle(window, LIGHT_BLUE, (center_x, center_y), square_size // 2 - 5)
            
            circle = {'color': LIGHT_BLUE, 'center': (center_x, center_y)}
            
            pieces.append(circle)

# atualizar a tela
pygame.display.update()

# loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
