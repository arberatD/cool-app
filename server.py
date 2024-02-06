from flask import Flask

app = Flask(__name__)

@app.route('/muhammed', methods=['GET'])
def muhammed():
    return "Hallo, Muhammed!", 200

@app.route('/')
def home():
    return "Welcome to my Flask API!"

@app.route('/push-force-hard')
def force():
    return "Force push hard"

@app.route('/enrico')
def enrico():
  return jsonify({"name": "Enrico"})

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/flamur')
def flamur():
    return 'Moin'

if __name__ == '__main__':
    app.run(debug=True)
