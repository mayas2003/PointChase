import pygame, random
from pygame.locals import *

#initiation
pygame.init()


#screen
bgcolor = (255,255,255)
window_length = 750
window_height = 750
screen = pygame.display.set_mode((window_length, window_height))
pygame.display.set_caption("Total points : 0")
screen.fill(bgcolor)


#colours
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Black = (0, 0, 0)
White = (255, 255, 255)
Grey = (100,100,100)

#loading icon of superhero
hero_image = pygame.image.load("superhero_64.png")
hero_rect = hero_image.get_rect()
hero_rect.centerx = window_length//2
hero_rect.centery = window_height//2


#loading icon of skull
skull_image = pygame.image.load("skull_48.png")
skull_rect = skull_image.get_rect()
skull_rect.centerx = random.randint(48, window_length - 60)
skull_rect.centery = random.randint(48, window_height)





#loading icon of shield
shield_image = pygame.image.load("shield_32.png")
shield_rect = shield_image.get_rect()
shield_rect.centerx = random.randint(32, window_length - 32)
shield_rect.centery = random.randint(32, window_height-32)


#loading sound effects
sound_point = pygame.mixer.Sound('sound1.wav')
sound_end = pygame.mixer.Sound('Sound_end.wav')


#loading texts
end_font = pygame.font.Font("SeratUltra-1GE24.ttf",32)
end_text = end_font.render("Game End!!", True , Red)
end_text_rect = end_text.get_rect()
end_text_rect.center = (window_length//2, window_height//2)


#fixed speed
velocity = 5
speed_level1 = [3,3]
speed_level2 = [6,4.5]
speed_level3_a = [2.9,3.1]
speed_level3_b = [3.2,-3.5]
speed_level4_a = [2.9,3.1]
speed_level4_b = [3.2,-3.5]
speed_level4_c = [4,4]

#clock
fps = 90
clock = pygame.time.Clock()

points = 0
c = 0
d = 0

#game loop
running = True
while running:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
                running = False
    


    

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_j]) and hero_rect.left > 0 :
            hero_rect.x -= velocity
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_l]) and hero_rect.right < window_length :
            hero_rect.x += velocity
    elif (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_i]) and hero_rect.top > 0:
            hero_rect.y -= velocity
    elif (keys[pygame.K_DOWN] or keys[pygame.K_s] or keys[pygame.K_k]) and hero_rect.bottom < window_height :
            hero_rect.y += velocity


    #avoiding duplication
    screen.fill(bgcolor)

    #level-1
    if points < 12 :
        #blitting skull icon
        screen.blit(skull_image, skull_rect)
        pygame.draw.rect(screen, bgcolor, skull_rect, 1)

        #moving skull 
        skull_rect = skull_rect.move(speed_level1)
        if skull_rect.left < 0 or skull_rect.right > window_length:
            speed_level1[0] = -speed_level1[0]
        if skull_rect.top < 0 or skull_rect.bottom > window_height:
            speed_level1[1] = -speed_level1[1]


    #level 2
    if points >= 12 and points < 26 :
        bgcolor = (50,50,50)
        #blitting skull icon
        screen.blit(skull_image, skull_rect)
        pygame.draw.rect(screen, bgcolor, skull_rect, 1)

        #moving skull 
        skull_rect = skull_rect.move(speed_level2)
        if skull_rect.left < 0 or skull_rect.right > window_length:
            speed_level2[0] = -speed_level2[0]
        if skull_rect.top < 0 or skull_rect.bottom > window_height:
            speed_level2[1] = -speed_level2[1]

    #level 3
    if points == 26 :
        c+=1
        if c == 1 :
            #loading other icon of skull
            print("a")
            skull_other_image = pygame.image.load("skull_48.png")
            skull_other_rect = skull_other_image.get_rect()
            skull_other_rect.centerx = random.randint(48, window_length - 60)
            skull_other_rect.centery = random.randint(48, window_height)

    if points >= 26 and points < 42 :
        bgcolor = (110,110,110)
        #blitting skull icon
        screen.blit(skull_image, skull_rect)
        pygame.draw.rect(screen, bgcolor, skull_rect, 1)
        
        skull_rect = skull_rect.move(speed_level3_a)
        if skull_rect.left < 0 or skull_rect.right > window_length:
            speed_level3_a[0] = -speed_level3_a[0]
        if skull_rect.top < 0 or skull_rect.bottom > window_height:
            speed_level3_a[1] = -speed_level3_a[1]



        #blitting other skull icon
        screen.blit(skull_other_image, skull_other_rect)
        pygame.draw.rect(screen, bgcolor, skull_rect, 1)

        skull_other_rect = skull_other_rect.move(speed_level3_b)
        if skull_other_rect.left < 0 or skull_other_rect.right > window_length:
            speed_level3_b[0] = -speed_level3_b[0]
        if skull_other_rect.top < 0 or skull_other_rect.bottom > window_height:
            speed_level3_b[1] = -speed_level3_b[1]


    #level 4
    if points == 42 :
        d+=1
        if d == 1 :
            #loading 3rd icon of skull
            skull_image3 = pygame.image.load("skull_48.png")
            skull_rect3 = skull_image3.get_rect()
            skull_rect3.x = 32
            skull_rect3.y = 32

    if points >= 42 and points < 56 :
        bgcolor = (160,160,160)
        #blitting skull icon
        screen.blit(skull_image, skull_rect)
        pygame.draw.rect(screen, bgcolor, skull_rect, 1)
        
        skull_rect = skull_rect.move(speed_level4_a)
        if skull_rect.left < 0 or skull_rect.right > window_length:
            speed_level4_a[0] = -speed_level4_a[0]
        if skull_rect.top < 0 or skull_rect.bottom > window_height:
            speed_level4_a[1] = -speed_level4_a[1]

        screen.blit(skull_other_image, skull_other_rect)
        pygame.draw.rect(screen, bgcolor, skull_rect, 1)

        skull_other_rect = skull_other_rect.move(speed_level3_b)
        if skull_other_rect.left < 0 or skull_other_rect.right > window_length:
            speed_level3_b[0] = -speed_level3_b[0]
        if skull_other_rect.top < 0 or skull_other_rect.bottom > window_height:
            speed_level3_b[1] = -speed_level3_b[1]


        #blitting skull icon
        screen.blit(skull_image3, skull_rect3)
        pygame.draw.rect(screen, bgcolor, skull_rect3, 1)
        
        skull_rect3 = skull_rect3.move(speed_level4_c)
        if skull_rect3.left < 0 or skull_rect3.right > window_length:
            speed_level4_c[0] = -speed_level4_c[0]
        if skull_rect3.top < 0 or skull_rect3.bottom > window_height:
            speed_level4_c[1] = -speed_level4_c[1]

    
    #level 5 
     


    if hero_rect.colliderect(shield_rect) :
        points +=1
        sound_point.play()
        shield_rect.centerx = random.randint(32, window_length - 32)
        shield_rect.centery = random.randint(32, window_height-32)
        pygame.display.set_caption("Total points : " + str(points))

    if hero_rect.colliderect(skull_rect) :
        sound_end.play()
        pygame.time.delay(2000)
        screen.blit(end_text, end_text_rect)
        running = False

    if points > 26 :
        if hero_rect.colliderect(skull_other_rect):
            sound_end.play()
            pygame.time.delay(2000)
            screen.blit(end_text, end_text_rect)
            running = False


    

    #blitting the hero icon
    screen.blit(hero_image, hero_rect)
    pygame.draw.rect(screen, bgcolor, hero_rect,1)

    


    #blitting shield icon
    screen.blit(shield_image, shield_rect)
    pygame.draw.rect(screen, bgcolor, shield_rect,1)

    pygame.display.update()
    
    clock.tick(fps)

print()
print("Game End")
print()
pygame.quit()