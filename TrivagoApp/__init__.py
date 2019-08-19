import logging

from flask import Flask
from flask_restplus import Api, Resource, fields

import pandas as pd

app = Flask(__name__)
gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.INFO)

api = Api(app=app, version="1.0.0", title="Trivago User Insights",
          description="Trivage User Insights application")
# Nasty hack otherwise model would not disappear from the screen

name_space = api.namespace('', description='Trivago')

parser = api.parser()
parser.add_argument('user_id', type=int, required=True)
parser.add_argument('limit', type=int, required=False, default=10)

# Eager loading as we don't want to load/unload for each request
selection_df = pd.read_csv("/tmp/selections.csv", error_bad_lines=False, header=None, index_col=[1])  # user_id as index
clicks_df = pd.read_csv("/tmp/clicks.csv", error_bad_lines=False, header=None, index_col=[1])

from TrivagoApp import routes