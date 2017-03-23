# -*- coding: utf-8 -*-
'''
╔═╗┬  ┬┬  ┬┬┌─┐  ╔╗ ┌─┐┬─┐┌┬┐┌─┐┬ ┬
║ ║│  │└┐┌┘│├─┤  ╠╩╗│ │├┬┘ ││├┤ │ │
╚═╝┴─┘┴ └┘ ┴┴ ┴  ╚═╝└─┘┴└──┴┘└─┘└─┘
'''
# DATE: 14-Mar-2017
# ACTION: Gets rut from chile.rutificador.com 

import distance
import requests

import time
from time import sleep




def getRUT(iterator):
	iterator['rutificador']=None
	iterator['nombreRutificador']=None

	nombre=iterator['nombre']


	url = 'https://chile.rutificador.com/'
	client = requests.session()
	client.get(url)
	csrftoken = client.cookies['csrftoken']
	url = url + 'get_generic_ajax/'

	data = {
		'entrada': nombre,
		'csrfmiddlewaretoken': csrftoken,
		}
	headers = {
		'Referer': url,
		}
	try:
		response = client.post(url, data=data, headers=headers)
	except:
		print("Connection refused by the server..")
		print("A dormir por 5 segundos")
		print("ZZzzzz...")
		time.sleep(5)
		print("Nice, ahora sigamos...")
		response = client.post(url, data=data, headers=headers)
	results=[]
	if response.json()['status']=='success':
		for x in response.json()['value']:
			dist=distance.levenshtein(nombre,x['name'])
			results.append((x['name'],dist,x['rut']))
		distances=sorted(results, key=lambda palabra: palabra[1])
		if len(distances)!=0:
			iterator['rutificador']=distances[0][2]
			iterator['nombreRutificador'] = distances[0][0]
	return iterator


def main():
	
	data={
	'nombre': 'GARY MEDEL SOTO'
	}

	output=getRUT(data)
	print output


if __name__ == '__main__':
    main()


