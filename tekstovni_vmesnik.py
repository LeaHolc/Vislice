import model

PONOVNI_ZAGON = 'p'
IZHOD = 'i'

def izpis_igre(igra):
    poskusi = model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()
    tekst = f"""#########################################\n
    Pravilni del gesla: {igra.pravilni_del_gesla()}\n
    Število poskusov: {poskusi}\n
    Nepravilne črke: {igra.nepravilni_ugibi()}\n
#########################################\n
    """
    return tekst

def izpis_zmage(igra):
    tekst = f"""#########################################\n
    Bravo! Zmagali ste!\n
    Uganili ste geslo: {igra.pravilni_del_gesla()}\n
#########################################\n"""
    return tekst

def izpis_poraza(igra):
    tekst = f"""#########################################\n
    Porabili ste vse poskuse!\n
    Pravilno geslo: {igra.geslo}\n
#########################################\n"""
    return tekst

def zahtevaj_vnos():
    return input('Vnesite črko:')

def zahtevaj_moznost():
    return input('Vnesite možnost:')

def ponudi_moznosti():
    tekst = f"""Vpišite črko za izbor naslednjih možnosti:\n
    {PONOVNI_ZAGON} : ponovni zagon igre\n
    {IZHOD} : izhod\n
    """
    return tekst

def izberi_ponovitev():
    print(ponudi_moznosti())
    moznost = zahtevaj_moznost().strip().lower()
    if moznost == PONOVNI_ZAGON:
        igra = model.nova_igra()
        print(izpis_igre(igra))
        return igra
    else:
        return IZHOD

def pozeni_vmesnik():
    igra = model.nova_igra()
    print(izpis_igre(igra))
    while True:
        crka = zahtevaj_vnos()
        odziv = igra.ugibaj(crka)
        if odziv == model.ZMAGA:
            print(izpis_zmage(igra))
            igra = izberi_ponovitev()
            if igra == IZHOD:
                break
        elif odziv == model.PORAZ:
            print(izpis_poraza(igra))
            igra = izberi_ponovitev()
            if igra == IZHOD:
                break
        else:
            print(izpis_igre(igra))
        
pozeni_vmesnik()

# stopnje = [
# """\n _____
#        |   |
#        |   o
#        |  /|\\
#        |  / \\
#       _|______ 
# """, """ _____
#        |   |
#        |   o
#        |  /|\\
#        |  / \\
#       _|______ 
# """]

# testne_crke = ['A', 'I', 'O', 'U', 'D', 'J', 'K', 'Ž', 'E']
# testna_igra = model.Igra("DEŽUJE", testne_crke)
# print(izpis_zmage(testna_igra))