from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/info")
def info():
    return jsonify(name="Gerardo", song="Corazon")

if __name__ == "__main__":
    app.run()
