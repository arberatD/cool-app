from flask import Flask

app = Flask(__name__)

@app.route('/muhammed', methods=['GET'])
def muhammed():
    return "Hallo, Muhammed!", 200

if __name__ == '__main__':
    app.run(debug=True)
