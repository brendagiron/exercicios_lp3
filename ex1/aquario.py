def volume(com, alt, lar):
    return (com * alt * lar) / 1000

def potenciatermostato(vol, des, amb):
    return vol * 0.05 * (des - amb)

def filtragem(vol):
    return vol * 2, vol * 3