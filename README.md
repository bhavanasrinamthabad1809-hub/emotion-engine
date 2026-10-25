## khatak

## My Kathak Emotion Instrument
The idea

I’ve been learning Kathak for a while, and the best part is how a dancer can show a whole emotion with just her face, her hands and her feet. In Indian classical dance those emotions are called the rasas. So I thought: what if I could build a board you play with feelings?

It’s a circuit board shaped like a lotus. Each petal has a button, and each button is one emotion: love (Shringara), courage (Veera), sorrow (Karuna), joy (Hasya) and peace (Shanta). Press one, and an LED behind it lights up in that emotion’s color.

## How it works

Pressing a button tells a small chip which emotion I picked. The chip sends a color to the LEDs, and the light travels across the petals like a dancer’s footsteps. That’s tatkar, the stamping rhythm of Kathak. A knob in the corner is my laya control (tempo): turn it one way and the lights get slower (vilambit), the other way and they get faster (drut). In the middle there’s an amber LED called the diya, because every performance starts with lighting a lamp. It flickers like a real flame. Tiny bells (ghungroo) will hang from the petal tips so the board jingles when I move it.

all the switches will play music according to your mood if your mood was sad the music starts from sad takes you into happy with the different  intensity of sound thats how your mood is going to light up as well .

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
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6b01a50d-19ff-4822-878c-f377d2190a9b" />


PCB: I designed my own lotus outline, placed all the parts in a , and put the LEDs and tiny parts on the back so the front stays clean for art.
<img width="1920" height="1080" alt="Screenshot 2026-10-25 204858" src="https://github.com/user-attachments/assets/27c8b49f-3f7d-4f6d-98e6-6e50e49b9521" />



Routing: This was the hardest part. I fixed collision errors, deleted old leftover traces, and rotated the XIAO so the USB-C port sits at the edge. At my last check there were about zero connections left.
<img width="1920" height="1080" alt="Screenshot 2026-10-25 195007" src="https://github.com/user-attachments/assets/3431c28d-f90c-492d-9cb7-794e15b95ed4" />


art time :- added a dancer in middle and showed in images what are the switches did not much more cause i want the main attention to be ghungroo 
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/06eec810-ab98-4a46-891a-e49467a94269" />

flimware is still left yahh

