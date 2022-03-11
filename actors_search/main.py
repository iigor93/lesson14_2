from flask import Blueprint, jsonify
from db_read import db_read


actor_search_blueprint = Blueprint('actor_search_blueprint', __name__)


@actor_search_blueprint.route('/actor/<first_actor>/<second_actor>/')
def rating_search(first_actor, second_actor):
    """Поиск Актеров которые играли больше чем 2 раза вместе  """
    query = f"""
            SELECT title, "cast"
            FROM netflix
            WHERE "cast" LIKE "%{first_actor}%" AND "cast" LIKE "%{second_actor}%"
            """
    data_read = db_read(query)

    # Список всех актеров (записи могут дублироваться), которые играли с выбранными актерами
    all_actors_list = []

    for item in data_read:
        all_actors_item = item[1].split(', ')
        all_actors_list.extend(all_actors_item)

    # список актеров без повторов
    all_actors_set = set(all_actors_list)

    final_dict = {}

    for item in all_actors_set:
        if all_actors_list.count(item.strip()) > 1:
            if item.strip() != first_actor and item.strip() != second_actor:
                final_dict[item.strip()] = all_actors_list.count(item.strip())

    return jsonify(final_dict)
