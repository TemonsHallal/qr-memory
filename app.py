import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    print()
    print("======================================")
    print("        WEBSITE LOVE QR ❤️")
    print("======================================")
    print()
    print(f"Website aktif di port: {port}")
    print()

    app.run(host='0.0.0.0', port=port, debug=False)
