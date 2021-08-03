purchaseList = [
  {"person": "Petr", "item": "Prací prášek", "value": 399},
  {"person": "Ondra", "item": "Savo", "value": 80},
  {"person": "Petr", "item": "Toaletní papír", "value": 65},
  {"person": "Libor", "item": "Pivo", "value": 124},
  {"person": "Petr", "item": "Pytel na odpadky", "value": 75},
  {"person": "Míša", "item": "Utěrky na nádobí", "value": 130},
  {"person": "Ondra", "item": "Toaletní papír", "value": 120},
  {"person": "Míša", "item": "Pečící papír", "value": 30},
  {"person": "Zuzka", "item": "Savo", "value": 80},
  {"person": "Pavla", "item": "Máslo", "value": 50},
  {"person": "Ondra", "item": "Káva", "value": 300}
]
sumPerPerson = {}
total = 0
for item in purchaseList:
  person = item["person"]
  total = total + item["value"]
  if person in sumPerPerson:
    sumPerPerson[person] = sumPerPerson[person] + item["value"]
  else:
    sumPerPerson[person] = item["value"]
average_value = total/len(sumPerPerson)
for person, value in sumPerPerson.items():
  if value > average_value:
    print(f"{person} dostane {value - average_value} Kč.")
  else:
    print(f"{person} doplatí {average_value - value} Kč.")
