#Importujemy wymagane biblioteki/moduły
import pydnsbl, ipaddress
from pydnsbl import DNSBLIpChecker, providers
from pydnsbl.providers import BASE_PROVIDERS, Provider

#Skracamy wywołanie modułu
ip_checker = pydnsbl.DNSBLIpChecker()

#Definiujemy plik dla wyniku skanowania
file_path = "BLresult.txt"

#Zmieniamy prefiksy w listę adresów IPv4
def get_ip_addresses(prefixes):
    addresses = []
    for prefix in prefixes:
        network = ipaddress.IPv4Network(prefix)
        addresses.extend([str(ip) for ip in network.hosts()])
    return addresses

prefixes = ["89.40.147.0/30", "89.40.147.0/29"]
addresses = get_ip_addresses(prefixes)

address_list = []
for address in addresses:
    address_list.append(address)

#Pętla weryfikująca każdy adres po kolei (poprzedzone formatowaniem listy) i zapisanie wyniku do pliku
with open(file_path, "a") as file:
    for ip in address_list:
        output = str(ip_checker.check(f'{ip}'))
        file.write(output + "\n")
file.close()
