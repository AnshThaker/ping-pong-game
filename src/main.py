import pygame
import sys


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.rotozoom(pygame.image.load('assets/graphics/paddle.png').convert_alpha(), 0, 0.5)
        self.rect = self.image.get_rect(center=(349.5, 300))
        self.velocity = 6

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.right <= 695:
            self.rect.x += self.velocity
        if keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.x -= self.velocity

    def level_up(self):
        if score == 10:
            self.velocity = 6.5
        elif score == 20:
            self.velocity = 7
        elif score == 30:
            self.velocity = 7.5
        elif score == 40:
            self.velocity = 8
        elif score == 50:
            self.velocity = 8.5
        elif score == 60:
            self.velocity = 9
        elif score == 70:
            self.velocity = 9.5
        elif score == 80:
            self.velocity = 10
        elif score == 90:
            self.velocity = 10.5
        elif score == 100:
            self.velocity = 11

    def update(self):
        self.player_input()
        self.level_up()


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.rotozoom(pygame.image.load('assets/graphics/ball.png').convert_alpha(), 0, 0.75)
        self.rect = self.image.get_rect(center=(349.5, 187))
        self.delta_x = 3
        self.delta_y = 5

    def move(self):
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y

    def border_check(self):
        if self.rect.top < 0 or self.rect.bottom > 380:
            self.delta_y *= -1
        if self.rect.left < 0 or self.rect.right > 695:
            self.delta_x *= -1

    def collision(self):
        if pygame.sprite.spritecollide(ball.sprite, player, False):
            self.delta_y *= -1

    def level_up(self):
        if score == 10:
            self.delta_x = 3.5
            self.delta_y = 5.5
            self.rect.x = 349.5
            self.rect.y = 187
        elif score == 20:
            self.delta_x = 4
            self.delta_y = 6
            self.rect.x = 349.5
            self.rect.y = 187
        elif score == 30:
            self.delta_x = 4.5
            self.delta_y = 6.5
            self.rect.x = 349.5
            self.rect.y = 187
        elif score == 40:
            self.delta_x = 5
            self.delta_y = 7
            self.rect.x = 349.5
            self.rect.y = 187
        elif score == 50:
            self.delta_x = 5.5
            self.delta_y = 7.5
            self.rect.x = 349.5
            self.rect.y = 187
        elif score == 60:
            self.delta_x = 6
            self.delta_y = 8
            self.rect.x = 349.5
            self.rect.y = 187
        elif score == 70:
            self.delta_x = 6.5
            self.delta_y = 8.5
            self.rect.x = 349.5
            self.rect.y = 187
        elif score == 80:
            self.delta_x = 7
            self.delta_y = 9
            self.rect.x = 349.5
            self.rect.y = 187
        elif score == 90:
            self.delta_x = 7.5
            self.delta_y = 9.5
            self.rect.x = 349.5
            self.rect.y = 187
        elif score == 100:
            self.delta_x = 8
            self.delta_y = 10
            self.rect.x = 349.5
            self.rect.y = 187

    def reset_speed(self):
        self.delta_x = 3
        self.delta_y = 5

    def update(self):
        self.move()
        self.border_check()
        self.collision()
        self.level_up()


def display_fps():
    fps_surface = font.render(f'{int(clock.get_fps())} fps', False, (64, 64, 64))
    fps_rectangle = fps_surface.get_rect(center=(637.5, 35))
    window.blit(fps_surface, fps_rectangle)


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rectangle = score_surface.get_rect(center=(349.5, 36))
    window.blit(score_surface, score_rectangle)
    return current_time


def lava_collide():
    if pygame.Rect.colliderect(ball.sprite.rect, lava_rectangle):
        lava_splash.play()
        return False
    else:
        return True


def display_level():
    level = 1
    if score >= 10:
        level = 2
    if score >= 20:
        level = 3
    if score >= 30:
        level = 4
    if score >= 40:
        level = 5
    if score >= 50:
        level = 6
    if score >= 60:
        level = 7
    if score >= 70:
        level = 8
    if score >= 80:
        level = 9
    if score >= 90:
        level = 10
    if score >= 100:
        level = 11
    level_surface = font.render(f'Level {level}', False, (64, 64, 64))
    level_rectangle = level_surface.get_rect(center=(61.5, 35))
    window.blit(level_surface, level_rectangle)


pygame.init()

window_height = 699
window_width = 374
window_caption = 'Ping Pong'

font = pygame.font.Font('assets/fonts/pixel_font.ttf', 50)

window = pygame.display.set_mode((window_height, window_width))
pygame.display.set_caption(window_caption)
clock = pygame.time.Clock()

game_active = False

start_time = 0

score = 0

sky_surface = pygame.image.load('assets/graphics/sky.png').convert()

lava_surface = pygame.image.load('assets/graphics/lava.png').convert()
lava_rectangle = lava_surface.get_rect(bottomleft=(0, 374))

player = pygame.sprite.GroupSingle()
player.add(Player())

ball = pygame.sprite.GroupSingle()
ball.add(Ball())

paddle_image = pygame.transform.rotozoom(pygame.image.load('assets/graphics/paddle.png').convert_alpha(), 0, 0.75)
paddle_rectangle = paddle_image.get_rect(center=(350, 225))

ball_image = pygame.transform.rotozoom(pygame.image.load('assets/graphics/ball.png').convert_alpha(), 0, 1.25)
ball_rectangle = ball_image.get_rect(center=(350, 165))

game_name = font.render('Ping Pong', False, (111, 196, 169))
game_name_rectangle = game_name.get_rect(center=(350, 65))

game_message = font.render('Press space to start', False, (111, 196, 169))
game_message_rectangle = game_message.get_rect(center=(350, 300))

lava_splash = pygame.mixer.Sound('assets/audios/lava.flac')

main_channel = pygame.mixer.Channel(0)
home_channel = pygame.mixer.Channel(1)

main_channel.play(pygame.mixer.Sound('assets/audios/game.wav'), loops=-1)
main_channel.set_volume(0.2)

home_channel.play(pygame.mixer.Sound('assets/audios/home_screen.wav'), loops=-1)
home_channel.set_volume(0.2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        window.blit(sky_surface, (0, 0))
        window.blit(lava_surface, lava_rectangle)

        player.draw(window)
        player.update()

        ball.draw(window)
        ball.update()

        display_fps()
        display_score()
        display_level()

        game_active = lava_collide()

        score = display_score()

        home_channel.pause()
        main_channel.unpause()

    else:
        score_message = font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rectangle = score_message.get_rect(center=(350, 300))

        window.fill((94, 129, 162))
        window.blit(ball_image, ball_rectangle)
        window.blit(paddle_image, paddle_rectangle)
        window.blit(game_name, game_name_rectangle)

        ball.sprite.rect.x, ball.sprite.rect.y = 349.5, 187
        player.sprite.rect.x, player.sprite.rect.y = 349.5, 280

        if score == 0:
            window.blit(game_message, game_message_rectangle)
        else:
            window.blit(score_message, score_message_rectangle)

        for ball_sprite in ball:
            ball_sprite.reset_speed()

        main_channel.pause()
        home_channel.unpause()

    pygame.display.update()
    clock.tick(60)
