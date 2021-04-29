import harperdb
from flask import *
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = "SECRET_KEY"
db = harperdb.HarperDB(
    url="HARPERDB_URL",
    username="HARPERDB_USERNAME",
    password="HARPERDB_PASSWORD"
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contacts/", methods=["GET", "POST"])
def contacts():
    if request.method == "POST":
        action = request.form.get("action")
        contact_data = {
            "name": request.form.get("name", "").strip(),
            "job": request.form.get("job", "").strip(),
            "email": request.form.get("email", "").strip(),
            "phone": request.form.get("phone", "").strip()
        }

        if action == "addContact":
            db.insert("contacts_repo", "contacts", [contact_data])
            flash("Successfully added new contact", "success")
        if action == "updateContact":
            contact_data["contact_id"] = request.form.get("contactID")
            db.update("contacts_repo", "contacts", [contact_data])
            flash("Successfully updated contact information", "success")

        return redirect(url_for("contacts"))

    contacts_data = db.sql(
        "SELECT * FROM contacts_repo.contacts ORDER BY name")
    return render_template("contacts.html", contacts_data=contacts_data)


@app.route("/contacts/delete/<string:contact_id>")
def delete_contact(contact_id):
    db.delete("contacts_repo", "contacts", [contact_id])
    flash("Successfully deleted contact information", "success")
    return redirect(url_for("contacts"))


if __name__ == "__main__":
    app.run(debug=True)
