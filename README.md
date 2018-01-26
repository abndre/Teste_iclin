# Teste_iclin
Instalar os pacotes python:
bootle -  https://bottlepy.org/docs/dev/

```bash
pip install bottle

```
Rodar o script main.py

```bash

python main.py
```
Usar alguma aplicação, eu utilizei o PostMan do Google Chrome - https://www.getpostman.com/


Para receber os valores salvos:

GET - localhost:8080/agenda

Para adicionar um valor:

POST - localhost:8080/agenda
Exemplo de BODY JSON
{
	 "data" : "12-11-2017",
	 "horario_inicio":"13:00",
	 "horario_final":"14:00",
	 "Paciente":"Jose",
	 "Procedimento":"Clinico"
}

Para atualizar:

PUT - igual ao exemplo do POST

Para deletar: 

DELETE - localhost:8080/agenda/Andre

Esta é uma aplicação simples que não foi colocado os problemas de sobreposição de horários. Também tem o problema
de deletar ou atualizar um usuário, pois se houver alguém com o mesmo nome dará problema. Mas isto é fácil de ser resolvido utilizando uma base de dados para armazenar, não coloquei pois demandaria mais tempo.

Não foi colocado uma pagina de erro.


