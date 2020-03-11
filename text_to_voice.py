from argparse import ArgumentParser
from io import BytesIO
from googletrans import Translator
from gtts import gTTS
from pygame import mixer


def translate(text, lang):
    translator = Translator()
    translated = translator.translate(text, dest=lang).text
    tts = gTTS(text=translated, lang=lang)
    mixer.init()
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    mixer.music.load(fp)
    mixer.music.play()
    print(translated)


def main():
    parser = ArgumentParser()
    parser.add_argument("-1", '--language', action="store", default='ben')
    args = parser.parse_args()

    while True:
        text = input("translate:")
        translate(text, args.language)


if __name__ == "__main__":
    main()