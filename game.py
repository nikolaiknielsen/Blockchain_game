import pygame
from menu import *
import random
import sys

class Game():
    def __init__(self):
        pygame.init()
        self.pos = (0,0)
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.mouse_click = False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1250, 725
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = 'Xolonium-Regular.ttf'
        #self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE, self.RED, self.SILVER, self.light_grey = (0, 0, 0), (255, 255, 255), (255,0,0), (128,128,128), (224,224,244)
        self.colours = [(204,0,0),(204,102,0),(204,204,0),(102,204,0)]
        self.main_menu = MainMenu(self)
        self.Tutorial = TutorialMenu(self)
        self.score = 0
        self.beginning = False
        self.curr_menu = self.main_menu
        self.first_round = False 
        self.block_1 = 0
        self.rect1_num = 3
        self.blockchain = []
        # self.remove_block_ = 0
        self.update_colour = False

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.display.fill(self.BLACK)
            self.create_blockchain()
            pygame.display.flip()
            self.draw_text('CREATION', 65, self.DISPLAY_W/2, self.DISPLAY_H/self.DISPLAY_H+50, self.RED)
            score = str(self.score)
            self.draw_text('MONEY: ' + score, 25, self.DISPLAY_W/2-525, self.DISPLAY_H-20, self.RED)
            self.window.blit(self.display, (0,0))
            # pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_click = True 
            if event.type == pygame.MOUSEBUTTONUP and self.mouse_click == True:
                self.pos = pygame.mouse.get_pos()
                self.mouse_click = False
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.mouse_click = False, False, False, False, False

    def draw_text(self, text, size, x, y, color):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
    
    def draw_blocks(self):
        self.block1 = pygame.draw.rect(self.window, self.SILVER, pygame.Rect(self.DISPLAY_W/2-100, self.DISPLAY_H/2+250, 60, 60))
        self.block2 = pygame.draw.rect(self.window, self.SILVER, pygame.Rect(self.DISPLAY_W/2-30, self.DISPLAY_H/2+250, 60, 60))
        self.block3 = pygame.draw.rect(self.window, self.SILVER, pygame.Rect(self.DISPLAY_W/2+40, self.DISPLAY_H/2+250, 60, 60))

    def update_block(self):
        if self.block_1 == 1: 
            pygame.draw.rect(self.window, self.colours[(1)], pygame.Rect(self.DISPLAY_W/2-100, self.DISPLAY_H/2+250, 60, 60))
        if self.block_1 == 2: 
            pygame.draw.rect(self.window, self.colours[(2)], pygame.Rect(self.DISPLAY_W/2-30, self.DISPLAY_H/2+250, 60, 60))
        if self.block_1 == 3: 
            pygame.draw.rect(self.window, self.colours[(0)], pygame.Rect(self.DISPLAY_W/2+40, self.DISPLAY_H/2+250, 60, 60))
        
    def choose_block(self):
        if self.first_round == False:
            if self.block1.collidepoint(self.pos):
                random_ = random.randint(1,5)
                random_gen = random.randint(1,5)
                if random_gen == random_:
                    self.update_colour = True
                    print(self.update_colour)
                    self.block_1 = 1
                    self.score += 25
                    self.blockchain.append(self.block1)
                    self.first_round = True
            if self.block2.collidepoint(self.pos):
                random_ = random.randint(1,5)
                random_gen = random.randint(1,5)
                if random_gen == random_:
                    self.update_colour
                    self.block_1 = 2
                    self.score += 35
                    self.blockchain.append(self.block2)
                    self.first_round = True
            if self.block3.collidepoint(self.pos):
                random_ = random.randint(1,4)
                random_gen = random.randint(1,4)
                if random_gen == random_:
                    self.update_colour
                    self.block_1 = 3
                    self.score += 15
                    self.blockchain.append(self.block3)
                    self.first_round = True
    
    def draw_blockchain(self, block_width, line_begin, line_end): 
        self.first_block = pygame.draw.rect(self.window, self.WHITE, pygame.Rect(30, self.DISPLAY_H/2-70, 60, 60))
        self.blockchain.append(self.first_block)
        if self.first_round == True: 
            pygame.draw.line(self.window, self.SILVER, line_begin, line_end, 5)
            pygame.draw.rect(self.window, self.WHITE, pygame.Rect(30+block_width, self.DISPLAY_H/2-70, 60, 60))
            self.update_block()

    def create_blockchain(self):
        self.draw_blocks()
        self.choose_block()
        self.draw_blockchain(75,(90,325),(150,325))