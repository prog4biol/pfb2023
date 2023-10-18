#!/usr/bin/env python3

def doAnnealing(time):
  temp = 57
  print(f"  Annealing at temp {temp}oC for {time}")

def doDenature(time):
  temp = 94
  print(f"  Denaturing at temp {temp}oC for {time}")

def doExtension(time):
  temp = 72
  print(f"  Extending at temp {temp}oC for {time}")

def doChilling(time):
  temp = 4
  print(f"  Chilling at temp {temp}oC for {time}")


cycles = 30
print(f"PCR Started.")

doDenature("3min")

for cycle in range(cycles):
  cycle+=1
  print(f"Starting Cycle {cycle}")
  doDenature("30sec")
  doAnnealing("30sec")
  doExtension("1min")
 
doExtension("5min")

print(f"PCR Complete.")
print(f"Starting Chilling")

while (True):
 doChilling("forever")
