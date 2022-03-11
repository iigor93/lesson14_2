from flask import Flask, jsonify
from title_search.main import title_search_blueprint
from year_search.main import year_search_blueprint
from rating_search.main import rating_search_blueprint
from genre_search.main import genre_search_blueprint
from actors_search.main import actor_search_blueprint


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# route('/movie/<title_>/')
app.register_blueprint(title_search_blueprint)

# route('/<year_start>/to/<year_ends>/')
app.register_blueprint(year_search_blueprint)

# route('/rating/<rating>/')
app.register_blueprint(rating_search_blueprint)

# route('/genre/<genre>/')
app.register_blueprint(genre_search_blueprint)

# actor('/actor/<actor>/<actor>')
app.register_blueprint(actor_search_blueprint)
