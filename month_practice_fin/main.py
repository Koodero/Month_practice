
from testit import kuukausi_numero, numero_kuukausi, kello_numero, puhdista_nautto
from isot_jutut import kellot, kuukausi_sanakirja, alku_valinnat
from piste_luokka import Pisteet


# Ns. main menu jossa kerrotaan käyttäjälle ohjeet ja omat pisteet.
def main():
    puhdista_nautto()

    # Luodaan Pisteet luokasta pelaaja muuttuja jonne on helppo tallentaa pisteet
    pelaaja = Pisteet()

    while True:

        # Tarkastetaan onko käyttäja jo tenhnyt harjoituksia, jos on, niin kerrotaan omat pisteet
        if pelaaja.yritykset != 0:
            print(f"Sinun pisteesi tähän mennessä {pelaaja.pisteet}/{pelaaja.yritykset}")
            print(f"Olet saanut noin {(pelaaja.pisteet/pelaaja.yritykset) * 100:.0f}% vastauksistasi oikein\n\n")

        # Kerrotaan käyttäjälle ohjelman eri vaihtoehdot ja otetaan hänen valinta
        print(alku_valinnat)
        kauttaja_valinta = input("Valitse yksi annetuista vaihtoehdoista: ").strip()
        puhdista_nautto()

        # Riippuen käyttäjän valinnasta aloitetaan jokin harjoitus tai lopetetaan while loopi ja samalla peli
        if kauttaja_valinta == "1":
            pist, yri = kuukausi_numero(kuukausi_sanakirja)

        elif kauttaja_valinta == "2":
            pist, yri = numero_kuukausi(kuukausi_sanakirja)

        elif kauttaja_valinta == "3":
            pist, yri = kello_numero(kuukausi_sanakirja, kellot)

        elif kauttaja_valinta == "4":
            break
        
        # Jos annetaan sopimaton vastaus, tarjotaan käyttäjälle valinta uusiksi
        else:
            puhdista_nautto()
            print("!!!! Koita uudestaan, anna nyt sopiva vaihtoehto !!!!\n")

        # Annetaan pelaajalle pisteet ja asetetaan pist ja yri nollaksi, jotta muuttujat eivät lisää pisteitä siinä tilanteessa jos käyttäjä antaa sopimattoman vastauksen
        pelaaja.lisää_pisteet(pisteet=pist, yritykset=yri)
        pist = yri = 0


# Tämä tapahtuu break jälkeen - valitaan 4 ja lopetetaan peli
    puhdista_nautto()
    try:
        print(f"Pisteesi olivat {pelaaja.pisteet}/{pelaaja.yritykset}.")
        print(f"Olet saanut noin {(pelaaja.pisteet/pelaaja.yritykset) * 100:.0f}% vastauksistasi oikein\n\n")
    except ZeroDivisionError: # Ei voida jakaa pelaajan pisteitä yrityksillä jos molemmat ovat 0
        print("Et edes koittanut 😂")
    print("Kiitos kun pelasit !!!")



if __name__ == "__main__":
    main()

