import pytesseract
from PIL import Image
import pyttsx3

textoExtraido = pytesseract.image_to_string(Image.open('./amostra.jpg'))
print(textoExtraido)
engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty("voice", voices[54].id)

engine.say(textoExtraido)
engine.runAndWait()
