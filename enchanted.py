import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("This is me praying that", 0.09),
        ("This was the very first page", 0.09),
        ("Not where the story line ends", 0.10),
        ("My thoughts will echo your name,", 0.07),
        ("until I see you again", 0.11),
        ("These are the words I held back, as I was leaving too soon", 0.10),
        ("I was enchanted to meet you.....", 0.15),
        ("Please don't be in love with someone else", 0.13),
        ("Please don't have somebody waiting on you", 0.12),
        ("Please don't be in love with someone else", 0.12),
        ("Please don't have somebody waiting on you", 0.12),

    ]

    delays = [0.3, 0.3, 0.3, 0.3, 0.4, 0.3, 0.7, 0.6, 0.07, 0.3, 5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()