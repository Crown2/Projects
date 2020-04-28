import pygame
import time
import random

from pygame.locals import*
from time import sleep

class Sprite():
	def __init__(self, type, x, y, w, h, model):
		self.model = model
		self.type = type 
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		
		if self.type == 'mario':
			self.prev_x = 0
			self.prev_y = 0	
			self.airtime = 0
			self.vvel = 0

		if type == 'coinblock':
			self.counter = 6; #used to keep track of coins left
			self.image = pygame.image.load("cb.png")

		if type == 'coin':
			self.glcounter = 0
			self.impacts = 0
			self.prev_x = 0
			self.prev_y = 0	
			self.vvel = -15
			self.hvel = random.randint(-18,18)
			self.arraylocation = len(self.model.sprites)
			print(self.arraylocation)


	def update(self):

		#Mario specific update
		if self.type == 'mario':
			#Camera
			self.model.scroll = self.x - 200
			
			#Gravity 
			self.vvel += 2.5
			self.y += self.vvel

			 #When mario hits the ground
			if self.y >= 425:
				self.y = 425
				self.vvel = 0
				self.airtime = 0

			#Increment jump counter
			self.airtime += 1

			#Collision Testing
			for index in range(len(self.model.sprites)):
				s = self.model.sprites[index]
				if s.type == 'brick':
					if self.collides(s):
						self.separate(s)
				if s.type == '4x1brick':
					if self.collides(s):
						self.separate(s)
				if s.type == 'coinblock':
					if self.collides(s):
						self.separate(s)
				
		#Coin Update  
		if self.type == 'coin':
			#Gravity Logic
			self.vvel += 3
			self.y += self.vvel
			self.x += self.hvel

			#Hitting the ground
			if self.y >= 469:
				self.y = 469
				if self.glcounter <= 60:
					self.hvel = self.hvel * .75
					self.vvel = self.vvel * .75
				elif self.glcounter > 30:
					self.hvel = 0
					self.vvel = 0
				self.glcounter += 1
			
			#Collision Testing for coins
			for index in range(len(self.model.sprites)):
				s = self.model.sprites[index]
				if s.type == 'brick': 
					if self.collides(s):
						self.separate(s)
				if s.type == '4x1brick': 
					if self.collides(s):
						self.separate(s)
				if s.type == 'mario': 
					if self.collides(s):
						pygame.mixer.Sound.play(coin_sfx)
						self.model.score += 1
						loc = self.arraylocation
						del self.model.sprites[self.arraylocation]
						self.model.sprites.insert(loc, Sprite("none", 0, 0, 0, 0, self.model))
						print('coin deleted successfully')
				
				

	#prev x and y updated
	def return_position(self):
		self.prev_x = self.x
		self.prev_y = self.y

	def collides(self, brick):
		if self.x + self.w <= brick.x:
			return False
		elif self.x >= brick.x + brick.w:
			return False
		elif self.y + self.h <= brick.y:
			return False
		elif self.y >= brick.y + brick.h:
			return False

		return True

	#Main collision code. Separates self(Mario) from that(brick/coinblock).
	def separate(self, that):
		#mario collison
		if self.type == 'mario':
			if self.x + self.w >= that.x and self.prev_x + self.w <= that.x: 				#Righthand Collision (Mario Perspective)
				self.x = self.prev_x
			if self.x <= that.x + that.w and self.prev_x >= that.x + that.w: 				#Lefthand Collision (Mario Perspective)
				self.x = self.prev_x
			if self.y + self.h >= that.y and self.prev_y + self.h <= that.y: 				#Top Collision (Mario Perspective)
				self.vvel = 0
				self.y = that.y - 96
				self.airtime = 0
			if self.y <= that.y + that.h and self.prev_y >= that.y + that.h: 				#Bottom Collision (Mario Perspective)
				self.y = self.prev_y
				self.vvel = 1
				self.airtime = 6
				if that.type == 'coinblock':
					that.counter -= 1
					if that.counter >= 1:
						self.model.sprites.insert(len(self.model.sprites) + 1, Sprite("coin", that.x, that.y, 51, 51, self.model)) 				#Creates a coin
						print("Coin created at array index: ", len(self.model.sprites))
						if that.counter <= 1:
							that.image = pygame.image.load("cb2.png") 						#No more coins left. Changes image source to "cb2"
		#Coin collison
		if self.type == 'coin':
			if self.impacts <= 10:
				if that.type == 'brick' or '4x1brick':
					if self.x + self.w >= that.x and self.prev_x + self.w <= that.x: 				#Righthand Collision (Coin Perspective)
						self.x = that.x - self.w
					if self.x <= that.x + that.w and self.prev_x >= that.x + that.w: 				#Lefthand Collision (Coin Perspective)
						self.x = that.x + self.w
					if self.y + self.h >= that.y and self.prev_y + self.h <= that.y: 				#Top Collision (Coin Perspective)
						if self.hvel >= 0:  #Horizontal Velocity Logic when hitting thw top of a block or 4x1.
							self.hvel = self.hvel / 2 + 1
						if self.hvel < 0: 
							self.hvel = self.hvel / 2 - 1
						self.vvel = -10
						self.y = that.y - 51
					if self.y <= that.y + that.h and self.prev_y >= that.y + that.h: 				#Bottom Collision (Coin Perspective)
						self.y = self.prev_y
						self.vvel = self.vvel - 3
			self.impacts += 1
				
	
		
