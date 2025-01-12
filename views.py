from flask import Blueprint, render_template,request
import json
views = Blueprint(__name__, "views")

foods = []


#Renders each page
@views.route("/")
def home():
    return render_template("index.html")

@views.route("/donate",methods = ["POST", "GET"])
def donate():
    global foods
    #recieve data from front end
    if request.method == "POST": 
        #gets image
        file = request.files["image"]
        print(file)
        
        #saves the image
        file.save("static/images/" + file.filename)
        
        #Saves image name
        image_name = file.filename

        #Gets json data
        JSON_data = request.form.get("data")
        print(JSON_data)
        
        #Loads each json data
        pars_data = json.loads(JSON_data)
        
        bname = pars_data.get("business-name")
        bemail = pars_data.get("business-email")
        blocation = pars_data.get("business-location")
        d_content = pars_data.get("donation-name")
        d_weight = pars_data.get("donation-weight")
        allergies = pars_data.get("allergies")
        id = pars_data.get("id")

        donatedfood = [bname, bemail, blocation, image_name, d_content, d_weight, allergies, id]
        foods.append(donatedfood)
    return render_template("donate.html")

@views.route("/receive", methods = ["POST","GET"])
def receive():
    global foods
    #recieve data from front end
    if request.method == "POST":
        data = request.get_json()
        print(data)
        id = data["content"]
        id = int(id)
        #Looking to see if id of donation matches id that we have got then removing that whole donation from the foods list because user already received it.
        for donation in foods:
            if id in donation:
                print("DELETED")
                foods.remove(donation)
    return render_template("receive.html",meals = foods,zip = zip)

@views.route("/login")
def login():
    return render_template("login.html")

@views.route("/signup")
def signup():
    return render_template("signup.html")