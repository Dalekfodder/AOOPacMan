# Pacman in Python with PyGame
# https://github.com/hbokmann/Pacman
import sys

import pygame

from block import Block
from ghost import *
from pac_man import PacMan
from wall import Wall

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
    Blinky = ConcreteBlinky(width, blinky_height)

    Pinky = ConcretePinky(width, monster_height)

    Inky = ConcreteInky(inky_width, monster_height)

    Clyde = ConcreteClyde(clyde_width, monster_height)

    all_sprites_list.add(Blinky, Pinky, Inky, Clyde)
    monster_list.add(Blinky, Pinky, Inky, Clyde)


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


pac_man = PacMan()


def start_game():
    all_sprites_list = pygame.sprite.RenderPlain()
    monster_list = pygame.sprite.RenderPlain()
    pacman_collide = pygame.sprite.RenderPlain()

    walls = setup_room_one(all_sprites_list)
    gate = setup_gate(all_sprites_list)
    setup_monsters(all_sprites_list, monster_list)

    all_sprites_list.add(pac_man.get_pacman())
    pacman_collide.add(pac_man.get_pacman())

    block_list, bll = setup_blocks(all_sprites_list, walls, pacman_collide)

    score = 0

    is_game_over = False
    while not is_game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_game_over = True

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

        pac_man.update(walls, gate)

        blocks_hit_list = pygame.sprite.spritecollide(pac_man, block_list, True)

        if len(blocks_hit_list) > 0:
            score += len(blocks_hit_list)

        screen.fill(black)

        walls.draw(screen)
        gate.draw(screen)
        all_sprites_list.draw(screen)
        monster_list.draw(screen)

        if score == bll:
            is_game_over = True

        monster_hit_list = pygame.sprite.spritecollide(pac_man, monster_list, False)

        if monster_hit_list:
            game_over("Game Over", 235, all_sprites_list, block_list, monster_list, pacman_collide, walls, gate)

        pygame.display.flip()

        clock.tick(10)


def game_over(message, left, all_sprites_list, block_list, monsta_list, pacman_collide, wall_list, gate):
    pygame.font.init()
    font = pygame.font.Font("freesansbold.ttf", 24)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    del all_sprites_list
                    del block_list
                    del monsta_list
                    del pacman_collide
                    del wall_list
                    del gate
                    start_game()

        w = pygame.Surface((400, 200))  # the size of your rect
        w.set_alpha(10)  # alpha level
        w.fill((128, 128, 128))  # this fills the entire surface
        screen.blit(w, (100, 200))  # (0,0) are the top-left coordinates

        text1 = font.render(message, True, white)
        screen.blit(text1, [left, 233])

        text2 = font.render("To play again, press ENTER.", True, white)
        screen.blit(text2, [135, 303])
        text3 = font.render("To quit, press ESCAPE.", True, white)
        screen.blit(text3, [165, 333])

        pygame.display.flip()
        clock.tick(10)


start_game()

pygame.quit()
