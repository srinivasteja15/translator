from googletrans import Translator
sentence = str(input("enter string to translate:"))
translator = Translator()
translated_sentence=translator.translate(sentence, src='en', dest='hi')
print(translated_sentence.text)
