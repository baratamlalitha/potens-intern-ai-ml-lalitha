from deep_translator import GoogleTranslator

def translate_to_english(text):

    translated = GoogleTranslator(
        source='auto',
        target='en'
    ).translate(text)

    return translated


def translate_to_original_language(
    text,
    target_language
):

    translated = GoogleTranslator(
        source='en',
        target=target_language
    ).translate(text)

    return translated