from flask import Flask, request


app = Flask(__name__)


@app.post('/soma')
def soma():
    number = request.get_json()
    total = number['x'] + number['y']
    return {"Resultado": total}, 202


if __name__ == '__main__':
    app.run(debug=True)
