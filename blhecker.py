import pydnsbl
import ipaddress
import asyncio
import time
import os

#Usuwanie poprzedniego pliku
os.system("rm -rf ./BLresult.txt")

# Importujemy wymagane biblioteki/moduły
from pydnsbl.providers import BASE_PROVIDERS

# Skracamy wywołanie modułu
ip_checker = pydnsbl.DNSBLIpChecker()

# Definiujemy plik dla wyniku skanowania
file_path = "BLresult.txt"

# Zmieniamy prefiksy w listę adresów IPv4
def get_ip_addresses(prefixes):
    addresses = []
    for prefix in prefixes:
        network = ipaddress.IPv4Network(prefix)
        addresses.extend([str(ip) for ip in network.hosts()])
    return addresses

prefixes = ["89.40.144.0/22", "185.11.128.0/22"]
addresses = get_ip_addresses(prefixes)



address_list = []
for address in addresses:
    address_list.append(address)

# Funkcja asynchroniczna do sprawdzania adresu IP
async def check_ip(ip):
    return ip, str(await ip_checker.check_async(ip))

# Pętla weryfikująca każdy adres po kolei (poprzedzone formatowaniem listy) i zapisanie wyniku do pliku
async def main():
    start_time = time.time()

    with open(file_path, "a") as file:
        tasks = []
        for ip in address_list:
            tasks.append(check_ip(ip))
        results = await asyncio.gather(*tasks)
        for ip, output in results:
            file.write(output + "\n")
    file.close()

    end_time = time.time()
    duration = end_time - start_time
    print(f"Skanowanie zakończone. Czas trwania: {duration:.2f} sekundy")

    # Usuwanie pustych linii z pliku
    with open(file_path, "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if line.strip()]

    with open(file_path, "w") as file:
        for line in lines:
            file.write(line + "\n")

# Tworzymy dedykowaną pętlę zdarzeń asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
