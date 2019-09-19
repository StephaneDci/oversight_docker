#coding:utf-8

#import module
import docker

# instanciation d'un client sur le socket docker
client = docker.from_env()

#print ("\n## Lancement container ## ")
#client.containers.run("alpine", ["echo", "hello", "world"])

print("\n## Liste des containers ##")
for container in client.containers.list(all=True, since="consul"):
  print("%s  %s  %s" % (container.short_id, container.name, container.status))

print("\n## Liste des images docker ##")
for image in client.images.list():
  print image

