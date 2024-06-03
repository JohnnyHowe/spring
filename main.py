import pygame
from spring2d import Spring2D
from vector2 import Vector2

MIN_DELTA_TIME = 0.001
MAX_DELTA_TIME = 0.1
SMOOTH_DELTATIME_LERP = 10

FONT_SIZE = 30
SCREEN_SIZE = 1000, 1000


def main():
    screen_size = Vector2(SCREEN_SIZE[0], SCREEN_SIZE[1])

    pygame.init()
    screen = pygame.display.set_mode(tuple(screen_size))
    clock = pygame.time.Clock()
    smooth_delta_time = 0

    font = pygame.font.SysFont("sans-serif", FONT_SIZE)

    spring = Spring2D()
    spring.set_target(Vector2(0.5, 0))

    while True:
        text_to_display = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                if event.key == pygame.K_r:
                    spring = Spring2D()
                    spring.set_target(Vector2(0.5, 0))
        
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            spring.set_target(Vector2(mouse_pos[0], mouse_pos[1]).component_division(screen_size / 2) - Vector2(1, 1))

        delta_time = min(max(MIN_DELTA_TIME, clock.tick() / 1000.0), MAX_DELTA_TIME)
        smooth_delta_time = lerp(smooth_delta_time, delta_time, SMOOTH_DELTATIME_LERP * delta_time)

        text_to_display.append("dt: " + str(delta_time))
        text_to_display.append("smooth dt: " + str(round(smooth_delta_time, 4)))
        text_to_display.append("smooth FPS: " + str(int(1 / smooth_delta_time)))

        spring.update(delta_time)

        screen.fill((255, 255, 255))
        # draw text
        for i in range(len(text_to_display)):
            text_surface = font.render(text_to_display[i], True, (0, 0, 0))
            screen.blit(text_surface, (0, i * FONT_SIZE))
        # draw spring
        origin = Vector2(0, 0) + screen_size / 2 
        end = spring.postion.component_multiplication(screen_size / 2) + screen_size / 2 
        target = spring.target.component_multiplication(screen_size / 2) + screen_size / 2 
        pygame.draw.line(screen, (0, 255, 0), tuple(origin), tuple(end), 3)
        pygame.draw.circle(screen, (0, 0, 0), tuple(origin), 5)
        pygame.draw.circle(screen, (0, 0, 0), tuple(end), 5)
        pygame.draw.circle(screen, (255, 0, 0), tuple(target), 5)
        pygame.display.update()


def lerp(a, b, t):
    return a * (1.0 - t) + (b * t)


if __name__ == "__main__":
    main()
