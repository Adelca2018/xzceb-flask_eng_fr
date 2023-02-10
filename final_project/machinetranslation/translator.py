import json
import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
AUTHENTICATOR = IAMAuthenticator(APIKEY)

language_translator = LanguageTranslatorV3(version = '2023-02-08' ,  
authenticator = AUTHENTICATOR)

language_translator.set_service_url(URL)

def english_to_french(english_text):
    try:
        french_text = language_translator.translate(text = english_text,
            model_id = 'en-fr').get_result()
    except IOError:   
        print("input error")
    else:
        return french_text

def french_to_english(french_text):
    try:
        english_text = language_translator.translate(
            text = french_text,
            model_id = 'fr-en'
            ).get_result()
    except IOError:   
        print("input error")
    else:
        return english_text