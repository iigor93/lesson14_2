from db_read import db_read
from flask import jsonify


def search_type_year_genre(type_, year, genre):
    """Поиск по типу, году и жанру"""
    available_types = ['TV Show', 'Movie']
    if type_ not in available_types:
        return jsonify(f'Не верный тип фильма, нужно выбрать: {available_types}')

    if year.isdigit() is False or len(year) != 4:
        return jsonify('Не верно указан год')

    query = f"""
            SELECT title, description 
            FROM netflix
            WHERE "type" = "{type_}"
            AND "release_year" = {year}
            AND "listed_in" LIKE '%{genre}%' 

            """

    data_read = db_read(query)
    return jsonify(data_read)
