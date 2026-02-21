from flask import Flask, render_template

app = Flask(__name__)

# Dummy data
trips = [
    {"id": 1, "name": "Goa Trip", "date": "2026-03-15"},
    {"id": 2, "name": "Munnar Trip", "date": "2026-04-01"}
]

items_data = {
    1: [
        {"name": "Shoes", "status": 1},
        {"name": "Passport", "status": 0},
        {"name": "Charger", "status": 1}
    ],
    2: [
        {"name": "Jacket", "status": 0},
        {"name": "Camera", "status": 0}
    ]
}

@app.route("/")
def dashboard():
    return render_template("dashboard.html", trips=trips)

@app.route("/trip/<int:trip_id>")
def trip(trip_id):
    trip = next((t for t in trips if t["id"] == trip_id), None)
    items = items_data.get(trip_id, [])

    total = len(items)
    packed = len([i for i in items if i["status"] == 1])
    progress = int((packed/total)*100) if total > 0 else 0

    return render_template("trip.html",
                           trip=trip,
                           items=items,
                           progress=progress)

if __name__ == "__main__":
    app.run(debug=True)