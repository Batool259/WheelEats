from flask import Flask, render_template, request

app = Flask(__name__)

# ➜ Beispiel-Daten für WheelEats
restaurants = [
    {
        "id": 1,
        "name": "Restaurant Maximilians",
        "address": "Friedrichstraße 185-190, 10117 Berlin",
        "district": "Mitte",
        "cuisine": "Deutsche Küche",
        "features": ["step_free", "toilet", "spacious"],
    },
    {
        "id": 2,
        "name": "Pizzeria Bella Italia",
        "address": "Friedrichstraße 45, 10117 Berlin",
        "district": "Mitte",
        "cuisine": "Italienisch",
        "features": ["step_free", "toilet"],
    },
    {
        "id": 3,
        "name": "Curry 36",
        "address": "Mehringdamm 36, 10961 Berlin",
        "district": "Kreuzberg",
        "cuisine": "Imbiss",
        "features": ["step_free"],
    },
]


@app.route("/")
def index():
    # Werte aus der URL holen, z.B. /?q=pizza&district=Mitte
    q = request.args.get("q", "").lower()          # Suchtext
    district = request.args.get("district", "")    # Stadtteil
    feature = request.args.get("feature", "")      # Barriere-Merkmal

    # Stadtteile-Liste für das Dropdown
    districts = sorted({r["district"] for r in restaurants})

    # Restaurants nach Filtern durchsuchen
    filtered = []
    for r in restaurants:
        # Textsuche in Name, Adresse, Küche
        if q:
            text = (r["name"] + r["address"] + r["cuisine"]).lower()
            if q not in text:
                continue

        # Stadtteil-Filter
        if district and r["district"] != district:
            continue

        # Barriere-Feature-Filter
        if feature and feature not in r["features"]:
            continue

        filtered.append(r)

    return render_template(
        "index.html",
        restaurants=filtered,
        q=q,
        district=district,
        feature=feature,
        districts=districts,
    )


@app.route("/restaurants")
def restaurants_page():
    return render_template("restaurants.html", restaurants=restaurants)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/add")
def add_page():
    return render_template("add.html")




if __name__ == "__main__":
    app.run(debug=True)