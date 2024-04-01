pip3 install googletrans
pip3 install googletrans==3.1.0a0
from googletrans import Translator, constants
from pprint import pprint
# init the Google API translator
translator = Translator()
# translate a spanish text to arabic for instance
translation = translator.translate("Hola Mundo", dest="ar")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
# specify source language
translation = translator.translate("Wie gehts ?", src="de")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
# print all translations and other data
pprint(translation.extra_data)
