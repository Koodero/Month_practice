import random
import os


# Funktio pyyhkimään terminaali
def puhdista_nautto():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS ja Linux
        os.system('clear')


# Tässä kysytään käyttäjältä haluaako jatkaa pelaamista vai ei
def haluatko_jatkaa(pisteet: int, yritykset: int):
    print(f"Pisteesi tähän mennessä {pisteet}/{yritykset}\n")
    print("Haluatko vielä jatkaa tätä harjoitusta?")
    
    vastaus = input("(Kyllä / Ei): ").strip().lower()
    puhdista_nautto()

    return vastaus in ["kyllä", "k"]


# Tämä on käyttäjän vaihtoehto 1: Annetaan käyttäjälle kuukausi ja käyttäjän pitää antaa numerona mones kuu on kyseessä
def kuukausi_numero(sanakirja: dict):
    pisteet = 0
    yritykset = 0
    
    while True:
        # luodaan random kuukausi joka halutaan käyttäjän tietävän
        kuu_nmr = random.randint(1,12)

        print("Mones vuoden kuukausi tämä on?")
        print(sanakirja[kuu_nmr],"\n")
        
        vastaus = input("Anna numero 1 - 12: ").strip()

        # Tarkastetaan onko käyttäjän vastaus sopiva
        if not vastaus.isdigit() or not (1 <= int(vastaus) <= 12):
            print("Virheellinen syöte. Anna numero väliltä 1-12.")
            continue

        puhdista_nautto()

        # Tarkistetaan onko käyttäjän vastaus oikein vai väärin
        vastaus_lause = f"{sanakirja[kuu_nmr]} on vuoden {kuu_nmr} kuukausi"
        if vastaus == str(kuu_nmr):
            print(f"Oikein, {vastaus_lause}!")
            pisteet += 1
        else:
            print(f"Väärin, {vastaus_lause} :(")
            print(f"Sinä vastasit: {vastaus}.")
        yritykset += 1

        # Kysytään halutaanko jatkaa
        if not haluatko_jatkaa(pisteet, yritykset):
            break
        
    return pisteet, yritykset



# Tämä on käyttäjän vaihtoehto 2: Annetaan käyttäjälle kuukauden järjestysnumero ja käyttäjän pitää antaa numerona vastaava kuukausi
# Samat vaiheet kuin kuukausi_numero()
def numero_kuukausi(sanakirja: dict):
    pisteet = 0
    yritykset = 0

    while True:
        kuu_nmr = random.randint(1,12)

        print("Kerro mikä kuukausi vastaa seuraavaa numeroa?")
        print(str(kuu_nmr) + ":","\n")

        vastaus = input("Kirjoita kuukausi tähän: ").strip()

        puhdista_nautto()


        vastaus_lause = f"{sanakirja[kuu_nmr]} on vuoden {kuu_nmr} kuukausi"

        if vastaus.title() == (sanakirja[kuu_nmr]):
            print(f"Oikein, {vastaus_lause}!")
            pisteet += 1
        else:
            print(f"Väärin, {vastaus_lause} :(")
            print(f"Sinä vastasit: {vastaus}.")
        yritykset += 1

        if not haluatko_jatkaa(pisteet, yritykset):
            break
        
    return pisteet, yritykset



# Tämä on käyttäjän vaihtoehto 3: Annetaan käyttäjälle kuukauden järjestysnumero kellon muodossa ja käyttäjän pitää antaa numerona vastaava kuukausi
# Samat vaiheet kuin kuukausi_numero()
def kello_numero(kuu_sanakirja: dict, kello_sanakirja: dict):
    pisteet = 0
    yritykset = 0

    while True:
        kuu_nmr = random.randint(1,12)

        print("Kerro mitä kuuta viisari vastaa?")
        print(kello_sanakirja[kuu_nmr],"\n")

        vastaus = input("Kirjoita numeroa vastaava kuukausi tähän: ").strip()

        puhdista_nautto()

        vastaus_lause = f"{kuu_sanakirja[kuu_nmr]} on vuoden {kuu_nmr} kuukausi"

        if vastaus.title() == (kuu_sanakirja[kuu_nmr]):
            print(f"Oikein, {vastaus_lause}!")
            pisteet += 1
        else:
            print(f"Väärin, {vastaus_lause} :(")
            print(f"Sinä vastasit: {vastaus}.")
        yritykset += 1

        if not haluatko_jatkaa(pisteet, yritykset):
            break
        
    return pisteet, yritykset