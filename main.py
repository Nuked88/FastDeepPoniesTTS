import json
import os

from api import DeepPoniesTTS, download_dependencies

speaker = 'Billie Eilish'  #@param ['Adachi Tohru', 'Apple Bloom', 'Applejack', 'Barack Obama', 'Bart Simpson', 'Billie Eilish', 'Celestia', 'Chie Satonaka', 'Cozy Glow', 'Demoman', 'Discord', 'Donald Trump', 'Engineer', 'Fluttershy', 'Franklin', 'GLaDOS', 'Granny Smith', 'Heavy', 'Homer Simpson', 'Joe Biden', 'Joe Rogan', 'Kanji Tatsumi', 'Kanye West', 'Kim Kardashian', 'Kratos', 'Luna', 'Medic', 'Michael', 'Nameless Hero', 'Nanako Dojima', 'Naoto Shirogane', 'Pinkie Pie', 'Rainbow Dash', 'Rarity', 'Rise Kujikawa', 'Ryotaro Dojima', 'Scootaloo', 'Scout', 'Sniper', 'Soldier', 'Spike', 'SpongeBob', 'Spy', 'Starlight', 'Sunset Shimmer', 'Sweetie Belle', 'Teddie', 'Trevor', 'Trixie', 'Twilight Sparkle', 'Yosuke Hanamura', 'Yukiko Amagi']
talking_speed = 1
text = '''
    The sun was just beginning to rise over the horizon, casting a golden glow across the landscape. The birds were chirping in the trees, and a gentle breeze was blowing through the fields. It was a peaceful morning, and everything seemed to be in perfect harmony.

    As I walked along the path, I felt a sense of calm wash over me. I breathed in the fresh air, letting it fill my lungs and invigorate my senses. The world seemed so alive, so full of potential and possibility.

    I had been feeling stuck lately, trapped in my own thoughts and unable to find my way forward. But being out in nature, surrounded by all this beauty, was like a balm for my soul. It reminded me that there is so much more to life than the small problems and worries that consume us.

    As I continued along the path, I came across a small stream. It was crystal clear, and I could see fish swimming in the depths below. I sat down on a nearby rock and just watched the water flow by, listening to the gentle sound of it splashing against the rocks.

    For a moment, everything else fell away. There was only me and the stream, and it was as though time had stopped. I felt at peace, connected to something greater than myself.

    Eventually, I stood up and continued on my way. But the memory of that moment stayed with me, a reminder that even in the midst of chaos and uncertainty, there is still beauty to be found.
    '''

def synth_audio():
    global tts
    try:
        tts = DeepPoniesTTS()
    except NameError:
        print()
        print("Starting initial download, this can take a minute and will only be required once ...")
        download_dependencies()
        tts = DeepPoniesTTS()

    print()
    print("Converting audio ...")
    audio = tts.synthesize(text, speaker, 1 / talking_speed)

    #save audio (numpy.ndarray) to file
    import soundfile as sf
    sf.write("audio.wav", audio, 22050)

    #play with ffplay on cmd
    #import os
    #os.system("ffplay -nodisp -autoexit audio.wav")

synth_audio()