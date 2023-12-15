import re
def recherche_mot(chaine, mot):
    return mot in chaine

def contient_chiffres(chaine):
    return any(char.isdigit() for char in chaine)

def remplacer_espaces(chaine):
    return chaine.replace(' ', '-')

def verifier_format_telephone(numero):
    pattern = r'^\d{2}-\d{3}-\d{4}$'
    return bool(re.match(pattern, numero))

def valider_email(email):
    pattern = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

