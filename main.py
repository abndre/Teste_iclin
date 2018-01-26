#script para Iclinic
#API REST - Agendamento
# deve conter:
#
# 1- Data
# 2- Horario inicio
# 3- Horario fim
# 4- Paciente
# 5- Procedimento

#Interecoes necessarias

#Linstagem de agendamentos - OK
#Detalhes de um agendamento - OK
#Cadastro de um agendamento - OK
#Atualizacao de um agendamento - NOK
#Exclusao de um agendamento - OK

from bottle import run, get, post, request, delete, put

#Examplo de Input

agendamento = [
			{
			 'data' : '12-11-2017',
			 'horario_inicio':'12:00',
			 'horario_final':'13:00',
			 'Paciente':'Andre',
			 'Procedimento':'Clinico Geral',
            },
            {
			 'data' : '12-11-2017',
			 'horario_inicio':'13:00',
			 'horario_final':'14:00',
			 'Paciente':'Joao',
			 'Procedimento':'Ortopedista',
			},
			]


#method para procurar valor na lista agendamento
# TODO: Criar alguma base para colocar os valores
def look_in_list(lista_of_dict,name):
	for value in lista_of_dict:
		if value['Paciente']==name:
			return value


def getAgendamento():
	return {'agendamento' : agendamento}

#methodo para retornar toda a agenda
'''Este e o metodo que retorna a listagem de agendamento'''
@get('/agenda')
def getAll():
	getAgendamento()

#methodo que retorna um nome da agenda,
# TODO, retorna apenas um valor de Paciente,
# 	se houver duas instancias nao retorna

'''methodo que retorna detalhes de um agendamento'''
@get('/agenda/<name>')
def getOne(name):
	return look_in_list(agendamento,name)



#methodo que cria um novo input de paciente
# Todo: nao verifica se o horario esta definido
''' methodo de cadastro de um agendamento'''
@post('/agenda')
def addOne():
	new_agendamento = {
					   'Paciente' : request.json.get('Paciente'), 
					   'data' : request.json.get('data'),
					   'horario_inicio' : request.json.get('horario_inicio'),
					   'horario_final' : request.json.get('horario_final'),
					   'Procedimento' : request.json.get('Procedimento'),
					   }
	agendamento.append(new_agendamento)
	getAgendamento()


#Methodo que remove um paciente
# Todo: remove o primeiro a encontrar
''' remove agendamento'''
@delete('/agenda/<name>')
def removeOne(name):
	agenda = look_in_list(agendamento,name)
	agendamento.remove(agenda)
	getAgendamento()


#Method que atualiza
# Todo: remove apenas o primeiro a encontrar
@put('/agenda')
def updateOne():
	name = request.json.get('Paciente')
	if look_in_list(agendamento,name):
		removeOne(name)
		addOne()
	else:
		addOne()

	

# Este exemplo simples, apenas cria uma lista de dicionarios para colocar os paciente
# Algo mais complexo precisa de uma base e ao criar verificar se os horarios nao conflitan
#   para uma mesma especialidade, mas ai precisaria ser analisado e nao era o escopo
#   do problema.
# O metodo update nao esta tao agradavel quanto queria mas deixei assim. Pois algo mais
#   elaborado depende de uma base boa como ficarao os dados

#chama o script
run(reloader=True, debug=True)