class Model():
	def __init__(self): #constructor. "self" is basically the same as "this" in js.
		self.sprites = []
		self.sprites.insert(0, Sprite("4x1brick", 48, 354, 201, 51, self))
		self.sprites.insert(1, Sprite("coinblock", 150, 100, 51, 51, self))
		self.sprites.insert(2, Sprite("coinblock", 400, 300, 51, 51, self))
		self.sprites.insert(3, Sprite("4x1brick", -400, 344, 201, 51, self))
		self.sprites.insert(4, Sprite("brick", 651, 300, 51, 51, self))
		self.mario = Sprite("mario", 100, 200, 60, 95, self)
		self.sprites.insert(5, self.mario)
		self.scroll = self.mario.x
		self.score = 0


	def update(self): 
		for index in range(len(self.sprites)):
			s = self.sprites[index]
			s.update()
		
		


class View():
	def __init__(self, model):
		screen_size = (800,600)
		self.screen = pygame.display.set_mode(screen_size, 32)
		self.bg = pygame.image.load("background.png")
		self.frame = ['mario1.png', 'mario2.png', 'mario3.png', 'mario4.png', 'mario5.png'] #used for animating mario
		self.mario_image = pygame.image.load("mario1.png")
		self.brick_image = pygame.image.load("brick.png")
		self.four_brick_image = pygame.image.load("4x1brick.png")
		self.coin_image = pygame.image.load("coin.png")
		self.model = model
		self.font = pygame.font.SysFont("monospace", 16)
		self.scoretext = 'Score = '

	def update(self):   
		#self.score += 1 
		self.screen.blit(self.bg,(-900 - self.model.scroll,-150))
		self.screen.blit(self.bg,(-100 - self.model.scroll,-150))
		self.screen.blit(self.bg,(700 - self.model.scroll,-150))
		self.screen.blit(self.bg,(1500 - self.model.scroll,-150))
		self.screen.blit(self.bg,(2300 - self.model.scroll,-150))
		self.scoretext = self.font.render("Score = "+str(self.model.score), 1, (0,0,0))
		self.screen.blit(self.scoretext, (5, 10))
		
		#Mario walk animation
		for index in range(len(self.model.sprites)):
				s = self.model.sprites[index]
				if s.type == 'mario':
					if (abs(s.x) / 20) % 5 == 0:
						self.mario_image = pygame.image.load(self.frame[0])
					elif (abs(s.x) / 20) % 5 == 1:
						self.mario_image = pygame.image.load(self.frame[1])
					elif (abs(s.x) / 20) % 5 == 2:
						self.mario_image = pygame.image.load(self.frame[2])
					elif (abs(s.x) / 20) % 5 == 3:
						self.mario_image = pygame.image.load(self.frame[3])
					elif (abs(s.x) / 20) % 5 == 4:
						self.mario_image = pygame.image.load(self.frame[4])
					self.screen.blit(self.mario_image, (s.x - self.model.scroll, s.y, s.w, s.h))

				if s.type == 'brick':
					self.screen.blit(self.brick_image, (s.x - self.model.scroll, s.y))
				
				if s.type == '4x1brick':
					self.screen.blit(self.four_brick_image, (s.x - self.model.scroll, s.y))
		
				if s.type == 'coinblock':
					self.screen.blit(self.model.sprites[index].image, (s.x - self.model.scroll, s.y))
		
				if s.type == 'coin': #set coin image
					self.screen.blit(self.coin_image, (s.x - self.model.scroll, s.y))
		
		pygame.display.flip()

class Controller():
	def __init__(self, model):
		self.model = model
		self.keep_going = True

	def update(self):
		self.model.mario.return_position()

		for event in pygame.event.get():
			if event.type == QUIT:
				self.keep_going = False
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.keep_going = False
 
		keys = pygame.key.get_pressed()
		if keys[K_LEFT]:
			self.model.mario.x -= 10
		if keys[K_RIGHT]:
			self.model.mario.x += 10
		if keys[K_UP]:
			if self.model.mario.airtime <= 1:
				pygame.mixer.Sound.play(jump_sfx)
			if self.model.mario.airtime <= 5:
				self.model.mario.vvel = -25
		if keys[K_SPACE]:
			if self.model.mario.airtime <= 1:
				pygame.mixer.Sound.play(jump_sfx)
			if self.model.mario.airtime <= 5:
				self.model.mario.vvel = -25

print("Use the arrow keys to move. Press Esc to quit.")
pygame.init()
#Sounds
coin_sfx = pygame.mixer.Sound("coin_sfx.wav")
jump_sfx = pygame.mixer.Sound("jump_sfx.wav")
start_sfx = pygame.mixer.Sound("start_sfx.wav")
pygame.mixer.Sound.play(start_sfx)
#Model/View/Controller Setup
m = Model()
v = View(m)
c = Controller(m)
while c.keep_going:
	c.update()
	m.update()
	v.update()
	sleep(0.03)
print("Program Terminated")
