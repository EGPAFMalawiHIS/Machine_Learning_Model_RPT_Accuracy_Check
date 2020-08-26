
import sys
import os
import numpy as np
from common.helper import *

class IndicatorMapper:
	def __init__(self):
		self.data_folder = './rawdata'
		self.dataset_folder = './dataset'
		self.helper = Helper()

	def getSite(self,data):
		sitecode = self.helper.chaStrip(data['sitecode'])
		sitename = self.helper.chaStrip(data['sitename'])
		site = {'sitecode':sitecode,'sitename':sitename}
		return site
	def generatePath(self,site):
		path = self.dataset_folder + site.lower() + '.h5'
		return path
	def pepfar_disagg(self,data):
		return 0

	def extractData(self,data):
		#check report name
		report_data = []
		report_name = data['report_name']
		if report_name == 'PEPFAR Disaggregated Report':
			report_data = self.pepfar_disagg(data)
		return report_data


	def mapper(self,data):
		site = self.getSite(data)
		#check is this site exit in our internal db
		file_path = self.generatePath(site['sitecode'])
		if self.helper.checkIfFileExists(file_path):
			extracted_data = self.extractData(data)
		else:
			extracted_data = self.extractData(data)


		print('EXIST:',self.helper.checkIfFileExists(file_path))
		sys.exit()


	def main(self):
		chafiles = self.helper.collectFiles(self.data_folder,'.json')
		for file in chafiles:
			files_json = file
			with open(files_json) as jsonfile:
				data = self.helper.loadJson(jsonfile)
				mapped_data = self.mapper(data)

