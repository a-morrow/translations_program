# Packages used for program
from connection_status import connection as con
from parse_translation_text import parse_url as par
from translator import translations as tr


print('Welcome to Python Translator....\nTesting Connection:')

flag = True
while flag:
    avail_input_lang = {'es': 'spanish', 'fr': 'french', 'gr': 'german', 'it': 'italian'}
    if not con.connection_main():
        print('Connection error detected')
        flag = False
    else:
        print('Connection successful')
    print('OPTIONS:\n--------------\n'+'a) Enter Application [enter]\n' + 'b) Quit Application [quit]')
    user_decision = input('>')
    if user_decision == 'quit':
        print('Exiting program')
        flag = False
    else:
        print('Entering program')
    print("Available languages to translate to are:'\n'",avail_input_lang)
    language_input = input('Choose language:')
    if language_input not in avail_input_lang:
        print('Language not supported. Exiting program')
        flag = False
    else:
        print('Language chosen:',avail_input_lang[language_input])
    translation_text = input('Enter text to translate:')
    query_url = par.parse_information_to_url(avail_input_lang[language_input],translation_text)
    translation = tr.translation_result(query_url)
    print('Translation:\n')
    for i in translation:
        print(i)
    print('\nExiting Program -- Translation Complete')
    flag = False
