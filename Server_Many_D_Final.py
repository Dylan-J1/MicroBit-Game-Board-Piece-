from microbit import *
import radio
radio.on()
def acc(incoming):
    timer = 0
    while True:
        incoming = radio.receive()
        if incoming != 'ack' and timer == 3000:
            #display.scroll('r')
            radio.send(str(incoming))
            timer = 0
            continue
        if incoming == 'ack':
            #display.scroll('a')
            timer = 0
            return
        elif timer < 3000:
            timer = timer + 1
def change(message, both):
    cwho = message[0]
    while True:
        if cwho == 'f':
            (both[2])[message[1]+message[2]+message[3]] = (int(message[4:]))
            break
        if cwho == 'e':
            (both[0])[message[1]+message[2]+message[3]] = (int(message[4:]))
            break
    switch(both, cwho)
    return both
def switch(both, cwho):
    while True:
        rep = 0
        if cwho == 'f':
            while True:
                if both[2] == Fstats1 and rep == 0:
                    #display.scroll('switch')
                    both[2] = Fstats0
                    both[3] = Fstats1
                    return both
                if both[2] == Fstats0 and rep == 0:
                    #display.scroll('switch')
                    both[2] = Fstats1
                    both[3] = Fstats0
                    return both
        if cwho == 'e':
            while True:
                if both[0] is Estats1 and rep == 0:
                    #display.scroll('switch')
                    both[0] = Estats0
                    both[1] = Estats1
                    return both
                if both[0] is Estats0 and rep == 0:
                    #display.scroll('switch')
                    both[0] = Estats1
                    both[1] = Estats0
                    return both
def who():
    while True:
        incoming = radio.receive()
        if incoming == 'f':
            radio.send('ack')
            who = 'F'
            return who 
        if incoming == 'e':
            radio.send('ack')
            who = 'E'
            return who 
        if incoming == None:
            continue
def start(both):
    radio.send('ack')
    twho = who()
    display.scroll('.')
    while True:
        if twho == 'F':
            #display.scroll('F')
            for stat in both[3]:
                #display.scroll(str(both[3][stat]))
                radio.send(str(both[3][stat]))
                acc(both[3][stat])
            return
        if twho == 'E':
            #display.scroll('E')
            for stat in Ebackup:
                radio.send(str(both[1][stat]))
                acc(both[1][stat])
            return
Estats0 = {'hp ': 0, 'cp ': 0, 'sp ': 0, 'ep ':0, 'gp ':0, 'pp ':0, 'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0,}
Estats1 = Estats0.copy()
Eworking = Estats1
Ebackup = Estats0
Fstats0 = {'hp ': 0, 'cp ': 0, 'sp ': 0, 'ep ':0, 'gp ':0, 'pp ':0, 'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0,}
Fstats1 = Fstats0.copy()
Fworking = Fstats1
Fbackup = Fstats0
both = [Eworking, Ebackup, Fworking, Fbackup]
base = ['hp ', 'cp ', 'sp ', 'ep ', 'gp ', 'pp ', 'str', 'dex', 'con', 'int', 'wis', 'cha']
check = 0 
while True:
    message = radio.receive()
    if message == 'start':
        start(both)
        message = None
        continue
    if message is not None:
        rep = 0 
        while True:
            if (message[1]+message[2]+message[3]) in base:
                radio.send('ack')
                change(message,both)
                break
            if message not in base or message == None:
                break
        #display.scroll('done')
        continue
    if button_b.was_pressed():
        display.scroll('=)')
    if message is None:
        continue