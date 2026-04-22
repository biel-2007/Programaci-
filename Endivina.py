import random
numero_ocult=int(random.randrange(1,11))
intents=3
while True:
 resposta=int(input("Número:"))
 intents-=1
 if resposta<numero_ocult:
  print("Més alt")
 elif resposta>numero_ocult:
  print("Més baix")
 elif respuesta==numero_ocult:
  print("Guanyat:",numero_ocult)
  break
 if intents==0:
  print("Perdut:",numero_ocult)
  break