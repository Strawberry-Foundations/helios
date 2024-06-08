from helios.core.config import config

from flask import Flask

app = Flask(
    __name__,
    static_url_path=config.static_url_path,
    static_folder=config.static_folder,
    template_folder=config.template_folder
)

# app.config["SECRET_KEY"] = load_secret()