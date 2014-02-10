#!/usr/bin/env python3

import pygame.mixer

sounds = pygame.mixer
sounds.init()

def wait_finish(channel):
    while channel.get_busy():
        pass


s = sounds.Sound('heartbeat.wav')
s.play()
s2 = sounds.Sound('buzz.wav')
s2.play()
s3 = sounds.Sound('ohno.wav')
s3.play()
s4 = sounds.Sound('carhorn.wav')
channel = s4.play()

wait_finish(channel)