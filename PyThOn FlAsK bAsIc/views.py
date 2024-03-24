from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")



@views.route("/")
def home():
    return render_template("index.html", name="Solo")
             

@views.route("/profile") #type "/profile?name=whatever
def profile(): #Query parameters
    args = request.args
    name = args.get("name")
    return render_template("index.html", name=name)

@views.route("/json")
def get_json(): #Returning JSON data
    return jsonify({
        "name": "Solomon",
        "isFlaskWebsites": True
        })

@views.route("/data") 
def get_data(): #Getting JSON data
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home(): #Redirecting
    return redirect(url_for("views.get_json")) #Redirects to get_json, can change to views.home

