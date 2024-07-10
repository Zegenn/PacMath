from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


# Route untuk halaman utama
@app.route("/")
def index():
    return render_template("index.html")


# Route untuk menghandle permintaan download aplikasi
@app.route("/download/<path:filename>")
def download(filename):
    directory = "static/downloads/"
    return send_from_directory(directory, filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
