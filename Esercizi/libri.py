import json

libreria={
    "Libro1": '{ "nome": "Promessi Sposi", "autore": "Alessandro Manzoni", "genere": "Romanzo storico"}',

    "Libro2": '{ "nome": "Piccole Donne", "autore": "Louisa May Alcott", "genere": "Romanzo di formazione"}',

    "Libro3": '{ "nome": "Orgoglio e pregiudizio", "autore": "Jane Austen", "genere": "Dramma"}',

    "Libro4":  '{ "nome": "Il libro della giungla", "autore": "Rudyard Kipling", "genere": "Narrativa"}',

    "Libro5":  '{ "nome": "Harry Potter e la Pietra Filosofale", "autore": "J.K Rowling", "genere": "Romanzo"}',

    "Libro6":  '{ "nome": "Il ritratto di Dorian Gray", "autore": "Oscar Wilde", "genere": "Romanzo"}',

    "Libro7":  '{ "nome": "It", "autore": "Stephen King", "genere": "Horror"}',

    "Libro8":  '{ "nome": "Sherlock Holmes", "autore": "Conan Doyle", "genere": "Giallo"}',

    "Libro9":  '{ "nome": "Grandi Speranze", "autore": "Charles Dickens", "genere": "Avventura"}',

    "Libro10": '{ "nome": "Jane Eyre", "autore": "Charlotte Brontë", "genere": "Romanzo rosa"}'
    }

y = json.loads(libreria["Libro1"])


print(y["genere"])
