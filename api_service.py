api_service api_service.py from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2, os

app = Flask(__name__)
CORS(app)

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://hello_cloud3_db_5c33_user:v0zPhI7xUyBJiQXRzhSM9dOnUAT8FsJS@dpg-d3tjhd0gjchc73fan1s0-a.oregon-postgres.render.com/hello_cloud3_db_5c33"
)

def connect_db():
    return psycopg2.connect(DATABASE_URL)

@app.route("/ziyaretciler", methods=["GET", "POST"])
def ziyaretciler():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS ziyaretciler (id SERIAL PRIMARY KEY, isim TEXT, sehir TEXT)")

    if request.method == "POST":
        isim = request.json.get("isim")
        sehir = request.json.get("sehir")
        if isim and sehir:
            cur.execute("INSERT INTO ziyaretciler (isim, sehir) VALUES (%s,%s)", (isim, sehir))
            conn.commit()

    cur.execute("SELECT isim, sehir FROM ziyaretciler ORDER BY id DESC LIMIT 10")
    isimler = [{"isim": row[0], "sehir": row[1]} for row in cur.fetchall()]

    cur.close()
    conn.close()

    return jsonify(isimler)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
