from flask import Flask, jsonify
import math

app = Flask(__name__)


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


@app.route("/prime_number/<int:number>")
def prime_number(number):
    response = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)