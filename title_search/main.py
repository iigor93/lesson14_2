from flask import Blueprint, jsonify
from db_read import db_read

title_search_blueprint = Blueprint('title_search_blueprint', __name__)


@title_search_blueprint.route('/movie/')
def title_search_empty():
    return jsonify('Пустой запрос')


@title_search_blueprint.route('/movie/<title_>/')
def title_search(title_):
    """Поиск фильма по названию"""
    query = f"""
        SELECT title, country, release_year, listed_in, description 
        FROM netflix
        WHERE title LIKE '%{title_}%'
        ORDER BY release_year DESC
        LIMIT 1
        """

    result = {}
    data_read = db_read(query)
    if data_read:
        result['title'] = data_read[0][0]
        result['country'] = data_read[0][1]
        result['release_year'] = data_read[0][2]
        result['genre'] = data_read[0][3]
        result['description'] = data_read[0][4]
        return jsonify(result)

    return jsonify('Ничего не найдено')
