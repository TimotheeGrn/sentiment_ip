import re
from textblob import TextBlob
import nltk
from urllib.parse import urlparse
import socket

# Assurez-vous d'avoir installé nltk et textblob en utilisant : pip install nltk textblob

def extract_ip(text):
    # Utiliser la bibliothèque TextBlob pour analyser le texte
    blob = TextBlob(text)
    # Extraire les mots clés pertinents pour détecter la demande d'IP
    keywords = ["IP", "adresse", "site", "web"]
    words = [word.lower() for word in blob.words]
    
    # Vérifier si la demande contient des mots clés
    if any(keyword in words for keyword in keywords):
        # Utiliser NLTK pour trouver l'URL dans le texte
        url_pattern = r'https?://\S+'
        urls = re.findall(url_pattern, text)
        if urls:
            url = urls[0]
            parsed_url = urlparse(url)
            domain = parsed_url.netloc
            try:
                # Utiliser la résolution DNS pour obtenir l'adresse IP
                ip_address = socket.gethostbyname(domain)
                return f"L'IP du site {domain} est : {ip_address}"
            except socket.gaierror:
                return f"Impossible de résoudre l'IP du site {domain}."
        else:
            return "Je n'ai pas trouvé d'URL dans votre demande."
    else:
        return "Je n'ai pas compris votre demande concernant l'adresse IP d'un site web."

# Demander à l'utilisateur d'entrer la demande
user_input = input("# ")
result = extract_ip(user_input)
print(result)
