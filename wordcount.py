#!/usr/bin/python2.7

import sys
#import string

def process_file(filename):
  hist = {}
  f = open(filename, 'rU')
  for line in f:
    line = line.lower()
    for word in line.split(): 
    #  print word
      if word in hist:
        hist[word] += 1
      else:
        hist[word] = 1
 # print_count(hist)
  return hist

def print_count(filename):
  hist = process_file(filename)
  t=[]
  for key, val in hist.items():
    t.append( (val, key))
  
  t.sort(reverse=True)

  for key, val in t:
    print key, val

#word_count(hist)
def print_top_count(filename):
  hist = process_file(filename)
  t=[]
  for key, val in hist.items():
    t.append( (val, key))

  t.sort(reverse=True)

  for key, val in t[:05]:
    print key, val


def main():
  #process_file(sys.argv[1])
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)
  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_count(filename)
  elif option == '--topcount':
    print_top_count(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)



if __name__ == '__main__':
  main()
