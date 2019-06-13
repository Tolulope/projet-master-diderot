from io import StringIO

def comprimer(donnees):
    dict_size = 256
    dictionnaire = {chr(i): i for i in range(dict_size)}

    w = ""
    donnees_comprimees = []

    for symbole in donnees:
        ws = w + symbole
        if ws in dictionnaire:
            w = ws
        else: 
            donnees_comprimees.append(dictionnaire[w])
            dictionnaire[ws] = dict_size
            dict_size += 1
            w = symbole
    if w in dictionnaire:
        donnees_comprimees.append(dictionnaire[w])
    return donnees_comprimees

def decomprimer(donnees_comprimees):
    dict_size = 256
    dictionnaire = {i: chr(i) for i in range(dict_size)}
    resultat = StringIO()
    w = chr(donnees_comprimees.pop(0))
    resultat.write(w)

    for code in donnees_comprimees:
        if code in dictionnaire:
            entry = dictionnaire[code]
        elif code == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed code: %s' %code)
        resultat.write(entry)

        dictionnaire[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return resultat.getvalue()
          