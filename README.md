## khatak

## My Kathak Emotion Instrument
The idea

I’ve been learning Kathak for a while, and the best part is how a dancer can show a whole emotion with just her face, her hands and her feet. In Indian classical dance those emotions are called the rasas. So I thought: what if I could build a board you play with feelings?

It’s a circuit board shaped like a lotus. Each petal has a button, and each button is one emotion: love (Shringara), courage (Veera), sorrow (Karuna), joy (Hasya) and peace (Shanta). Press one, and an LED behind it lights up in that emotion’s color.

you can select your mood and music plays according to that 

if you see a khatak dancer performing live it is  just completely different world if just feels like divine feminism you could  never get away the eyes 

 i wish i did not stopped  it high school took all my time. 

 here some photos take a moment to watch some khatak reels you will amaze by energy 
 <img width="736" height="980" alt="Dance Jewellery" src="https://github.com/user-attachments/assets/9d010258-3351-4a35-9c3c-0c51b055aaad" />

 <img width="736" height="1308" alt="oh how i love to dance🪷" src="https://github.com/user-attachments/assets/72d127eb-9a5b-407c-a8e1-2eb13d41a1c1" />
 
<img width="736" height="736" alt="Kathak🪕" src="https://github.com/user-attachments/assets/7a275e68-0901-4674-8485-02a2bb29d61a" />

## How it works

Pressing a button tells a small chip which emotion I picked. The chip sends a color to the LEDs, and the light travels across the petals like a dancer’s footsteps. That’s tatkar, the stamping rhythm of Kathak. A knob in the corner is my laya control (tempo): turn it one way and the lights get slower (vilambit), the other way and they get faster (drut). In the middle there’s an amber LED called the diya, because every performance starts with lighting a lamp. It flickers like a real flame. Tiny bells (ghungroo) will hang from the petal tips so the board jingles when I move it.

all the switches will play music according to your mood if your mood was sad the music starts from sad takes you into happy with the different  intensity of sound thats how your mood is going to light up as well .

so it plays music according to your mood as some one who loves muscic and dance this is game changer for me 
<img width="1170" height="912" alt="Gemini_Generated_Image_xlynp3xlynp3xlyn" src="https://github.com/user-attachments/assets/c69ff6a9-e973-4169-8a4b-46d757739551" />
the dance character is not like that though more art is there just a reference as how i am gonna add ghungro


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
<img width="1920" height="1080" alt="Screenshot 2026-10-26 045200" src="https://github.com/user-attachments/assets/09bd6d03-a1f0-495b-a4b9-63eb4f7d8f96" />


PCB: I designed my own lotus outline, placed all the parts in a , and put the LEDs and tiny parts on the back so the front stays clean for art.
<img width="1920" height="1080" alt="Screenshot 2026-10-25 204858" src="https://github.com/user-attachments/assets/27c8b49f-3f7d-4f6d-98e6-6e50e49b9521" />



Routing: This was the hardest part. I fixed collision errors, deleted old leftover traces, and rotated the XIAO so the USB-C port sits at the edge. At my last check there were about zero connections left.
<img width="1920" height="1080" alt="Screenshot 2026-10-25 195007" src="https://github.com/user-attachments/assets/3431c28d-f90c-492d-9cb7-794e15b95ed4" />


art time :- added a dancer in middle and showed in images what are the switches did not much more cause i want the main attention to be ghungroo 
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/06eec810-ab98-4a46-891a-e49467a94269" />

## flimware 
going to use python and kmk




## BOM

| Component    | Quantity | Description         | Source                       | Price |
| ------------ | -------: | ------------------- | ---------------------------- | ----: |
| ESP32-S3    |        1 | Microcontroller     |  https://amzn.in/d/0gQRRsHi| $14.75  |
| rotarty encoder |        1 | intensity control       | [link]https://robu.in/product/hongyan-ec11h-7ce20p1zy20-rotary-encoder-with-push-button-switch-vertical-plug-in-5-pin/ | $1.22|
| 330OHM Resistor |        1 | resistor    | https://robu.in/product/330-ohm-1-4w-1206-surface-mount-chip-resistor-pack-of-100/ |$0.10|
| switch  |        5 | User input buttons  | https://amzn.in/d/0ap4lnfj | $3.24 |
| capactior |        6 |   | https://robu.in/product/100nf-1206-surface-mount-multilayer-ceramic-capacitor-pack-of-30/ | $1.26 |
| PCB          |        1 | Custom-designed PCB | [link]https://jlcpcb.com/capabilities/pcb-capabilities| $4|
| knob  |  1 | cap |  https://robu.in/product/potentiometer-knob-rotary-switch-cap-blue-color-pack-of-5-pcs/|$0.31 |
| sk6812 | 8 | leds | [link] |   |


## credits 

all the images credit goes to pin 
and the girls 



