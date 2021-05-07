from flask import *
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")


@app.route("/contacts/delete/<string:contact_id>")
def delete_contact(contact_id):
    return redirect(url_for("contacts"))


if __name__ == "__main__":
    app.run(debug=True)
