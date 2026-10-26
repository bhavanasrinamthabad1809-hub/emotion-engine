import time, random, board, neopixel, keypad, rotaryio

strip = neopixel.NeoPixel(board.D9, 5, brightness=0.25, auto_write=False, pixel_order=neopixel.GRB)
diya  = neopixel.NeoPixel(board.D10, 1, brightness=0.25, auto_write=False, pixel_order=neopixel.GRB)
keys  = keypad.Keys((board.D0, board.D1, board.D2, board.D3, board.D4),
                    value_when_pressed=False, pull=True)
knob  = rotaryio.IncrementalEncoder(board.D5, board.D8)

RASA = [(255, 20, 120),   # 1 Shringara, love
        (255, 40, 0),     # 2 Veera, courage
        (0, 60, 255),     # 3 Karuna, sorrow
        (255, 200, 0),    # 4 Hasya, joy
        (0, 255, 100)]    # 5 Shanta, peace
AMBER = (255, 115, 0)

tempo = 0.15            # seconds per step, smaller is faster
last_pos = knob.position
active = None
pos = 0
t_step = t_diya = time.monotonic()
flare_until = 0

while True:
    now = time.monotonic()

    event = keys.events.get()          # debounced button presses
    if event and event.pressed:
        active = event.key_number
        pos = 0
        flare_until = now + 0.3

    change = knob.position - last_pos  # tempo knob
    if change:
        tempo = min(0.5, max(0.04, tempo - 0.01 * change))
        last_pos = knob.position

    if active is not None and now - t_step > tempo:   # tatkar chase
        t_step = now
        strip.fill((0, 0, 0))
        strip[pos] = RASA[active]
        strip.show()
        pos = (pos + 1) % 5

    if now - t_diya > 0.07:                           # diya flicker
        t_diya = now
        if now < flare_until and active is not None:
            diya[0] = RASA[active]
        else:
            f = random.uniform(0.3, 1.0)
            diya[0] = (int(AMBER[0] * f), int(AMBER[1] * f), 0)
        diya.show()
