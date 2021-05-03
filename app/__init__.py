import flask,requests,json 
import jinja2
from authlib.flask.client import OAuth
from flask import Flask, redirect, url_for, render_template, request, flash

app = flask.Flask(__name__)

@app.route("/")
def home_view():
    return "<p>hello</p>"
@app.route("/test")
def test():
	return "<p> This is working good,</p>"



@app.route("/abc")
def abc():
    return jsonify(
                message="good test",
                category="success",
                data=data,
                status=200
            )
