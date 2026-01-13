from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route("/")
def checklist():
    return render_template("checklist.html")

if __name__ == "__main__":
    # Use a non-privileged port (>1024) to avoid permission errors
    app.run(debug=True, host="127.0.0.1", port=4000)
