# Copyright 2023 Strawberry Foundations (matteodev8)

from flask import Flask, template_renderer

app = Flask(__name__)


@app.route("/")
def home():
    return template_renderer('index.html')
