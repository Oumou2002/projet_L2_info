import json

# Je crée dans ce script des twwets factices
tweets = [] # initialisation de tweets vide au debut 

for i in range(1, 5): # pour generer 100 tweets 
    tweet = {  # chaque iteration correspond à un tweet 
        "id": i, # id du tweet 
        "user": f"OUMOU",# utilisateurs
        "text": f"étudiante", # contenu 
        "hashtags": ["#55", "#2"],# Hashtag
        "mentions": ["@mention1", "@mention2"],# utilisateurs mentionnés
        "sentiment": "positif" if i % 2 == 0 else "négatif", #  simulation du  sentiment si i est pair c'est un sentiment positif sinon le sentiment est negatif  
        "entities": {
            "hashtags": [{"text": "hashtag1", "indices": [10, 19]}, {"text": "hashtag2", "indices": [30, 39]}],
            "mentions": [{"username": "mention1", "indices": [5, 14]}, {"username": "mention2", "indices": [25, 34]}]
        },
        "conversation_id": f"conv_{i}"
    }
    tweets.append(tweet)

# Enregistrer la liste de tweets dans un fichier JSON
with open('tweets.json', 'w', encoding='utf-8') as file:
    json.dump(tweets, file, ensure_ascii=False, indent=4)
