from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/home')
def home():
 return "Flask Microservice is running!"


@app.route("/add", methods=["POST"])
def add():

    data = request.get_json()

    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return jsonify({"error": "Both 'a' and 'b' are required"}), 400

    result = a + b

    return jsonify({
        "operation": "addition",
        "result": result
    })
@app.route("/subtract", methods=["POST"])
def subtract():

    data = request.get_json()

    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return jsonify({"error": "Both 'a' and 'b' are required"}), 400

    result = a - b

    return jsonify({
        "operation": "subtraction",
        "result": result
    })
@app.route("/multiply", methods=["POST"])
def multiply():

    data = request.get_json()

    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return jsonify({"error": "Both 'a' and 'b' are required"}), 400

    result = a * b

    return jsonify({
        "operation": "multiplication",
        "result": result
    })
@app.route("/divide", methods=["POST"])
def divide():

    data = request.get_json()

    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return jsonify({"error": "Both 'a' and 'b' are required"}), 400

    if b == 0:
        return jsonify({"error": "Division by zero is not allowed"}), 400

    result = a / b

    return jsonify({
        "operation": "division",
        "result": result
    })

if __name__ == '__main__':
 app.run(debug=True)
