
import time
import serial
import pygame

from pathlib import Path
from serial import SerialException


SERIAL_PORT = "COM3"
BAUD_RATE = 115200

MUSIC_FOLDER = Path(__file__).parent / "music"

VOLUME = 0.7

EMOTION_TRACKS = {
    "LOVE": "LOVE.mp3",
    "COURAGE": "COURAGE.mp3",
    "SORROW": "SORROW.mp3",
    "JOY": "JOY.mp3",
    "PEACE": "PEACE.mp3"
}



current_emotion = None


def play_music(emotion):

    global current_emotion

    if emotion not in EMOTION_TRACKS:
        print(f"Unknown emotion: {emotion}")
        return

    if emotion == current_emotion:
        print("This emotion is already playing.")
        return

    music_file = MUSIC_FOLDER / EMOTION_TRACKS[emotion]

    if not music_file.exists():
        print(f"Music file not found: {music_file}")
        return

    try:
        pygame.mixer.music.load(str(music_file))
        pygame.mixer.music.play(-1)

        current_emotion = emotion

        print(f"Now playing: {emotion}")

    except pygame.error as error:
        print(f"Could not play music: {error}")


def stop_music():

    global current_emotion

    pygame.mixer.music.stop()
    current_emotion = None

    print("Music stopped.")


def change_volume(value):

    global VOLUME

    try:
        volume = float(value)

        if 0.0 <= volume <= 1.0:
            VOLUME = volume
            pygame.mixer.music.set_volume(VOLUME)

            print(f"Volume: {int(VOLUME * 100)}%")

        else:
            print("Volume must be between 0 and 1.")

    except ValueError:
        print("Invalid volume command.")



def handle_command(command):

    command = command.strip().upper()

    if not command:
        return

    print(f"Received: {command}")

    if command in EMOTION_TRACKS:
        play_music(command)

    elif command == "STOP":
        stop_music()

    elif command.startswith("VOLUME:"):
        value = command.split(":", 1)[1]
        change_volume(value)

    else:
        print("Command not recognised.")




def connect_esp32():

    try:
        esp32 = serial.Serial(
            port=SERIAL_PORT,
            baudrate=BAUD_RATE,
            timeout=1
        )

        
        time.sleep(2)

        esp32.reset_input_buffer()

        print("ESP32 connected successfully!")

        return esp32

    except SerialException as error:

        print(f"Could not connect to ESP32: {error}")

        return None




def main():

    print()
    print("==============================")
    print("       EMOTION ENGINE")
    print("==============================")
    print("Starting laptop music player...")

    pygame.mixer.init()
    pygame.mixer.music.set_volume(VOLUME)

    print("Music player ready.")
    print(f"Music folder: {MUSIC_FOLDER}")

    esp32 = None

    try:

        while True:

            
            if esp32 is None:

                esp32 = connect_esp32()

                if esp32 is None:
                    print("Retrying connection in 3 seconds...")
                    time.sleep(3)
                    continue

            try:

                if esp32.in_waiting > 0:

                    message = esp32.readline().decode(
                        "utf-8",
                        errors="ignore"
                    ).strip()

                    if message:
                        handle_command(message)

                time.sleep(0.01)

            except SerialException:

                print("ESP32 disconnected.")

                esp32.close()
                esp32 = None

    except KeyboardInterrupt:

        print("\nShutting down Emotion Engine...")

    finally:

        if esp32 is not None and esp32.is_open:
            esp32.close()

        pygame.mixer.music.stop()
        pygame.mixer.quit()

        print("Music player closed.")


if __name__ == "__main__":
    main()
