from vypis import Vypis


class PridatUzivatele:

    def __init__(self, jmeno, prijmeni, tel_cislo, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.tel_cislo = tel_cislo
        self.vek = vek

    def __str__(self):
        return f'{self.jmeno} \t {self.prijmeni} \t {self.tel_cislo} \t {self.vek}'