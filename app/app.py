from flask import Flask

app = Flask(__name__)
count = 0


@app.route("/")
def hello():
    global count
    count += 1
    return f"Hello GitOps! Visits: {count}\n"


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
