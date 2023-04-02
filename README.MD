# Fast DeepPoniesTTS

This is a fork of the [DeepPoniesFrontend](https://github.com/dunky11/deep-ponies-frontend) project by [dunky11](https://github.com/dunky11) that greatly improves its performance by parallelizing the text-to-speech conversion process and adding GPU support.

The original project allows you to generate an audio file from text using a multispeaker TTS model. The available voices are: Adachi Tohru, Apple Bloom, Applejack, Barack Obama, Bart Simpson, Billie Eilish, Celestia, Chie Satonaka, Cozy Glow, Demoman, Discord, Donald Trump, Engineer, Fluttershy, Franklin, GLaDOS, Granny Smith, Heavy, Homer Simpson, Joe Biden, Joe Rogan, Kanji Tatsumi, Kanye West, Kim Kardashian, Kratos, Luna, Medic, Michael, Nameless Hero, Nanako Dojima, Naoto Shirogane, Pinkie Pie, Rainbow Dash, Rarity, Rise Kujikawa, Ryotaro Dojima, Scootaloo, Scout, Sniper, Soldier, Spike, SpongeBob, Spy, Starlight, Sunset Shimmer, Sweetie Belle, Teddie, Trevor, Trixie, Twilight Sparkle, and Yosuke Hanamura.

My fork greatly speeds up the text-to-speech conversion process by parallelizing the work in threads. Furthermore, it adds GPU support, resulting in incredibly fast processing times for longer texts. For example:
| Text Length | Type | Original | FastMod |
| --- | --- | --- | --- |
| 1416 | CPU | 24 sec | 14 sec |
| 1416 | GPU | Not supported | 3.72 sec |


To take advantage of these improvements, simply run the main.py file, which will convert your text into an audio file using the selected speaker and playback speed.

## Example Usage

To use this project, simply follow these steps:

1. If you are on Linux, please run `pip install pynini==2.1.4` manually. On Windows, it is recommended to use a Conda environment; otherwise, it may be impossible to install Pynini. In this case, you will need to run `conda install -c conda-forge pynini` manually. Finally, on both systems, you can install the required dependencies by running `pip install -r requirements.txt`

2. Edit and run the `main.py` file.

3. Wait for the audio file to be generated.

4. Enjoy your audio file!

## Credits

This project is based on the [DeepPoniesTTS](https://github.com/dunky11/deep-ponies-frontend) project by [dunky11](https://github.com/dunky11).It is also based on [this notebook](https://colab.research.google.com/drive/1zh6w_TpEAyr_UIojiLmt4ZdYLWeap9mn#scrollTo=Ozp0CT08owZ2) I would like to thank him for his hard work and for creating such an amazing text-to-speech models.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
The models license specified in the [original notebook](https://colab.research.google.com/drive/1zh6w_TpEAyr_UIojiLmt4ZdYLWeap9mn#scrollTo=Ozp0CT08owZ2) is the following: "If you use the synthesized voices of this notebook in your project, citing/naming is appreciated, but not required :)" 

