import json
import glob
class Helper:
	def loadJson(self,file):
		data = json.load(file)
		return data
	def collectFiles(self,data_folder,ext):
		chafiles = glob.glob(data_folder+'/*'+ext)
		return chafiles