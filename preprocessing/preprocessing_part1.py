
import sys
import os
import numpy as np
from common.helper import *

class IndicatorMapper:
	def __init__(self):
		self.data_folder = './data'
		self.helper = Helper()

	def getSite(self,data):
		site = []
		site.append({sitecode:data['sitecode'],sitename:data['sitename']})

	def main(self):
		chafiles = self.helper.collectFiles(self.data_folder,'.json')
		for file in chafiles:
			files_json = file
			with open(files_json) as jsonfile:
				data = self.helper.loadJson(jsonfile)
				print('Data:',data)
				sys.exit()
				for category in categories:
					print(category)
					sys.exit()