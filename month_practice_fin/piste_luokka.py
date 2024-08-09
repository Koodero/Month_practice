
# Luokka jonne voidaan varastoida käyttäjän pisteet
class Pisteet:
    def __init__(self) -> None:
        self.pisteet = 0
        self.yritykset = 0

    # Metodi jonka avulla voidaan nopeasti tehdä tämä
    def lisää_pisteet(self, pisteet: int, yritykset: int):
        self.pisteet += pisteet
        self.yritykset += yritykset
    