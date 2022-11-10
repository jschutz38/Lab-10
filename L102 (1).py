#author is Julia Schutz
dictionary = {"Schutz" : "Julia", "Bub" : "Julia", "Shadid" : "Christina", "Brown" : "Cody", "Doherty" : "Catherine", "Dunn" : "Margaret", "Greene" : "Haley", "Guthrie Beckstrom" : "Isabella", "Hongell" : "Danielle", "Hurley" : "Camryn", "Kevin" : "Ellen", "Kieft" : "Brenna", "Miloserny" : "Amanda", "Nyhuis" : "Kaylen", "Reger" : "Cadyn", "Rusch" : "Emily", "Salazar" : "Britney", "Skrip" : "Holly", "Sullivan" : "Anna", "Verstrete" : "Adrianne", "Wardlow" : "Sarah"}
def new_dict(dictio):
    dictionary2 = dict()
    for key in dictio:
        val = dictio[key]
        if val not in dictionary2:
            dictionary2[val] = [key]
        else:
            dictionary2[val].append(key)
    return dictionary2

d = new_dict(dictionary)
print(d)
