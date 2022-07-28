def parse_information_to_url(language,text):
    origin_lang = 'https://context.reverso.net/translation/english-'
    language_url = origin_lang+language+'/'
    text_url = text.replace(' ','+').replace(',','%2C').replace(':','%3A').replace(';','%3B').replace('?','%3F')
    query_url = language_url+text_url
    return query_url

# print(parse_information_to_url('spanish','Hello I am going to the-mall with my friends today: It will be fun'))
