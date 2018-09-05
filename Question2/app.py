from flask import Flask
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView

from extensions import db, admin
from models import URL
from settings import Settings
from api import bp


def create_app():
    app = Flask('Shortner')
    app.config.from_object(Settings)
    db.init_app(app)
    admin.init_app(app, index_view=AdminIndexView(url='/shortner/admin'))
    admin.add_view(ModelView(URL, db.session))
    app.register_blueprint(bp)

    return app
