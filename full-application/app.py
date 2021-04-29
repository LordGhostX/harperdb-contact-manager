import harperdb
from flask import *
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = "SECRET_KEY"
db = harperdb.HarperDB(
    url="https://cloud-1-lordghostx.harperdbcloud.com",
    username="lordghostx",
    password="lordghostx"
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contacts/", methods=["GET", "POST"])
def contacts():
    if request.method == "POST":
        action = request.form.get("action")

        if action == "addContact":
            contact_data = {
                "name": request.form.get("name").strip(),
                "job": request.form.get("job").strip(),
                "email": request.form.get("email").strip(),
                "phone": request.form.get("phone").strip()
            }
            db.insert("contacts_repo", "contacts", [contact_data])

            flash("Successfully added new contact", "success")
            return redirect(url_for("contacts"))

    contacts_data = db.sql("SELECT * FROM contacts_repo.contacts")
    return render_template("contacts.html", contacts_data=contacts_data)


if __name__ == "__main__":
    app.run(debug=True)
