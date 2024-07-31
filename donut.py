import pygame
import math
import colorsys

pygame.init()

white = (255,255,255)
black = (0,0,0)
hue = 0

WIDTH = 700
HEIGHT = 700

x_start, y_start = 0,0

x_seperator = 10
y_seperator = 20

rows = HEIGHT// y_seperator
column = WIDTH // x_seperator
screen_size = rows*column

x_offset = column / 2
y_offset = rows / 2

A, B = 0, 0

theta_spacing = 10
phi_spacing = 1

chars = ".,-~:;=!*#$@"

screen = pygame.display.set_mode((WIDTH,HEIGHT))

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Donut')
font = pygame.font.SysFont('Arial', 18, bold=True)


def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, hsv2rgb(hue, 1, 1))
    display_surface.blit(text, (x_start, y_start))

run = True
while run:

    screen.fill((black))

    z = [0] * screen_size
    b = [' '] * screen_size

    for j in range(0, 628, theta_spacing):
        for i in range(0, 628, phi_spacing):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (l * h * m - t * n))
            y = int(y_offset + 20 * D * (l * h * n + t * m))
            o = int(x + column * y)  
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if rows > y and y > 0 and x > 0 and column > x and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    if y_start == rows * y_seperator - y_seperator:
        y_start = 0

    for i in range(len(b)):
        A += 0.00004
        B += 0.00002
        if i == 0 or i % column:
            text_display(b[i], x_start, y_start)
            x_start += x_seperator
        else:
            y_start += y_seperator
            x_start = 0
            text_display(b[i], x_start, y_start)
            x_start += x_seperator


    pygame.display.update()

    hue += 0.005

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False