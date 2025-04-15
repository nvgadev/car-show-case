from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/cars')
def get_cars():
    cars = [
        {
            "model": "Tesla Model S",
            "description": "An all-electric five-door liftback sedan produced by Tesla, Inc.",
            "image": "https://example.com/tesla.jpg",
            "technologies": ["Autopilot", "Electric Powertrain", "Over-the-Air Updates"]
        },
        {
            "model": "BMW i8",
            "description": "A plug-in hybrid sports car developed by BMW.",
            "image": "https://example.com/bmw.jpg",
            "technologies": ["Hybrid Drive", "Carbon Fiber Reinforced Plastic", "Laser Headlights"]
        }
    ]
    return jsonify(cars)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
