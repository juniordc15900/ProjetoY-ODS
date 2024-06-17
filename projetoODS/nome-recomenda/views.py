from django.shortcuts import render
from django.http import HttpResponse
from models import GeminiNomeRecomenda
import re
import random

'''
def extract_numbers(input_string):
    numbers = re.findall(r'\d+', input_string)
    numbers = [int(num) for num in numbers]

    return numbers
'''
'''
def escolherMelhoresNomes(nomesEscolhidos, listaDeNomes):

    print("\nQual dos seguintes nomes mais lhe agrada? Caso nenhum deles seja escolhido, aperte ENTER")
    
    for index, nome in enumerate(listaDeNomes):
        print(f"{index+1}. {nome}")
    
    escolha = input()
    escolha = extract_numbers(escolha)
    
    for i in escolha:
        nomesEscolhidos.append(listaDeNomes[i-1])
'''
'''
def initPrompt(prompt, perguntasLista):
    
        comandoPrincipal = "Estou com dificuldades para escolher o nome do meu novo empreendimento. Gere uma lista de nomes a partir das seguintes perguntas e respostas:\n"
        
        perguntaInicial = "Quais são as palavras-chave que identificam seu empreendimento?"
        print(perguntaInicial)
        respostaPerguntaInicial = input()
        perguntasLista.append(f"{perguntaInicial}\nR: {respostaPerguntaInicial}")
        
        detalhesComando = "Gere uma lista no seguinte modelo:\n\nLista - Gemini\n\n1. -----\n2. -----\n3. -----\n....\n\nNão adicione dicas, título, descrições ou qualquer texto extra"
        
        prompt = f"{comandoPrincipal}\n\n{perguntaInicial}\nResposta: {respostaPerguntaInicial}\n\n{detalhesComando}"
        
        return prompt
'''

def print_teste(request):
    return HttpResponse("Teste de Endpoint")

def initPerguntasPadrao():
    perguntasPadrao = []
    
    perguntasPadrao.append("Quais são as palavras-chave que identificam seu empreendimento?")
    perguntasPadrao.append("Há alguma palavra que não pode faltar no nome do seu empreendimento?")
    perguntasPadrao.append("Qual setor seu empreendimento atua?")
    
    return perguntasPadrao

def fazPergunta(assistant, perguntasPadrao, perguntasLista):
    
    if(len(perguntasPadrao) > 0):
        index = random.randint(0, len(perguntasPadrao)-1)
        perguntaSelecionada = perguntasPadrao[index]
        perguntasLista.append(perguntaSelecionada)
        perguntasPadrao.pop(index)
        return perguntaSelecionada
    else:
        return gerarNovaPergunta(assistant, perguntasLista)
    
def receberResposta(perguntaFeita, resposta, perguntasLista):
    
    len(perguntasLista) - 1
    perguntasLista[len(perguntasLista) - 1] = f"{perguntaFeita}\nR: {resposta}"
    
    return perguntasLista
        
def gerarNovaPergunta(assistant, perguntasLista):

    novaPerguntaprompt = "Estou desenvolvendo um sistema de geração de nomes para empreendimentos baseado em perguntas e respostas. Gere uma pergunta no mesmo modelo que as seguintes:\n\n"
    
    for pergunta in perguntasLista:
        novaPerguntaprompt = novaPerguntaprompt + pergunta + "\n"
        
    prompt_response = assistant.model.generate_content(novaPerguntaprompt).text
    perguntasLista.append(prompt_response)
    
    return prompt_response

def novoPrompt(perguntas):

    indexUltimaPergunta = len(perguntas)-1
    print(perguntas[indexUltimaPergunta])
    resposta = input()
    perguntas[indexUltimaPergunta] = f"{perguntas[indexUltimaPergunta]}\nR: {resposta}"
    
    comandoPrincipal = "Estou com dificuldades para escolher o nome do meu novo empreendimento. Gere uma lista de nomes a partir das seguintes perguntas e respostas:"
    
    perguntasRespostas = ""
    for pergunta in perguntas:
        perguntasRespostas = perguntasRespostas + pergunta
        perguntasRespostas = perguntasRespostas + "\n"
    
    detalhesComando = "Gere uma lista no seguinte modelo:\n\nLista - Gemini\n\n1. -----\n2. -----\n3. -----\n....\n\nNão adicione dicas, título, descrições ou qualquer texto extra"
    
    prompt = f"{comandoPrincipal}\n\n{perguntasRespostas}\n{detalhesComando}"
    
    return prompt
  
def formataNomes(promptResponse):
    nomesGerados = []

    lines = promptResponse.strip().split('\n')

    for line in lines[2:]:
        item = line.split('. ', 1)[1]
        nomesGerados.append(item)

def gerarNomes(perguntas, request):
    
    assistant = GeminiNomeRecomenda()
    flag = request.GET['flag']
    
    if(flag == 1):
        perguntasPadrao = initPerguntasPadrao()
        
        novaPergunta = fazPergunta(assistant, perguntasPadrao, perguntas)
        return novaPergunta
    
    elif(flag == 2):
        resposta = request.GET['resposta']
        ultima_pergunta_index = len(perguntas)-1
        receberResposta(perguntas[ultima_pergunta_index], resposta, perguntas)
        
        promptResponse = assistant.model.generate_content(novoPrompt(perguntas)).text
        nomes = formataNomes(promptResponse)
        
        return nomes
    
'''
def main():

    assistant = GeminiNomeRecomenda()
    
    prompt = ""
    perguntas = []
    listaDeNomes = []
    nomesEscolhidos = []
    
    prompt = initPrompt(prompt, perguntas)
    
    while True:
        prompt_response = assistant.model.generate_content(prompt).text
        print(prompt_response)
        
        adicionaNomes(listaDeNomes, prompt_response)
        escolherMelhoresNomes(nomesEscolhidos, listaDeNomes)

        while True:
            if len(nomesEscolhidos) > 0:
                print("Deseja continuar? (S/N)")
                resposta = input()
                
                if resposta.upper() == "N":
                    print(f"Nomes escolhidos: {nomesEscolhidos}")
                    return nomesEscolhidos
                elif resposta.upper() == "S":
                    gerarNovaPergunta(assistant, perguntas)
                    prompt = novoPrompt(perguntas)
                    break
                else:
                    print("Resposta inválida")
            else:
                gerarNovaPergunta(perguntas)
                prompt = novoPrompt(perguntas)
                break
'''