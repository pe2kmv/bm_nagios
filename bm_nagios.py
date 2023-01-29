#!/usr/bin/env python3

import requests
import json
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('HOST',help='Add the full URL for of the BM server')
parser.add_argument('CALL',help='Add the callsign of the repeater to monitor')

args =parser.parse_args()

dataset = requests.get(args.HOST).json()

for repeater in dataset:
	if repeater['caption'] == str(args.CALL).upper():
		print('Repeater connection OK')
		sys.exit(0)

print('Repeater connection CRITICAL')
sys.exit(2)
