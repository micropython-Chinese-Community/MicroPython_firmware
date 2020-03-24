from time import sleep_ms
import lcdF7D as lcd
import tchF7D as ts

MAX_X = 480
MAX_Y = 272

lcd.init()

lcd.select_layer(0)
lcd.set_text_color(0xFF)
lcd.fill_rect(50, 50, 200, 100)
lcd.set_text_color(0xFF00)
lcd.fill_rect(200, 80, 200, 100)
lcd.set_text_color(0xFF0000)
lcd.fill_rect(100, 100, 200, 100)
lcd.set_text_color(0xFF00)
lcd.set_font(20)
lcd.display_string_at(0, 0, 'rect show on the screen', 0)

lcd.select_layer(1)
lcd.set_text_color(0xFF0000)
lcd.set_font(24)
lcd.display_string_at(0, 60, 'no rect show on the screen', 0)
lcd.set_text_color(0x80, 0)
lcd.fill_rect(180, 90, 30, 30)
sleep_ms(2000)

lcd.set_layer_visible(1, 0)
sleep_ms(2000)

lcd.set_layer_visible(1, 1)

for i in range(255):
    lcd.set_transparency(1, 255 - i)
    sleep_ms(10)

for i in range(220):
    lcd.set_transparency(1, i)
    sleep_ms(10)