#!/usr/bin/python

import socket
import sys

class war_server:
  def __init__(self):
    self.server_address = ('localhost', 1337)
    
  def parse_args(self, args):
    i=0
    while(i<len(args)):
      if i == '-h':
        i+=1
        self.server_address[0] = args[i]
      else:
        self.usage()
        
  def main(self, args):
    self.parse_args(args)
  
if __name__ == 'main':
  try:
    w = war_server(sys.argv[1:])
    w.main()
  except KeyboardInterrupt:
    sys.exit(0)
