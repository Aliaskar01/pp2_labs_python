import pygame
import sys

pygame.init()

window = pygame.display.set_mode((800, 300))

Play = pygame.image.load(r'C:\Users\alias\OneDrive\Рабочий стол\pp1\Python\lab7\img\play.jpg')
Stop = pygame.image.load(r'C:\Users\alias\OneDrive\Рабочий стол\pp1\Python\lab7\img\stop.jpg')
Next = pygame.image.load(r'C:\Users\alias\OneDrive\Рабочий стол\pp1\Python\lab7\img\next.jpg')
Last = pygame.image.load(r'C:\Users\alias\OneDrive\Рабочий стол\pp1\Python\lab7\img\past.jpg')

Button = pygame.Surface((173, 173))

SONG_END = pygame.USEREVENT + 1

pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load(r'C:\Users\alias\OneDrive\Рабочий стол\pp1\Python\lab7\sounds\Rick Astley – Never Gonna Give You Up.mp3')
pygame.mixer.music.play()

_songs = [r'C:\Users\alias\OneDrive\Рабочий стол\pp1\Python\lab7\sounds\Rick Astley – Never Gonna Give You Up.mp3']

_currently_playing_song = None

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

def play_last_song():
    global _songs
    _songs = _songs[-1:] + _songs[:-1]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

play = False

while True:
    pos = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pos[0] < 450 and pos[0] > 300) and (pos[1] < 200 and pos[1] > 50):
                play = not play
                pygame.mixer.music.unpause()
            elif (pos[0] < 650 and pos[0] > 500) and (pos[1] < 200 and pos[1] > 50):
                play_next_song()
                play = True
            elif (pos[0] < 250 and pos[0] > 100) and (pos[1] < 200 and pos[1] > 50):
                play_last_song()
                play = True
        if event.type == SONG_END:
            play_next_song()
    
    if play:
        Button.blit(Stop, (0, 0))
    else:
        pygame.mixer.music.pause()
        Button.blit(Play, (0, 0))

    window.fill((255, 255, 255))
    window.blit(Last, (100, 50))
    window.blit(Next, (500, 50))
    window.blit(Button, (300, 50))

    pygame.display.flip()