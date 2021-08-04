from datetime import datetime, timedelta
# 15. 8. 2021
pozadovanyDenNastevyKina_str = input("Zadej datum návštěvy [den. měsíc. rok]: ")
pozadovanyDenNastevyKina_str = pozadovanyDenNastevyKina_str.replace(" ", "")
pozadovanyDenNastevyKina = datetime.strptime(pozadovanyDenNastevyKina_str, "%d.%m.%Y")
pozadovanyPocetListku = abs(int(input("Zadej počet lístků: ")))
otevreniKina = datetime(2021, 7, 1)
zacatekLenvejnsiSezony = datetime(2021, 8, 11)
uzavreniKina = datetime(2021, 9, 1)
if pozadovanyDenNastevyKina < otevreniKina:
    print("Kino je v té době zavřené")
elif pozadovanyDenNastevyKina < zacatekLenvejnsiSezony:
    cenaZaVstupenku = 250
    print(f"Cena za vstupenky je {cenaZaVstupenku * pozadovanyPocetListku}")
elif pozadovanyDenNastevyKina < uzavreniKina:
    cenaZaVstupenku = 180
    print(f"Cena za vstupenky je {cenaZaVstupenku * pozadovanyPocetListku}")
else:
    print("Kino je v té době zavřené")

