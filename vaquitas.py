import os
import random
import time
import threading

print('Apretá Ctrl + C varias veces para salir...')        
valor = int(input("Cuantas vacas van a cruzar el puente??"))

cowSemaph = threading.Semaphore(valor)

class Puente(threading.Thread):
  def __init__(self, valorInicio, valorLargo):
    super().__init__()
    self.inicio = valorInicio
    self.largo = valorLargo
    self.fin = (self.inicio + self.largo)
  
  def dibujarPuente(self):
      print(' ' * self.inicio + '=' * self.largo)

class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.5)

  def avanzar(self):
    time.sleep(self.velocidad)
    self.posicion += 1

  def dibujar(self):
    print(' ' * self.posicion + "🐮")

  def run(self):
    while(True):
      for p in puentes:
        if(self.posicion == p.inicio):
          cowSemaph.acquire()
          self.avanzar()
        elif(self.posicion == p.finPuente):
          cowSemaph.release()
          self.avanzar()
        else:
          self.avanzar()
      self.avanzar()
      

puentes = []
vacas = []

puente1 = Puente(10,20)
puente1.start()
puente2 = Puente(32,10)
puente2.start()
puentes.append(puente1)
puentes.append(puente2)

for i in range(5):
  v = Vaca()
  vacas.append(v)
  v.start()

def cls():
  os.system('cls' if os.name=='nt' else 'clear')


while(True):
  cls()
  for p in puentes:
    p.dibujarPuente()
    for v in vacas:
      v.dibujar()
    p.dibujarPuente()
    print()
  time.sleep(0.2)
