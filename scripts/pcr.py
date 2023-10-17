#!/usr/bin/env python3

def doAnnealing(temp,time):
  print(f"  Annealing at temp {temp}oC for {time}")

def doDenature(temp,time):
  print(f"  Denaturing at temp {temp}oC for {time}")

def doExtension(temp,time):
  print(f"  Extending at temp {temp}oC for {time}")

def doChilling(temp,time):
  print(f"  Chilling at temp {temp}oC for {time}")


print(f"PCR Started.")

(temp, time) = ('','')
cycles = 30

(temp,time) = (94, "3min")
doDenature(temp,time)

for cycle in range(cycles):
  cycle+=1
  print(f"Starting Cycle {cycle}")
  (temp,time) = (94, "30sec")
  doDenature(temp,time)
  (temp,time) = (57, "30sec")
  doAnnealing(temp,time)
  (temp,time) = (72, "1min")
  doExtension(temp,time)
  (temp,time) = (72, "5min")

doAnnealing(temp,time)

print(f"PCR Complete.")
print(f"Starting Chilling")

while (1):
 (temp,time) = (4, "forever")
 doChilling(temp,time)
