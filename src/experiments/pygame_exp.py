import pygame

def display_image(screen, image, x, y):
    sprite = pygame.sprite.Sprite()
    surface = pygame.image.load(image).convert()
    surface.set_colorkey(pygame.Color(255,0,255,0))
    sprite.image = surface.subsurface((0,0, 23, 23))
    sprite.rect = sprite.image.get_rect()
    sprite.rect.topleft = [x, y]
    return sprite


pygame.init()
pygame.display.set_caption("Katch")
sprites = pygame.sprite.Group()
screen = pygame.display.set_mode((1217, 600))
clock = pygame.time.Clock()
running = True

wizard = display_image(screen, "../../img/wizard.png", 10, 10)
player = display_image(screen, "../../img/player.png", 40, 40)

while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
           
    screen.blit(wizard.image, wizard.rect)
    screen.blit(player.image, player.rect)
    sprites.update(dt / 1000.)
    sprites.draw(screen)
    pygame.display.flip()