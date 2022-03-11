from flask import Blueprint, jsonify
from db_read import db_read


year_search_blueprint = Blueprint('year_search_blueprint', __name__)


@year_search_blueprint.route('/<year_start>/to/<year_ends>/')
def year_search(year_start, year_ends):
    """Поиск фильмов по годам"""
    if year_start > year_ends:
        year_start, year_ends = year_ends, year_start


    query = f"""
            SELECT title, release_year 
            FROM netflix
            WHERE release_year BETWEEN {year_start} AND {year_ends}
            ORDER BY release_year
            LIMIT 100
            """
    data_read = db_read(query)
    result = []

    for item in data_read:
        result_row = {}
        result_row['title'] = item[0]
        result_row['release_year'] = item[1]

        result.append(result_row)
    return jsonify(result)
