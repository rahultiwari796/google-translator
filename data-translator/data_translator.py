import json
from py_translator import Translator
from difflib import get_close_matches

languages_code = json.load(open("language.json","r"))
translator = Translator()


def data_translator(word , language="en"):
    if language.lower() in languages_code.keys():
        return translator.translate(word,dest=language.lower())
    elif language.upper() in languages_code.keys():
        return translator.translate(word,dest=language.upper())
    elif language.title() in languages_code.keys():
        return translator.translate(word,dest=language.title())
    elif len(get_close_matches(language,languages_code.keys())) > 0:
        isMean = input("Did you mean %s instead of %s ? if Yes enter Y , or if no enter N: " % (get_close_matches(language, languages_code.keys())[0],language)).upper()
        if isMean == "Y":
            return translator.translate(word,dest=get_close_matches(language,languages_code.keys())[0].upper())
        elif isMean == "N":
            return "Given language doesn't exist. Please double check it !!"
        else:
            return "We didn't understand your entry"
    else:
        return "Given language doesn't exist. Please double check it !!"


language = input("enter the language in which you want translation: ")
word = input("enter the word which you want to translate: ")

try:
    translation = data_translator(word,language)
    print("%s -> %s" % (translation.origin,translation.text))
except AttributeError:
    print("Due to some reason not able to translate, Please try later !!")


# print("Translated Text: ",translation.text)
