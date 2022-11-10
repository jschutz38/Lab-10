#author name is Julia
cpsc_names = ["Julia", "Bub", "Julia", "Schutz", "Cody", "Brown", "Catherine", "Doherty", "Margaret", "Dunn", "Christina", "Shadid", "Cadyn", "Reger", "Holly", "Skrip", "Haley", "Greene", "Isabella", "Guthrie Beckstrom", "Danielle", "Hongell", "Camryn", "Hurley", "Ellen", "Kevin", "Brenna", "Kieft", "Amanda", "Miloserny", "Kaylen", "Nyhuis", "Emily", "Rusch", "Britney", "Salazar", "Anna", "Sullivan", "Adrianne", "Verstraete", "Sarah", "Wardlow"]
def frequency_first_letter(list):
    dictio = dict()
    odd = list[1::2]
    for item in odd:
        if item[0] not in dictio:
            dictio[item[0]] = 1
        else:
            dictio[item[0]] += 1
    return dictio
d = frequency_first_letter(cpsc_names)
print(d)
