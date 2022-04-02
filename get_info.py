class info:
	def get_region():
		import requests
		import json
		r = requests.get('http://map-static.vadimklimenko.com/statuses.json')
		binary = r.content
		jsonout = json.loads(binary)
		jsonData = jsonout["states"]
		lenght = len(jsonData)
		list = [None] * lenght
		i = 0
		for key in jsonData:
			list[i] = key
			i = i + 1
		return list
	def get_district(region):
		import requests
		import json
		r = requests.get('http://map-static.vadimklimenko.com/statuses.json')
		binary = r.content
		jsonout = json.loads(binary)
		jsonData = jsonout["states"]
		rnData = jsonData[region]
		dstrk = rnData["districts"]
		list = [None] * len(dstrk)
		i = 0
		for rn in dstrk:
			list[i] = rn
			i = i + 1
		return list
	def get_rgndst_info(rgndst, rg):
		import requests
		import json
		r = requests.get('http://map-static.vadimklimenko.com/statuses.json')
		binary = r.content
		jsonout = json.loads(binary)
		jsonData = jsonout["states"]
		if rg:
			founded = False
			for key in jsonData:
				Data = jsonData[key]
				if key == rgndst:
					founded = True
					return Data["enabled"]
			if founded == False:
				return None
		else:
			founded = False
			for reg in jsonData:
				Data = jsonData[reg]
				region = Data["districts"]
				for key in region:
					if key == rgndst:
						dname = region[key]
						founded = True
						return dname["enabled"]
			if founded == False:
				return None