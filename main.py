# Pacman in Python with PyGame
# https://github.com/hbokmann/Pacman

import pygame

from block import Block
from ghost import *
from pac_man import PacMan

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
purple = (255, 0, 255)
yellow = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode([606, 606])

pygame.display.set_caption('AOOPacMan')
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(black)
clock = pygame.time.Clock()

# default locations for Pacman and monsters
width = 303 - 16  # Width
pacman_height = (7 * 60) + 19  # Pacman height
monster_height = (4 * 60) + 19  # Monster height
blinky_height = (3 * 60) + 19  # Binky height
inky_width = 303 - 16 - 32  # Inky width
clyde_width = 303 + (32 - 16)  # Clyde width


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x


def setup_room_one(all_sprites_list):
    wall_list = pygame.sprite.RenderPlain()
    walls = [[0, 0, 6, 600],
             [0, 0, 600, 6],
             [0, 600, 606, 6],
             [600, 0, 6, 606],
             [300, 0, 6, 66],
             [60, 60, 186, 6],
             [360, 60, 186, 6],
             [60, 120, 66, 6],
             [60, 120, 6, 126],
             [180, 120, 246, 6],
             [300, 120, 6, 66],
             [480, 120, 66, 6],
             [540, 120, 6, 126],
             [120, 180, 126, 6],
             [120, 180, 6, 126],
             [360, 180, 126, 6],
             [480, 180, 6, 126],
             [180, 240, 6, 126],
             [180, 360, 246, 6],
             [420, 240, 6, 126],
             [240, 240, 42, 6],
             [324, 240, 42, 6],
             [240, 240, 6, 66],
             [240, 300, 126, 6],
             [360, 240, 6, 66],
             [0, 300, 66, 6],
             [540, 300, 66, 6],
             [60, 360, 66, 6],
             [60, 360, 6, 186],
             [480, 360, 66, 6],
             [540, 360, 6, 186],
             [120, 420, 366, 6],
             [120, 420, 6, 66],
             [480, 420, 6, 66],
             [180, 480, 246, 6],
             [300, 480, 6, 66],
             [120, 540, 126, 6],
             [360, 540, 126, 6]
             ]

    # Loop through the list. Create the wall, add it to the list
    for item in walls:
        wall = Wall(item[0], item[1], item[2], item[3], blue)
        wall_list.add(wall)
        all_sprites_list.add(wall)

    # return our new list
    return wall_list


def setup_gate(all_sprites_list):
    gate = pygame.sprite.RenderPlain()
    gate.add(Wall(282, 242, 42, 2, white))
    all_sprites_list.add(gate)
    return gate


def setup_monsters(all_sprites_list, monster_list):
    Blinky = Ghost("images/Blinky.png", width, blinky_height, ChaseAggresive, ScatterBottomLeft)
    monster_list.add(Blinky)
    Blinky.current_behaviour = ChaseAggresive()
    all_sprites_list.add(Blinky)

    Pinky = Ghost("images/Pinky.png", width, monster_height, ChaseAmbush, ScatterBottomRight)
    monster_list.add(Pinky)
    all_sprites_list.add(Pinky)

    Inky = Ghost("images/Inky.png", inky_width, monster_height, ChasePatrol, ScatterTopRight)
    monster_list.add(Inky)
    all_sprites_list.add(Inky)

    Clyde = Ghost("images/Clyde.png", clyde_width, monster_height, RandomChase, ScatterTopLeft)
    monster_list.add(Clyde)
    all_sprites_list.add(Clyde)

    return Blinky, Pinky, Inky, Clyde

def setup_blocks(all_sprites_list, wall_list, pacman_collide):
    block_list = pygame.sprite.RenderPlain()

    for row in range(19):
        for column in range(19):
            if (row == 7 or row == 8) and (column == 8 or column == 9 or column == 10):
                continue
            else:
                block = Block(yellow, 4, 4)

                block.rect.x = (30 * column + 6) + 26
                block.rect.y = (30 * row + 6) + 26

                b_collide = pygame.sprite.spritecollide(block, wall_list, False)
                p_collide = pygame.sprite.spritecollide(block, pacman_collide, False)
                if b_collide:
                    continue
                elif p_collide:
                    continue
                else:
                    block_list.add(block)
                    all_sprites_list.add(block)

    return block_list, len(block_list)


def start_game():
    all_sprites_list = pygame.sprite.RenderPlain()

    monster_list = pygame.sprite.RenderPlain()

    pacman_collide = pygame.sprite.RenderPlain()

    wall_list = setup_room_one(all_sprites_list)

    gate = setup_gate(all_sprites_list)

    Blinky, Pinky, Inky, Clyde = setup_monsters(all_sprites_list, monster_list)

    pac_man = PacMan("images/pacman.png", width, pacman_height)
    all_sprites_list.add(pac_man)
    pacman_collide.add(pac_man)

    block_list, bll = setup_blocks(all_sprites_list, wall_list, pacman_collide)

    score = 0

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pac_man.changespeed(-30, 0)
                if event.key == pygame.K_RIGHT:
                    pac_man.changespeed(30, 0)
                if event.key == pygame.K_UP:
                    pac_man.changespeed(0, -30)
                if event.key == pygame.K_DOWN:
                    pac_man.changespeed(0, 30)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    pac_man.changespeed(30, 0)
                if event.key == pygame.K_RIGHT:
                    pac_man.changespeed(-30, 0)
                if event.key == pygame.K_UP:
                    pac_man.changespeed(0, 30)
                if event.key == pygame.K_DOWN:
                    pac_man.changespeed(0, -30)

        pac_man.update(wall_list, gate)

        blocks_hit_list = pygame.sprite.spritecollide(pac_man, block_list, True)

        if len(blocks_hit_list) > 0:
            score += len(blocks_hit_list)

        screen.fill(black)

        wall_list.draw(screen)
        gate.draw(screen)
        all_sprites_list.draw(screen)
        monster_list.draw(screen)

        if score == bll:
            game_over = True

        monster_hit_list = pygame.sprite.spritecollide(pac_man, monster_list, False)

        if monster_hit_list:
            game_over = True

        pygame.display.flip()

        clock.tick(10)


start_game()

pygame.quit()
