from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/mein-endpunkt', methods=['POST'])
def mein_endpunkt():
    data = request.get_json()
    # Verarbeiten Sie hier Ihre Daten
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
