from flask import Flask, request, render_template_string

app = Flask(__name__)
application = app

ziyaretci_listesi = []

HTML = """
<!doctype html>
<html>
<head>
    <title>Buluttan Selam!</title>
    <style>
        body { font-family: Arial; text-align: center; padding: 50px; background: #eef2f3; }
        h1 { color: #333; }
        form { margin: 20px auto; display: flex; flex-direction: column; align-items: center; gap: 10px; }
        input { padding: 10px; font-size: 16px; width: 250px; border-radius: 5px; border: 1px solid #ccc; }
        button { padding: 10px 20px; background: #4CAF50; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: bold; }
        ul { list-style: none; padding: 0; }
        li { background: white; margin: 8px auto; width: 300px; padding: 12px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .city { color: #666; font-size: 0.9em; font-style: italic; }
    </style>
</head>
<body>
    <h1>Buluttan Selam!</h1>
    <p>Bilgilerini yaz, selamını bırak</p>
    
    <form method="POST">
        <input type="text" name="isim" placeholder="Adınızı yazın" required>
        <input type="text" name="sehir" placeholder="Yaşadığınız şehir" required>
        <button type="submit">Selam Gönder</button>
    </form>

    <h3>Son Ziyaretçiler:</h3>
    <ul>
        {% for kisi in ziyaretciler %}
            <li>
                <strong>{{ kisi.ad }}</strong><br>
                <span class="city">📍 {{ kisi.sehir }}</span>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        isim = request.form.get("isim")
        sehir = request.form.get("sehir")

        if isim and sehir:
            ziyaretci_listesi.insert(0, {"ad": isim, "sehir": sehir})
            if len(ziyaretci_listesi) > 10:
                ziyaretci_listesi.pop()

    return render_template_string(HTML, ziyaretciler=ziyaretci_listesi)
