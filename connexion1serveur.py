import socket
import json

# ça ça sert à se connecter au serveur , s'y inscrire
s = socket.socket()
s.connect(('172.17.10.52', 3000))
data = {"request": "subscribe",
  "port": 8888,
  "name": "pounds ",
  "matricules": [ "22259"]
}
json_data= json.dumps(data)
json_bytes= json_data.encode('utf-8')
s.sendall(json_bytes)

reponse=s.recv(3000)
print("réponse du serveur:",reponse.decode('utf-8'))
s.close()

# mtn faut le ping pong ce qui va servir quand on devra jouer , faire des coups
ip = '172.17.10.52'
port = 8888
adresse = (ip, port)

s2 = socket.socket()
s2.bind(adresse)
s2.listen(1)
print("en attente de connexion...")
s3, addr = s2.accept()

print("connecté à ", addr)
data2 = s3.recv(8888)
print("données reçu:",data2.decode('utf-8'))

reponse2= {"status": "ok", "message":"pong"}

json_bytes2= json.dumps(reponse2).encode('utf-8')
s3.recv(8888)
s3.send(json_bytes2)


print("deuxième réponse du serveur", reponse2["message"])

s3.close()
s2.close()



# pour voir si on arrive à envoyer un message au server on doit faire 'ping Adresse IP ' et lancer enter



