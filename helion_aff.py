while True:
    try:
        aff_id = int(input('Podaj swój kod afiliacyjny ---> '))
        break
    except ValueError:
        print('Kod jest błędny. Podaj poprawny kod numeryczny.')

from urllib.error import URLError
import requests

def status_200(url):
    status_check = requests.get(url)

    if status_check.status_code == 200:
        print('🟢 Kod odpowiedzi serwera ---> ', status_check.status_code)
        return url
    else:
        print('🔴 Kod odpowiedzi serwera jest inny niż 200, link nie został utworzony.')

def ensure_helion(url):
    return url.startswith('https://helion.pl')

def ensure_helion_homepage(url):
    return url == 'https://helion.pl' or url == 'https://helion.pl/'

def ensure_helion_product(url):
    return ensure_helion(url) and url[:-1].endswith('.htm#format/')

def ensure_helion_add_to_cart(url):
    return url.startswith('https://helion.pl/zakupy/add.cgi?id=')

def ensure_helion_category(url):
    return url.startswith('https://helion.pl/kategorie')

def get_helion_link_type(url):
    link_type_text = '🌐 Typ strony ---> '
    if ensure_helion_homepage(url):
        print(link_type_text, 'Strona główna')
    elif ensure_helion_category(url):
        print(link_type_text, 'Kategoria')
    elif ensure_helion_product(url):
        print(link_type_text, 'Produkt')
    elif ensure_helion_add_to_cart(url):
        print(link_type_text, 'Koszyk')
    else:
        print('🔴 Nie rozpoznano typu strony')

def get_link_naked():
    url = input('Podaj link, dla którego chcesz wygenerować link afiliacyjny ---> ')
    if status_200(url):
        if ensure_helion(url):
            get_helion_link_type(url)
            return url
        else:
            raise URLError('URL w nieodpowiednim formacie')

def post_link_aff(url):
    import re

    link_aff_text = '💸 Link afiliacyjny ---> '

    if ensure_helion_homepage(url):
        link_aff = f'https://helion.pl/view/{aff_id}'
        print(link_aff_text, link_aff)
        return link_aff
    elif ensure_helion_product(url):
        product_id = re.search(',(.*).htm(.*)', url).group(1)
        link_aff = f'https://helion.pl/view/{aff_id}/{product_id}.htm'
        print(link_aff_text, link_aff)
        return link_aff
    elif ensure_helion_category(url):
        category_slug = re.search('kategorie/(.*)', url).group(1)
        link_aff = f'https://helion.pl/page-new/{aff_id}/kategorie/{category_slug}'
        print(link_aff_text, link_aff)
        return link_aff
    elif ensure_helion_add_to_cart(url):
        product_id = re.search('id=(.*)', url).group(1)
        link_aff = f'https://helion.pl/add/{aff_id}/{product_id}'
        print(link_aff_text, link_aff)
        return link_aff
    else:
        print('Nie mogę utworzyć linku')


# def main():
#
#
# if __name__ == '__main__':
#     main()
