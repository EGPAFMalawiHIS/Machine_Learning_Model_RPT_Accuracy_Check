import json
import glob
import os
class Helper:
	def loadJson(self,file):
		data = json.load(file)
		return data
	def collectFiles(self,data_folder,ext):
		chafiles = glob.glob(data_folder+'/*'+ext)
		return chafiles
	def chaStrip(self,data):
		data = str(data)
		data = data.strip()
		stripped = data.rstrip()
		return stripped
	def jsonToDict(self, data):
		return json.loads(data)
	def checkIfFileExists(self,file):
		return os.path.isdir(file)

