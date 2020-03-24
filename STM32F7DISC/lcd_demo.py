from time import sleep_ms, ticks_ms, ticks_diff
import pyb, machine
from random import randrange as rand

import lcdF7D as lcd
import tchF7D as ts

MAX_X = 480
MAX_Y = 272

lcd.init()

ts.init(MAX_X, MAX_Y)


def test_rand_line(n = 5000, delay = 1):
    lcd.clear()
    lcd.set_font(24)
    lcd.set_text_color(255,255,128,0)
    lcd.display_string_at(0, 0, 'line test' ,0)
    sleep_ms(1000)
    t0 = ticks_ms()
    for i in range(n):
        lcd.set_text_color(rand(0xFF), rand(0xFFFFFF))
        lcd.draw_line(rand(MAX_X), rand(MAX_Y), rand(MAX_X), rand(MAX_Y))
        sleep_ms(delay)
    return ticks_diff(ticks_ms(), t0)

def test_rand_rect(n = 2000, delay = 1):
    lcd.clear()
    lcd.set_font(24)
    lcd.set_text_color(255,255,128,0)
    lcd.display_string_at(0, 0, 'rect test' ,0)
    sleep_ms(1000)
    t0 = ticks_ms()
    for i in range(n):
        lcd.set_text_color(rand(0xFF), rand(0xFFFFFF))
        x, y = rand(MAX_X), rand(MAX_Y)
        lcd.draw_rect(x, y, rand(MAX_X - x), rand(MAX_Y - y))
        sleep_ms(delay)
    return ticks_diff(ticks_ms(), t0)

def test_rand_fillrect(n = 2000, delay = 1):
    lcd.clear()
    lcd.set_font(24)
    lcd.set_text_color(255,255,128,0)
    lcd.display_string_at(0, 0, 'fill rect test' ,0)
    sleep_ms(1000)
    t0 = ticks_ms()
    for i in range(n):
        lcd.set_text_color(rand(0xFF), rand(0xFFFFFF))
        x, y = rand(MAX_X), rand(MAX_Y)
        lcd.fill_rect(x, y, rand(MAX_X - x), rand(MAX_Y - y))
        sleep_ms(delay)
    return ticks_diff(ticks_ms(), t0)

def test_gradient(c1=0, c2=0xff, dir=0):
    def cr(x1, x2, i, n):
        return int(x1 + i*(x2-x1)/n)

    r1, g1, b1 = c1>>16, (c1>>8)%256, c1%256
    r2, g2, b2 = c2>>16, (c2>>8)%256, c2%256
    if dir == 0:
        for i in range(MAX_X):
            r = cr(r1, r2, i, MAX_X)
            g = cr(g1, g2, i, MAX_X)
            b = cr(b1, b2, i, MAX_X)
            lcd.set_text_color(r, g, b)
            lcd.draw_Vline(i, 0, MAX_Y)
    elif dir == 1:
        for i in range(MAX_Y):
            r = cr(r1, r2, i, MAX_Y)
            g = cr(g1, g2, i, MAX_Y)
            b = cr(b1, b2, i, MAX_Y)
            lcd.set_text_color(r, g, b)
            lcd.draw_Hline(0, i, MAX_X)
    elif dir == 2:
        for i in range(MAX_X):
            r = cr(r2, r1, i, MAX_X)
            g = cr(g2, g1, i, MAX_X)
            b = cr(b2, b1, i, MAX_X)
            lcd.set_text_color(r, g, b)
            lcd.draw_Vline(i, 0, MAX_Y)
    else:
        for i in range(MAX_Y):
            r = cr(r2, r1, i, MAX_Y)
            g = cr(g2, g1, i, MAX_Y)
            b = cr(b2, b1, i, MAX_Y)
            lcd.set_text_color(r, g, b)
            lcd.draw_Hline(0, i, MAX_X)

def test_rand_char(n = 2000, font = 12, delay = 1):
    if font > 20: _w, _h = 17, 24,
    elif font > 16: _w, _h = 14, 20
    elif font > 12: _w, _h = 11, 16
    elif font > 8: _w, _h = 7, 12
    else: _w, _h = 5, 8

    lcd.clear()
    lcd.set_font(_h)
    mx, my = MAX_X//_w, MAX_Y//_h

    for i in range(n):
        lcd.set_text_color(rand(0xFFFFFF))
        lcd.display_char(rand(mx) * _w, rand(my) * _h, rand(95)+32)
        sleep_ms(delay)

def test_rand_pchar(n = 2000, font = 12, delay = 5):
    if font > 20: _w, _h = 17, 24,
    elif font > 16: _w, _h = 14, 20
    elif font > 12: _w, _h = 11, 16
    elif font > 8: _w, _h = 7, 12
    else: _w, _h = 5, 8

    lcd.clear()
    lcd.set_font(_h)
    mx, my = MAX_X//_w, MAX_Y//_h
    px, py = 0, 0

    for i in range(n):
        lcd.set_text_color(rand(0xFFFFFF))
        lcd.display_char(px * _w, py * _h, rand(95)+32)
        px += 1
        if px >= mx:
            px, py = 0, py + 1
            if py >= my:
                py = my - 1
                lcd.scroll(0, -_h)
                lcd.set_text_color(0)
                lcd.fill_rect(0, MAX_Y - _h, MAX_X-1, MAX_Y-1)
        sleep_ms(delay)

def test_rand_gradient(n = 20, delay = 500):
    for i in range(n):
        test_gradient(rand(0xFFFFFF), rand(0xFFFFFF), rand(4))
        sleep_ms(delay)


def lcd_test():
    test_rand_line()
    test_rand_rect()
    test_rand_fillrect()
    test_rand_gradient()
    test_rand_char(font = 8)
    test_rand_char(font = 12)
    test_rand_char(font = 16)
    test_rand_char(font = 20)
    test_rand_char(font = 24)
    test_rand_pchar(font = rand(32))

lcd_test()
