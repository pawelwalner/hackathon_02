import helion_aff

while True:
    try:
        filename = input('Podaj nazwę pliku, do którego chcesz dodawać linki ---> ')
        links_number = int(input('Ile linków chcesz zamienić na linki afiliacyjne? ---> '))
        while links_number != 0:
            links_number -= 1
            url = helion_aff.get_link_naked()
            link_aff = helion_aff.post_link_aff(url)
            with open(filename, 'a') as f:
                f.write(link_aff + '\n')
        print(f'\n💾 Linki zostały pomyślnie zapisane do pliku {filename}')
        break
    except helion_aff.URLError as error:
        print(error)
