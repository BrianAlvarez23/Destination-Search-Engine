import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, json


app = Flask(__name__)
db = SQL("sqlite:///destinations.db")

@app.route("/")
def index():
        countries = db.execute("SELECT Country FROM destinations ORDER BY Country" )
        modern = db.execute("SELECT Country FROM destinations WHERE Modern = TRUE ORDER BY Country" )
        english = db.execute("SELECT Country FROM destinations WHERE English = TRUE ORDER BY Country" )
        western = db.execute("SELECT Country FROM destinations WHERE Western = TRUE ORDER BY Country" )
        advanced = db.execute("SELECT Country FROM destinations WHERE Advanced = TRUE ORDER BY Country" )
        isolated = db.execute("SELECT Country FROM destinations WHERE Isolated = TRUE ORDER BY Country" )
        coastal = db.execute("SELECT Country FROM destinations WHERE Coastal = TRUE ORDER BY Country" )
        return render_template("index.html", countries=countries, modern=modern, english=english,
        western=western, advanced=advanced,isolated=isolated,coastal=coastal )

@app.route("/bali")
def Bali():
        return render_template("bali.html")

@app.route("/trinidad")
def trinidad():
        return render_template("trinidad.html")

if __name__ == '__main__':
    app.run(debug=True)