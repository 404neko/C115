def ZBar(System):
    if System=='Linux':
        return 'zbarimg'
    if System=='Windows':
        return 'zbar\zbarimg.exe'
