#!/usr/bin/env python3
# PURPOSE: parse a TSV file in the format of:
#  https://docs.google.com/spreadsheets/d/1ZLO4TMHaPMLD9d6LENYE9QOQdaMuOQarknNoZ0bICLM/edit?pli=1#gid=1174468441

import os
import sys
from getopt import getopt, GetoptError
from string import punctuation


punctuation_table = {}
for char in punctuation:
  punctuation_table[ord(char)] = None

def usage(message=None, status=1, stream=sys.stderr):
  message = '' if message is None else 'ERROR: %s\n\n' % message
  program = os.path.basename(__file__)
  stream.write(f"""
Usage: {program:s} <in.tsv>

Notes: in.tsv is expected to contain four tab-separated fields:
   role    name    style   size

{message:s}
""")
  sys.exit(status)
  

def main(argv):
  short_options = 'h'
  long_options = (
    '--help'
  )
  try:
    options, arguments = getopt(argv, short_options, long_options)
  except GetoptError as message:
    usage(message)

  for flag, value in options:
    if flag in ('-h','--help'): usage(status=0)
    
  if len(arguments) != 1:
    usage("Unexpected number of arguments")
    
  shirts = {}
  with open(arguments[0],"r") as file_object: 
    for line in file_object:
      line = line.rstrip()

      if line.startswith('#'):
        continue
      
      fields = line.split("\t")

      position, name, style, size = line.split("\t")[0:4]

      name = name.strip()
      style = style.strip().lower().replace('man','men').rstrip('s') + 's'
      size = size.strip().lower().translate(punctuation_table)

      if style not in shirts:
        shirts[style] = {}
      if size not in shirts[style]:
        shirts[style][size] = set()

      shirts[style][size].add((name, position))

  for style in shirts:
    for size in shirts[style]:
      count = len(shirts[style][size])
      print('\t'.join(('S',style,size,str(count))))
      for person in sorted(shirts[style][size]):
        name, position = person
        print('\t'.join(('n',name, position)))
  
      
if __name__ == '__main__':
  main(sys.argv[1:])
  
