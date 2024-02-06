from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/enrico')
def test():
  return jsonify({"name": "Enrico"})


