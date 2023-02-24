# SERVEUR TCP - pour TP Reseau

import socket

# Identification réseau de ce programme
IP = '172.22.49.89'
PORT = 6789

ADRESSE = IP, PORT

# création d'un canal de communication - socket - de type serveur
serveur = socket.socket() # création
serveur.bind(ADRESSE) # association à l'adresse du programme ...
serveur.listen(1) # écoute du réseau

print('[SERVEUR] démarré, en attente de connexions.')

# on attend une connexion entrante
client, adresseClient = serveur.accept()
print('[SERVEUR] Connexion de', adresseClient)

# Boucle de dialogue (ici de type «perroquet»)
while True:
    recu = client.recv(1024)
    if len(recu) == 0:
        print('[SERVEUR] Erreur de réception.')
        break
    else:
        recu = recu.decode('utf-8') # décodage du message reçu
        print('[SERVEUR] Réception de:', recu)
        reponse = input('>>> ')
        print('[SERVEUR] Envoi de :', reponse)
        reponse = reponse.encode('utf-8') # encodage du message à émettre
        n = client.send(reponse)
        if n != len(reponse):
            print('[SERVEUR] Erreur envoi.')
            break
        else:
            print('[SERVEUR] Envoi ok.')

# si on est là c'est que la connexion est rompue ;
# il faut alors fermer les canaux de communication
print('[SERVEUR] Fermeture de la connexion avec le client.')
client.close()
print('[SERVEUR] On se débranche et on quitte.')
serveur.close()