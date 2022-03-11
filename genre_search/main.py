from flask import Blueprint, jsonify
from db_read import db_read


genre_search_blueprint = Blueprint('genre_search_blueprint', __name__)


@genre_search_blueprint.route('/genre/')
def rating_search_empty():
    return jsonify('Укажите жанр')


@genre_search_blueprint.route('/genre/<genre>/')
def rating_search(genre):
    """Поиск фильмов по Жанру"""
    query = f"""
        SELECT title, description, listed_in
        FROM netflix
        WHERE listed_in LIKE '%{genre}%'
        ORDER BY release_year DESC
        LIMIT 10
        """

    data_read = db_read(query)
    result = []
    for item in data_read:
        result_row = {}
        result_row['title'] = item[0]
        result_row['description'] = item[1]
        result_row['genre'] = item[2]
        result.append(result_row)

    return jsonify(result)
