from django.http import JsonResponse
from time import time
import whois
import threading
import json

def is_registered(domain):
    try:
        whois.whois(domain)
        return {'disponivel': False}

    except:
        return {'disponivel': True}


def _threads(domains):
    begin = time()
    threads = []
    results = []
    response_data = []

    for domain in domains:
        t = threading.Thread(target=lambda d: results.append(is_registered(d)), args=(domain,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time()
    final = end - begin

    for domain, result in zip(domains, results):
        response_data.append({domain: result})

    print(round( final, 1 ), 'segundos foi o tempo de processamento de 100 requisições paralelas na API')
    print(response_data)
    return response_data

def check_domains(request):
    
    body_bytes = request.body
    body_str = body_bytes.decode('utf-8')
    json_data = json.loads(body_str)
    
    domains = json_data.get('dominios')
    results = _threads(domains)

    # Preparar a resposta como um JSON
    response_data = {'resultados': results}
    return JsonResponse(response_data)

domains = ['facebook.com.br', 'google.com', 'github.com', 'yahoo.com', 'microsoft.com', 'openai.org', 'amazon.com',
            'wikipedia.org', 'reddit.com', 'twitter.com', 'instagram.com', 'linkedin.com', 'netflix.com', 'apple.com', 
            'ebay.com', 'cnn.com', 'nytimes.com', 'stackoverflow.com', 'wordpress.com', 'pinterest.com', 'adobe.com',
            'dropbox.com', 'bbc.com', 'bloomberg.com', 'espn.com', 'foxnews.com', 'nasa.gov', 'paypal.com', 'tumblr.com',
            'msn.com', 'craigslist.org', 'imdb.com', 'cnn.com', 'nbcnews.com', 'forbes.com', 'weather.com', 'yelp.com',
            'wsj.com', 'huffpost.com', 'theguardian.com', 'buzzfeed.com', 'businessinsider.com', 'cnbc.com', 'vice.com', 'wired.com',
            'economist.com', 'techcrunch.com', 'theverge.com', 'mashable.com', 'nationalgeographic.com', 'reuters.com', 'fortune.com', 
            'time.com', 'theatlantic.com', 'pcmag.com', 'cnet.com', 'arstechnica.com', 'wired.co.uk', 'slate.com', 'economist.com', 
            'independent.co.uk', 'variety.com', 'newyorker.com', 'economist.com', 'washingtonpost.com', 'latimes.com', 'usatoday.com', 
            'telegraph.co.uk', 'usnews.com', 'abcnews.com', 'cbsnews.com', 'foxbusiness.com', 'npr.org', 'nypost.com', 'rollingstone.com', 
            'billboard.com', 'pitchfork.com', 'grantland.com', 'pitchfork.com', 'engadget.com', 'gizmodo.com', 'techradar.com', 'polygon.com', 
            'kotaku.com', 'ign.com', 'gamespot.com', 'gameinformer.com', 'pcgamer.com', 'rockpapershotgun.com', 'eurogamer.net', 'wired.com', 
            'arstechnica.com', 'slashdot.org', 'makeuseof.com', 'lifehacker.com', 'howtogeek.com', 'thesweetsetup.com', 'thewirecutter.com', 
            'tomsguide.com', 'pcworl.com']

_threads(domains)


#The Registry database contains ONLY .COM, .NET, .EDU domains and Registrars.