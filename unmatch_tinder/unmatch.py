from pynput.mouse import Button, Controller
import time

right_match = (413.890625, 664.578125)

middle_match = (306.796875, 674.12890625)

left_match = (208.77734375, 662.85546875)

unmatch = (1164.0390625, 784.609375)
unmatch_confirm = (767.10546875, 509.14453125)

places = list()
places.append(right_match)
places.append(middle_match)
places.append(left_match)


mouse = Controller()


# click on screen first
mouse.position = (616.48828125, 516.015625)
time.sleep(1)
mouse.click(Button.left, 1)
time.sleep(1)

for i in range(26):
    mouse.position = places[(i%3)] # three places to click
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = unmatch
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = unmatch_confirm
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)