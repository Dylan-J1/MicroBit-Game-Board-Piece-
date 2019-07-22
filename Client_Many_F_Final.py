from microbit import *
import radio 
radio.on()
def edit_mode(incoming, sty):
    hasshonw = 0
    edit = 0
    incoming = int(incoming)
    incoming = incoming - 10
    while True:
        if edit == 0:
            while True:
                if hasshonw == 0: 
                    display.scroll('+10')
                    hasshonw = 1
                    sleep(500)
                if button_a.was_pressed():
                    incoming = incoming + 10
                    display.scroll(str(incoming))
                if button_b.was_pressed():
                    edit = edit + 1
                    save(incoming, sty)
                    hasshonw = 0
                    break
        if edit == 1:
            while True:
                if hasshonw == 0: 
                    display.scroll('-10')
                    hasshonw = 1
                    sleep(500)
                if button_a.was_pressed():
                    incoming = incoming - 10
                    display.scroll(str(incoming))
                if button_b.was_pressed():
                    edit = edit + 1
                    save(incoming, sty)
                    hasshonw = 0
                    break
        if edit == 2:
            while True:
                if hasshonw == 0: 
                    display.scroll('+1')
                    hasshonw = 1
                    sleep(500)
                if button_a.was_pressed():
                    incoming = incoming + 1
                    display.scroll(str(incoming))
                if button_b.was_pressed():
                    edit = edit + 1
                    save(incoming, sty)
                    hasshonw = 0
                    break
        if edit == 3:
            while True:
                if hasshonw == 0: 
                    display.scroll('-1')
                    hasshonw = 1
                    sleep(500)
                if button_a.was_pressed():
                    incoming = incoming - 1
                    display.scroll(str(incoming))
                if button_b.was_pressed():
                    edit = edit + 1
                    save(incoming, sty)
                    hasshonw = 0
                    break
        if edit == 4:
            while True:
                if hasshonw == 0:
                    display.scroll('done')
                if button_a.was_pressed():
                    return 
                if button_b.was_pressed():
                    edit = edit + 1
                    hasshonw = 0
                    break
        if edit == 5:
            edit = 0
def save(incoming, sty):
    radio.send('f'+str(sty)+str(incoming))
    acc('f'+str(sty)+str(incoming))
    return 
def stat():
    loc = 0
    while True:
        if button_b.was_pressed():
            loc = loc + 1
        if loc == 0: 
            display.scroll('hp')
            if button_a.is_pressed():
                return 'hp '
        if loc == 1:
            display.scroll( 'cp')
            if button_a.is_pressed():
                return 'cp '
        if loc == 2:
            display.scroll('sp')
            if button_a.is_pressed():
                return 'sp '
        if loc == 3:
            display.scroll('ep')
            if button_a.is_pressed():
                return 'ep '
        if loc == 4:
            display.scroll('gp')
            if button_a.is_pressed():
                return 'gp '
        if loc == 5:
            display.scroll('pp')
            if button_a.is_pressed():
                return 'pp '
        if loc == 6:
            display.scroll('str')
            if button_a.is_pressed():
                return 'str'
        if loc == 7:
            display.scroll('dex')
            if button_a.is_pressed():
                return 'dex'
        if loc == 8:
            display.scroll('con')
            if button_a.is_pressed():
                return 'con'
        if loc == 9:
            display.scroll('int')
            if button_a.is_pressed():
                return 'int'
        if loc == 10: 
            display.scroll('wis')
            if button_a.is_pressed():
                return 'wis'
        if loc == 11:
            display.scroll('cha')
            if button_a.is_pressed():
                return 'cha'
        if loc == 12:
            loc = 0
    return
def acc(resend):
    timer = 0
    while True:
        incoming = radio.receive()
        if incoming != 'ack' and timer == 3000:
            #display.scroll('r')
            radio.send(str(resend))
            timer = 0
        if incoming == 'ack':
            #display.scroll('a')
            timer = 0
            return
        elif timer < 3000:
            timer = timer + 1
def start(stlt):
    radio.send('start')
    acc('start')
    radio.send('f')
    acc('f')
    for stat in stlt:
        while True:
            incoming = radio.receive()
            if incoming == None:
                continue
            if incoming != None:
                radio.send('ack')
                stlt[stat] = incoming
                break
    display.scroll('done')
    return stlt
stlt = {'hp ': 0, 'cp ': 0, 'sp ': 0, 'ep ':0, 'gp ':0, 'pp ':0, 'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0,}
start(stlt)
while True:
    incoming = radio.receive()
    if button_b.was_pressed():
        sty = stat()
        edit_mode(stlt[sty],sty)
    if incoming is None:
        continue