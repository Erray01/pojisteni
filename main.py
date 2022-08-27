from vypis import Vypis
from pridat import PridatUzivatele

vypis = Vypis()
pojistenci = []

pokracovat = True

nenalezen = "\nHledaný pojištěnec se nenachází v seznamu, pokračujte libovolnou klávesou...\n"

while pokracovat:
    vypis.obrazovka_hla_cela()
    zadano = False
    while not zadano:
        try:
            vyber = int(input())
            if vyber == 1:
                zadano = True
                jmeno = input("Zadejte křestní jméno pojištěnce: ")
                prijmeni = input("Zadejte přijmení pojištěnce: ")
                tel_cislo = input("Zadejte telefonní číslo pojištěnce: ")
                vek = input("Zadejte věk pojištěnce: ")

                novy_pojistenec = PridatUzivatele(jmeno, prijmeni, tel_cislo, vek)
                print(novy_pojistenec)
                print("Pojištěnec byl nahrán.")
                pojistenci.append(novy_pojistenec)

            elif vyber == 2:
                pozice = -1
                vypis.obrazovka_hla()
                zadano = True
                for pojistenec in pojistenci:
                    print(pojistenec)
                print("\nPokračujte libovolnou klávesou...\n")
                input()

            elif vyber == 3:
                zadano = True
                vypis.obrazovka_hla()
                zadane_jmeno = input("Zadejte jméno:")
                zadane_prijmeni = input('Zadejte přijmení:')
                for pojistenec in pojistenci:
                    if pojistenec.jmeno == zadane_jmeno and pojistenec.prijmeni == zadane_prijmeni:
                        print(pojistenec)

                    else:
                        print(nenalezen)
                        input()

            elif vyber == 4:
                zadano = True
                pokracovat = False
                pass

        except ValueError as v:
            print("Zadali jste nesprávnou možnost.")

vypis.obrazovka_hla()
print("              KONEC - Nashledanou.\n--------------------------------------------\n")
