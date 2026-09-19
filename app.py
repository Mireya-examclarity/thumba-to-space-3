from flask import Flask, render_template_string
import requests, math, datetime

app = Flask(__name__)

def get_apod():
    try:
        r = requests.get("https://api.nasa.gov/planetary/apod", params={"api_key":"DEMO_KEY"}, timeout=10).json()
        return r
    except: return None

def get_iss():
    try:
        r = requests.get("http://api.open-notify.org/iss-now.json", timeout=10).json()
        return r
    except: return None

HTML = """
<!DOCTYPE html>
<html><head>
<title>Thumba to Space 🚀</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body { background: linear-gradient(180deg,#000,#05051a,#10102d); color:white; font-family: 'Space Grotesk', sans-serif; margin:0; }
.hero { padding:45px 20px; text-align:center; border-radius:25px; background:linear-gradient(135deg,rgba(30,30,80,.95),rgba(0,0,0,.95)); border:1px solid rgba(255,255,255,.15); margin:20px; }
.card { background:rgba(255,255,255,.06); border:1px solid rgba(255,255,255,.12); border-radius:20px; padding:22px; margin:15px 20px; }
.glow { text-shadow: 0 0 5px #fff, 0 0 10px #7aa2ff, 0 0 20px #536dfe; }
.timeline { padding:20px; border-left:4px solid #536dfe; background:rgba(255,255,255,.04); border-radius:10px; margin:20px; }
button { background:#536dfe; color:white; border:none; padding:12px 20px; border-radius:10px; cursor:pointer; }
input { padding:10px; border-radius:8px; width:60%; }
</style>
</head><body>

<div class="hero">
<h1 class="glow">🚀 THUMBA TO SPACE</h1>
<h3>From Thiruvananthapuram to the Stars 🌌</h3>
<p>India's journey - Thumba to Moon, Mars and beyond.</p>
<div style="font-size:50px;">🇮🇳 🚀 🌍 🌙 🛰️</div>
</div>

<div class="card">
<h2>⏱️ Next Mission: Gaganyaan - {{ days }} Days</h2>
<p>Launch: 15 Sep 2026</p>
</div>

<div class="card">
<h2>🇮🇳 The Beginning - Thumba - 21 Nov 1963</h2>
<p>India's sounding rocket program began at Thumba, near Thiruvananthapuram, Kerala - near magnetic equator.</p>
</div>

<div class="card">
<h2>🚀 Kilimanoor Rocket Builder</h2>
<form method="get">
<input name="name" placeholder="Commander name...">
<button>🔥 LAUNCH FROM THUMBA</button>
</form>
{% if launch_name %}<h3>🚀 Commander {{ launch_name }}, Launched!</h3><div style="font-size:80px;text-align:center;">🚀<br>THUMBA → SPACE</div>{% endif %}
</div>

<div class="card">
<h2>🇮🇳 Chandrayaan-3 🌙 - SUCCESS 23 Aug 2023</h2>
<p>India landed near lunar south pole.</p>
</div>

<div class="card">
<h2>🧠 ISRO Quiz</h2>
<p>1. Thumba location? <b>Thumba</b><br>2. Chandrayaan-3? <b>2023</b><br>3. Father? <b>Vikram Sarabhai</b><br>4. Human spaceflight? <b>Gaganyaan</b><br>5. Mangalyaan? <b>Mars</b></p>
</div>

<div class="timeline">
<h2>📅 India's Space Timeline</h2>
<p>1963 - First sounding rocket Thumba</p>
<p>1969 - ISRO established</p>
<p>1975 - Aryabhata</p>
<p>2013 - MOM launched</p>
<p>2023 - Chandrayaan-3 Moon landing</p>
<p>2026 - Gaganyaan</p>
</div>

<div class="card">
<h2>🌌 NASA APOD</h2>
{% if apod and apod.media_type == 'image' %}
<h3>{{ apod.title }}</h3>
<img src="{{ apod.url }}" style="width:100%; border-radius:15px;">
<p>{{ apod.explanation[:500] }}</p>
{% else %}<p>NASA APOD loading...</p>{% endif %}
</div>

<div class="card">
<h2>🎬 From Earth to Space</h2>
<iframe width="100%" height="315" src="https://www.youtube.com/embed/WeA7edXsU40"></iframe>
<h2 style="margin-top:30px;">🎵 Space Vibes - M83</h2>
<iframe width="100%" height="315" src="https://www.youtube.com/embed/1H4B7Zp2w1Y"></iframe>
</div>

<div class="card">
<h2>🛰️ LIVE ISS TRACKER</h2>
{% if iss %}<p>Lat: {{ iss.iss_position.latitude }}, Lon: {{ iss.iss_position.longitude }}</p>{% endif %}
<p>ISS is moving fast over Earth!</p>
</div>

<div class="card"><h2>🔴 Mars Explorer</h2><p>Mars is most explored beyond Earth.</p></div>

<div class="card"><h2>🇮🇳🤝🇺🇸 ISRO x NASA - NISAR</h2><p>Joint Earth observation mission.</p></div>

<div class="card">
<h2>🚀 Rocket Simulator</h2>
<p>Thrust 800kN, Fuel 5000kg = Estimated 160km - SPACE REACHED!</p>
</div>

<div class="card">
<h2>🌱 Kilimanoor → Moon - 384,400 km journey</h2>
<div style="text-align:center; font-size:28px;">🚀 ━━━━━━━━━━ 🌙 - MOON REACHED!</div>
</div>

<div class="card" style="text-align:center;">
<h2>🌱 Meet Kuttan - The Tree-Naut 🚀</h2>
<div style="font-size:100px;">🌱</div>
<p>Your space-loving tree companion from Kilimanoor!</p>
</div>

<div style="text-align:center; padding:40px; color:#8890b5;">
🚀 <b>THUMBA TO SPACE</b> 🚀<br><br>Made with 💚 by Advika<br>Thumba → Kilimanoor → Moon → Mars → Beyond<br>🇮🇳 India to the Stars 🌌
</div>

</body></html>
"""

@app.route("/")
def home():
    name = app.config.get('name') # dummy
    launch_name = __import__('flask').request.args.get('name')
    apod = get_apod()
    iss = get_iss()
    next_launch = datetime.datetime(2026,9,15,10,30)
    diff = next_launch - datetime.datetime.now()
    days = diff.days if diff.total_seconds()>0 else 0
    return render_template_string(HTML, apod=apod, iss=iss, launch_name=launch_name, days=days)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)