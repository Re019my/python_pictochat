# CLIENT TCP - pour TP SIN

import socket

IPSERVEUR = '172.22.49.90' # pour test en local; sinon mettre la vraie adresse IP
PORT = 6789

client = socket.socket()
client.connect((IPSERVEUR, PORT))
print('[CLIENT] Connexion vers ' + IPSERVEUR + ':' + str(PORT) + ' reussie.')

while True:
    message = input('>>> ')
    print('[CLIENT] Envoi de :', message)
    message = message.encode('utf-8')
    n = client.send(message)
    if n != len(message):
        print('[CLIENT] Erreur envoi.')
        break
    else:
        print('[CLIENT] Envoi ok.')
        print('[CLIENT] Reception...')
        recu = client.recv(1024)
        recu = recu.decode('utf-8')
        print('[CLIENT] Recu :', recu)

print('[CLIENT] Déconnexion.')
client.close()