#!/usr/bin/python

from time import sleep
from random import randint
import threading

chopsticks = []
for loop in range(0,5):
  chopsticks.append(threading.Lock())

class DiningPhilosopher(threading.Thread):
  def __init__(self, philosopherID):
    threading.Thread.__init__(self)
    self.philosopherID = philosopherID
  
  def run(self):
    leftChopstick = self.philosopherID
    rightChopstick = (self.philosopherID + 1) % 5
    print("philosopher: " + str(self.philosopherID))

    while True:
      #think for random period of time
      sleep(randint(1,10))

      #chopsticks[leftChopstick].acquire()  #Currently results in deadlock duh

      #eat for random period of time
      #sleep(randint(1,10)) 
      #chopsticks[leftChopstick].release()
  
if __name__ == "__main__":
  philosophersList = []
  for philosopher in range(0,5):
    philosophersList.append(DiningPhilosopher(philosopher))
  
  for philosopher in philosophersList:
    philosopher.start()

  for philosopher in philosophersList:
    philosopher.join()

  print("Finish Running")
