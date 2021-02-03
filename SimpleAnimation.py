import pygame
pygame.init()

screen = pygame.display.set_mode((700, 1400))
color = (0, 255, 0)
line_width = 7
hcx = 50
hcy = 1150
litx, lity = 48, 1160
libx, liby = 40, 1180
lebx1, lebx2, leby1, leby2 = 50, 30, 1200, 1200
atx, aty = 45, 1170
abx1, aby1, abx2, aby2 = 65, 1160, 25, 1180
speed = 2
swap = 2
flag = True

running = True
while running:
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	pygame.draw.rect(screen, (100, 100, 100), (600, 0, 200, 1400))
	pygame.draw.rect(screen, (100, 100, 100), (0, 1200, 700, 200))
	
	pygame.draw.circle(screen, color, (hcx, hcy), 10)
	pygame.draw.line(screen, color, (litx, lity), (libx, liby), line_width)
	
	pygame.draw.line(screen, color, (libx, liby), (lebx1, leby1), line_width)
	
	pygame.draw.line(screen, color, (libx, liby), (lebx2, leby2), line_width)
	
	pygame.draw.line(screen, color, (atx, aty), (abx1, aby1), line_width)
	pygame.draw.line(screen, color, (atx, aty), (abx2, aby2), line_width)
	
	
	if hcx < 590 and flag == True:
		hcx += speed
		litx += speed
		libx += speed
		atx += speed
		abx1 += speed
		abx2 += speed

	if hcx <= 590 and lebx1 - lebx2 == 20:
		swap = 1
	if hcx < 590 and lebx2 - lebx1 == 20:
		swap = 2
	if hcx >=590:
		swap = 0	

	if swap == 1:
		lebx2 += speed*2
	if swap == 2:
		lebx1 += speed*2
	
	pygame.display.flip()

pygame.quit()
