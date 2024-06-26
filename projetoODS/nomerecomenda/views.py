from django.shortcuts import render
from django.http import HttpResponse
from nomerecomenda.models import GeminiNomeRecomenda
import re
import random

def print_teste(request):
    return HttpResponse("Teste de Endpoint")

def initPerguntasPadrao():
    perguntasPadrao = []
    
    perguntasPadrao.append("Quais são as palavras-chave que identificam seu empreendimento?")
    perguntasPadrao.append("Há alguma palavra que não pode faltar no nome do seu empreendimento?")
    perguntasPadrao.append("Qual setor seu empreendimento atua?")
    
    return perguntasPadrao

def fazPergunta(assistant, perguntasPadrao, perguntasLista):
    
    perguntas_para_remover = []

    for pergunta in perguntasPadrao:
        for pergunta_resposta in perguntasLista:
            if pergunta in pergunta_resposta:
                perguntas_para_remover.append(pergunta)
                break
    
    for pergunta in perguntas_para_remover:
        perguntasPadrao.remove(pergunta)

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
    
    comandoPrincipal = "Estou com dificuldades para escolher o nome do meu novo empreendimento. Gere uma lista de nomes a partir das seguintes perguntas e respostas:"
    
    perguntasRespostas = ""
    for pergunta in perguntas:
        perguntasRespostas = perguntasRespostas + pergunta
        perguntasRespostas = perguntasRespostas + "\n"
    
    detalhesComando = "Gere uma lista no seguinte modelo:\n\nLista - Gemini\n\n1. -----\n2. -----\n3. -----\n....\n\nNão adicione dicas, título, descrições ou qualquer texto extra. Busque ser criativo e evite gerar nomes genéricos"
    
    prompt = f"{comandoPrincipal}\n\n{perguntasRespostas}\n{detalhesComando}"
    
    return prompt
  
def formataNomes(promptResponse):
    nomesGerados = []

    lines = promptResponse.strip().split('\n')

    for line in lines[2:]:
        item = line.split('. ', 1)[1]
        nomesGerados.append(f"{item} ")
        
    return nomesGerados

def gerarNomes(request):
    
    assistant = GeminiNomeRecomenda()
    flag = int(request.GET.get('flag', 0))
    perguntas = request.GET.getlist('perguntas', [])
    
    if(flag == 1):
        perguntasPadrao = initPerguntasPadrao()
        
        novaPergunta = fazPergunta(assistant, perguntasPadrao, perguntas)
        return HttpResponse(novaPergunta)
    
    elif(flag == 2):
        resposta = request.GET['resposta']
        ultima_pergunta_index = len(perguntas)-1
        receberResposta(perguntas[ultima_pergunta_index], resposta, perguntas)
        
        promptResponse = assistant.model.generate_content(novoPrompt(perguntas)).text
        nomes = formataNomes(promptResponse)
        
        return HttpResponse(nomes)
    
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