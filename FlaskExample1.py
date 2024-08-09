


from flask import request, Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    res = {"title": "This is the home Page"}
    ex = request.args.get("extra") # recoge el query (id?extra=<???>) y lo pasa a var = ex
    res['extra'] = ex
    return jsonify(res), 200


@app.route("/id/<manual_id>/", methods=['GET'])
def id(manual_id):
    res = {"res": f" from def id(manual_id) = {manual_id}"}
    ex = request.args.get("extra") # recoge el query (id?extra=<???>) y lo pasa a var = ex
    res['extra'] = ex
    return jsonify(res), 200


@app.route("/db/<db_id>")
def db_id(db_id):
    res = {"res": f" from db id(db_id) = {db_id}"}
    ex = request.args.get("extra") # recoge el query (id?extra=<???>) y lo pasa a var = ex
    res['extra'] = ex
    return jsonify(res), 200


@app.route("/create", methods=['POST'])
def create():
    body = request.get_json()
    return jsonify(body), 202


if __name__ == '__main__':
    app.run(debug=True)