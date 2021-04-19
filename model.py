import random

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'

class Igra:
    def __init__(self, geslo, crke):
        self.geslo = geslo
        self.crke = crke[:]

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        vse_crke = True
        for crka in self.geslo:
            if crka in self.pravilne_crke():
                pass
            else:
                vse_crke = False
                break
        #vse_crke = all(crka in self.crke for crka in self.geslo)
        return vse_crke and STEVILO_DOVOLJENIH_NAPAK >= self.stevilo_napak()

    def poraz(self):
        return STEVILO_DOVOLJENIH_NAPAK < self.stevilo_napak()

    def pravilni_del_gesla(self):
        delni = ''
        ugibanje = [crka.upper() for crka in self.crke]
        for crka in self.geslo:
            if crka.upper() in ugibanje:
                delni += crka + ' '
            else:
                delni += '_ '
        return delni.strip()

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            self.crke.append(crka)
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA


with open('Vislice_1/besede.txt', 'r', encoding='utf-8') as f:
    bazen_besed = [beseda.strip().upper() for beseda in f.readlines()]   

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, [])    


# testno_geslo = 'DEŽUJE'
# testne_crke = ['A', 'I', 'O', 'U', 'D', 'J', 'K']
# igra = Igra(testno_geslo, testne_crke)

    

