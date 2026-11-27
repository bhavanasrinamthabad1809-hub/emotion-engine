## khatak

## My Kathak Emotion Instrument
The idea

I’ve learnt Kathak for a while, and the best part is how a dancer can show a whole emotion with just her face, her hands and her feet. In Indian classical dance those emotions are called the rasas. So I thought: what if I could build a board you play with feelings?

It’s a circuit board shaped like a hexagon near to flower shape. Each petal has a button, and each button is one emotion: love (Shringara), courage (Veera), sorrow (Karuna), joy (Hasya) and peace (Shanta). Press one, and an LED behind it lights up in that emotion’s color.

you can select your mood and music plays according to that 

if you see a khatak dancer performing live it is  just completely different world if just feels like divine feminism you could  never get away the eyes 

 i wish i did not stopped  it high school took all my time. 

 photo

 <img width="736" height="1308" alt="oh how i love to dance🪷" src="https://github.com/user-attachments/assets/72d127eb-9a5b-407c-a8e1-2eb13d41a1c1" />
 

## How it works

Pressing a button tells a small chip which emotion I picked. The chip sends a color to the LEDs, and the light travels across the petals like a dancer’s footsteps. That’s tatkar, the stamping rhythm of Kathak. A knob in the corner is my laya control (tempo): turn it one way and the lights get slower (vilambit), the other way and they get faster (drut). In the middle there’s an amber LED called the diya, because every performance starts with lighting a lamp. It flickers like a real flame. 

all the switches will play music according to your mood .

so it plays music according to your mood as some one who loves muscic and dance this is game changer for me 
 

## What I’m using, and why
## Part	Why
XIAO ESP32-S3	A tiny, cheap brain with built-in USB, so I can program it with one cable
6 SK6812MINI-E LEDs	Each one can show any color, and they chain together on a single wire
12×12 mm tactile buttons with round caps	Small enough for the petals, and the caps look like the buttons in my concept
EC11 rotary encoder	The tempo knob
330 Ω resistors	Protect the first LED’s data pin
100 nF capacitors (1206)	Keep the LEDs’ power steady when they change color
1206 size parts	Big enough for me to solder by hand


## My progress

Schematic: I drew the full circuit in KiCad: five buttons, the encoder, the LED chain, the diya on its own pin, and the capacitors and resistors. ERC came back clean.
<img width="1647" height="908" alt="image" src="https://github.com/user-attachments/assets/9bb4036a-02c9-4f8a-90bf-16a521c43357" />



PCB: I designed my own hexagonal outline, placed all the parts in a , and put the LEDs and tiny parts on the back so the front stays clean for art.
<img width="748" height="760" alt="image" src="https://github.com/user-attachments/assets/5117ccfc-a117-4ecd-aeb9-5ee2733ae331" />




Routing: This was the hardest part. I fixed collision errors, deleted old leftover traces, and rotated the XIAO so the USB-C port sits at the edge. At my last check there were about zero connections left.
<img width="1920" height="1080" alt="Screenshot 2026-10-25 195007" src="https://github.com/user-attachments/assets/3431c28d-f90c-492d-9cb7-794e15b95ed4" />




## flimware 
going to use arundino ide





## BOM


| Component    | Quantity | Description         | Source                       | Price |
| ------------ | -------: | ------------------- | ---------------------------- | ----: |
| ESP32-s3     |        1 | Microcontroller     | [link](https://robu.in/product/seeed-studio-xiao-esp32s3-2-4ghz-wifi-ble-5-0/) | $12.82  |
| switches |        1 | input   | [link](https://amzn.in/d/0ap4lnfj) |$3.24 |
|  Resistor |        1 |  resistor    | [link](https://robu.in/product/330-ohm-1-4w-1206-surface-mount-chip-resistor-pack-of-100/) |$0.10 |
| capactior  |        3 | current flow | [link](https://robu.in/product/100nf-1206-surface-mount-multilayer-ceramic-capacitor-pack-of-30/) | $1.26 |
| rotatry enconder |        1 | to control the vlolume  | [link](https://robu.in/product/hongyan-ec11h-7ce20p1zy20-rotary-encoder-with-push-button-switch-vertical-plug-in-5-pin/) | $1.21 |
| PCB          |        1 | Custom-designed PCB | [link](https://zbotic.in/shop/)  | $10.21 |
| knod | 1 | cap for encoder| [Link](https://robu.in/product/potentiometer-knob-rotary-switch-cap-blue-color-pack-of-5-pcs/) | $0.31 |
| sk6812 mini-e | 1 | leds light | [Link](https://amzn.in/d/052zw8zG) | $4.31 |


## credits 

all the images credit goes to pin 
and the girls 



