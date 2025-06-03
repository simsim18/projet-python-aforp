import re

# Expression régulière stricte pour les adresses IPv4
regex_ip = re.compile(
    r'^('
    r'(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}'
    r'(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$'
)

def est_adresse_ip(valeur):
    # Vérifie la correspondance avec l'expression régulière
    if not regex_ip.match(valeur):
        return False
    
    # Rejet si un octet commence par 0 et a plusieurs chiffres (ex: "01", "001")
    parties = valeur.split('.')
    for part in parties:
        if len(part) > 1 and part.startswith('0'):
            return False
    return True

# Boucle interactive
while True:
    ip = input("Entrez une adresse IP : ")
    if ip.lower() == 'exit':
        break
    if est_adresse_ip(ip):
        print(f"{ip} est une adresse IP VALIDE")
    else:
        print(f"{ip} est une adresse IP INVALIDE")