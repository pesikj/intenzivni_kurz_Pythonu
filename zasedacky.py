volne_zasedacky = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}
hodina = int(input("Zadej hodinu: "))
print(f"Počet volných zasedaček je {len(volne_zasedacky[hodina])}")
print(f"Volné zasedačky jsou: {volne_zasedacky[hodina]}")