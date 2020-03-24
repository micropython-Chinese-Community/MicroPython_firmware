import lcdF7D as lcd
import tchF7D as ts
from time import sleep_ms

lcd.init()
lcd.set_text_color(0x00FF00)

ts.init(480, 272)


def ts_test():
    while 1:
        ts.get_state()
        if ts.touches()> 0:
            lcd.clear(0)
            print('\nTouch num: ', str(ts.touches()))
            for i in range(ts.touches()):
                print('  {} {}'.format(i+1, ts.point_info(i+1)))
                p = ts.point_info(i+1)
                x1 = max(min(p[0] - p[2]//2, 479), 0)
                x2 = max(min(p[0] + p[2]//2, 479), 0)
                y1 = max(min(p[1] - p[2]//2, 271), 0)
                y2 = max(min(p[1] + p[2]//2, 271), 0)
                lcd.set_text_color(0x00FF00)
                lcd.draw_rect(x1, y1, x2-x1, y2-y1)
        sleep_ms(100)