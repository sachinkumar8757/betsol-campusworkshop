"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch9t5pu7avjdl28ljvqg-a.oregon-postgres.render.com",
        database="todo_3to8",
        user="root",
        password="Dw8nTtoilKMuP7gCjV4RVsKVK6GdNqa0")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
