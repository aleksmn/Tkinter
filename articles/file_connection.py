import json


def get_articles():
    with open("articles.json", 'r', encoding='utf-8') as json_file:
        articles_data = json.load(json_file)
    return articles_data


def save_article(name, text):
    # Получим все статьи
    articles = get_articles()
    # Добавляем статью
    articles[name] = text
    # Переписываем файл. w -  write - открыть файл для записи
    with open("articles.json", "w", encoding='utf-8') as json_file:
        json.dump(articles, json_file, ensure_ascii=False)



def delete_article(name):
    # Получим все статьи
    articles = get_articles()
    # Удаляем статью
    del articles[name]
    # Переписываем файл. w -  write - открыть файл для записи
    with open("articles.json", "w", encoding='utf-8') as json_file:
        json.dump(articles, json_file, ensure_ascii=False)



if __name__ == "__main__":
    print(get_articles())

    # save_article("Тестовая статья", "Тест тест тест")
    # delete_article("Тестовая статья")
