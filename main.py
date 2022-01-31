
from gtts import gTTS
import os

# On entre le texte au format string qu'on va convertir en audio
mytext = input("écrivez une phrase en francais.")

# On spécifie la langue
language = 'fr'

# On creer une instance de gTTS class
myobj = gTTS(text=mytext, lang=language, slow=False)

# on creer le mp3
myobj.save("1.mp3")
print("Succès")

# Lis l'audio
os.system("1.mp3")