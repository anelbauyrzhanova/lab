import pygame

pygame.init()

SONG_END = pygame.USEREVENT +  1
pygame.mixer.music.set_endevent(SONG_END)
song1 = r'C:\Users\Anel\Desktop\pp2\LAB7\Ex3 - Music Player\songs for code\I Miss You, Im Sorryy.mp3'
song2 = r'C:\Users\Anel\Desktop\pp2\LAB7\Ex3 - Music Player\songs for code\Angel'
song3 = r'C:\Users\Anel\Desktop\pp2\LAB7\Ex3 - Music Player\songs for code\Summertime Sadness'
song4 = r'C:\Users\Anel\Desktop\pp2\LAB7\Ex3 - Music Player\songs for code\Young and Beautifull'
songs = [song1, song2, song3, song4]

curently = None
next_song = 0
clock = pygame.time.Clock()


def play_music(next_song):
    global curently
    if next_song >= len(songs):
        next_song = 0
    elif next_song < -len(songs):
        next_song = len(songs) - 1
    while next_song == curently:
        next_song += 1
    curently = next_song
    pygame.mixer.music.load(songs[next_song])
    pygame.mixer.music.play()

play_music(next_song)

flag_pause = True
screen = pygame.display.set_mode((100, 100))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                next_song -= 1
                play_music(next_song)
            elif event.key == pygame.K_RIGHT:
                next_song += 1
                play_music(next_song)
            elif event.key == pygame.K_SPACE and flag_pause == True:
                flag_pause = False
                pygame.mixer.music.pause()
            elif event.key == pygame.K_SPACE and flag_pause == False:
                flag_pause = True
                pygame.mixer.music.unpause()

    pygame.display.flip()
    clock.tick(60)