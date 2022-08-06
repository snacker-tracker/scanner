#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()

inputs = parser.add_mutually_exclusive_group()
inputs.add_argument("-d", "--device", help="evdev device path")
inputs.add_argument("-f", "--file", help="file like input path")

parser.add_argument("-o", "--output", help="Destination URI (file:// | http:// | stdout://)", type=str, action="append")
args = parser.parse_args()

import snacker_tracker.scanner.input

import snacker_tracker.scanner.output

from datetime import datetime

source = None

#d = snacker_tracker.scanner.input.device.Device('/dev/input/event7')
if args.device != None:
  source = snacker_tracker.scanner.input.Device(args.device)

if args.file != None:
  source = snacker_tracker.scanner.input.File(args.file)

if source == None:
  print("No input defined")
  exit(1)

outputs = []
for output in args.output:
  print(output)
  if output.startswith("http"):
    o = snacker_tracker.scanner.output.Http(output)

  if output.startswith("file"):
    o = snacker_tracker.scanner.output.File(output)


  outputs.append(o)

for event in source.listen():
  dt = datetime.utcnow().isoformat() + "Z"
  #dt = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
  for o in outputs:
    try:
      response = o.write(dt, event)

    except:
      print("Failed to write to output", o)
      pass
