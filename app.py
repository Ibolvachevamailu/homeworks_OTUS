from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/")
def home():
    product = {
        "name": "Смарт-часы X100",
        "old_price": "9 990 ₽",
        "new_price": "6 990 ₽",
        "images": [
            {
                "src": url_for("static", filename="images/product-main.svg"),
                "alt": "Смарт-часы X100 крупный план",
            },
            {
                "src": url_for("static", filename="images/product-side.svg"),
                "alt": "Смарт-часы X100 боковой ракурс",
            },
            {
                "src": url_for("static", filename="images/product-back.svg"),
                "alt": "Смарт-часы X100 задняя часть",
            },
        ],
    }
    return render_template("index.html", product=product)


@app.route("/cart")
def cart():
    return render_template("cart.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)