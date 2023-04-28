from flask import Flask, request, jsonify
import util
app = Flask(__name__)


@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    return "hi"


if __name__ == "__main__":
    print("starting Python Flash Service")

    app.run(port=5050)
