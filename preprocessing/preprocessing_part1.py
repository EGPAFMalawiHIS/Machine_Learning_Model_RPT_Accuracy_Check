import json
import glob
import sys
import os
import numpy as np

DATAFOLDER = './data'
def loadJson(file):
	data = json.load(file)
	return data
def collectFiles():
	chafiles = glob.glob(DATAFOLDER+'/*.json')
	return chafiles

def main():
	chafiles = collectFiles()
	for file in chafiles:
		files_json = file
		with open(files_json) as jsonfile:
			data = loadJson(jsonfile)
			print('Data:',data)
			sys.exit()
			for category in categories:
				print(category)
				sys.exit()