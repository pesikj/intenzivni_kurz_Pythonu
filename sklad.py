sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
vstup = input("Zadej kód součástky: ")
if vstup in sklad:
    mnozstvi = int(input("Zadej požadované množství"))
    if sklad[vstup] < mnozstvi:
        print(f"Na skladě je pouze {sklad[vstup]} kusů.")
        print("Na skladě je pouze", sklad[vstup], "kusů")
        sklad.pop(vstup)
    else:
        print("Součástek je dostatek")
        sklad[vstup] = sklad[vstup] - mnozstvi
        # sklad[vstup] -= mnozstvi
else:
    print("Součástka není na skladě")
