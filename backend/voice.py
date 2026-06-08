import asyncio
import edge_tts
import os

VOICE =  "en-US-ChristopherNeural"

async def generate_voice(text):

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE
    )

    await communicate.save(
        "helios_voice.mp3"
    )

def speak(text):

    asyncio.run(
        generate_voice(text)
    )

    os.system(
        "termux-media-player play helios_voice.mp3"
    )

if __name__ == "__main__":

    speak(
        "Greetings HC. HELIOS online."
    )
