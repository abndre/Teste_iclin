import requests
import json
from argparse import ArgumentParser
from random import randint


parser = ArgumentParser()
parser.add_argument('--number', type=int)
args = parser.parse_args()

url = "http://localhost:8080/agenda"

header = {
    'content-type': 'application/json'
}

names = ['Andre','Carlos','Joao','Pedro']

procedimentos = ['Ortopedista','Clinico Geral','Ortopedista II']

data =   {
			 'data' : '12-11-2017',
			 'horario_inicio':'17:00',
			 'horario_final':'18:00',
			 'Paciente':'Carlos',
			 'Procedimento':'Ortopedista',
			}

r = requests.get(url)

try:
	for i in range(args.number):
		data['horario_inicio']='%s:00'%i
		data['horario_inicio']='%s:00'%(i+1)
		data['Procedimento'] = procedimentos[randint(0, 2)]
		data['Paciente'] = names[randint(0, 3)]


		r = requests.post(url, data=json.dumps(data), headers = header)
except:
	print 'miss arg try: python teste_aplicacao.py --number 10'