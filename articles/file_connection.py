import json


def get_articles():
    with open("articles.json", 'r', encoding='utf-8') as json_file:
        articles_data = json.load(json_file)
    return articles_data


def save_article(name, text):
    with open("articles.json", "r", encoding='utf-8') as file:
        articles = json.load(file)

    articles[name] = text

    with open("articles.json", "w", encoding='utf-8') as file:
        json.dump(articles, file, ensure_ascii=False)


def delete_article(name):
    with open("articles.json", "r", encoding='utf-8') as file:
        articles = json.load(file)

    del articles[name]

    with open("articles.json", "w", encoding='utf-8') as file:
        json.dump(articles, file, ensure_ascii=False)