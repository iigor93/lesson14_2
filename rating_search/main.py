from flask import Blueprint, jsonify
from db_read import db_read


rating_search_blueprint = Blueprint('rating_search_blueprint', __name__)


def rating_query(rating_list):
    query = f"""
        SELECT title, rating, description 
        FROM netflix
        WHERE rating IN {rating_list}
        LIMIT 100
        """
    data_read = db_read(query)
    return data_read


@rating_search_blueprint.route('/rating/')
def rating_search_empty():
    return jsonify('Укажите рейтинг: children, family или adult')



@rating_search_blueprint.route('/rating/<rating>/')
def rating_search(rating):
    """Поиск фильмов по Рейтингу"""
    children = ("G", "TV-G", "TV-Y", "TV-Y7")
    adult = ("TV-MA", "R", "NR", "NC-17")
    family = ("PG-13", "TV-14", "TV-PG", "PG", "TV-Y7-FV", "UR")

    if rating == 'children':
        data_read = rating_query(children)
    elif rating == 'adult':
        data_read = rating_query(adult)
    elif rating == 'family':
        data_read = rating_query(family)
    else:
        data_read = 'Нет такого рейтинга'
        return jsonify(data_read)

    result = []

    for item in data_read:
        result_row = {}
        result_row['title'] = item[0]
        result_row['rating'] = item[1]
        result_row['description'] = item[2]
        result.append(result_row)

    return jsonify(result)
