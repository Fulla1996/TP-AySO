import requests
import socket

URL = input("Ingrese la url deseada: ")

ip = requests.get("http://dns:5000/getip?url=" + URL)
#ip = socket.gethostbyname(URL)

if ip.status_code == 404:
    print("Servidor no encontrado")
elif ip.status_code == 200:
    print(f"IP del servidor: {ip.text}")
    URL = "http://" + ip.text + ":5000/"
    response = requests.get(URL)
    print("Respuesta del servidor:", response.json())
else:
    print("Error inesperado")