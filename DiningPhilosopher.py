#!/usr/bin/python

from time import sleep
from random import randint
import threading

#waiter to serve the philosophers
waiter = threading.Lock()

#chopsticks needed to eat!
chopsticks = []
for loop in range(0,5):
  chopsticks.append(threading.Lock())

#Implement philosopher thread class as a child class of threading.Thread
class DiningPhilosopher(threading.Thread):
  def __init__(self, philosopherID):
    threading.Thread.__init__(self)
    self.philosopherID = philosopherID
  
  def run(self):
    leftChopstick = self.philosopherID
    rightChopstick = (self.philosopherID + 1) % 5

    while True:
      #think for random period of time
      print("philosopher" + (str)(self.philosopherID) + "is thinking")
      sleep(randint(1,2))
		
      waiter.acquire()
      chopsticks[leftChopstick].acquire()
      sleep(5)  #increase likelyhood of deadlock by making all philosophers pick up right at same time
      chopsticks[rightChopstick].acquire()
      waiter.release()

      #eat for random period of time
      print("philosopher" + (str)(self.philosopherID) + "is eating")
      sleep(randint(1,2)) 
      chopsticks[leftChopstick].release()
      chopsticks[rightChopstick].release()
  
if __name__ == "__main__":
  philosophersList = []
  for philosopher in range(0,5):
    philosophersList.append(DiningPhilosopher(philosopher))
  
  for philosopher in philosophersList:
    philosopher.start()

  for philosopher in philosophersList:
    philosopher.join()

  print("Finish Running") #Technically it never finishes running since infinite loop :)
