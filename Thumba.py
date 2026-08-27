import streamlit as st
import datetime
import math

st.set_page_config(page_title="Thumba to Space", page_icon="🚀")

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #000000 0%, #0a0a23 50%, #1a1a3e 100%);
        color: white;
    }
    h1, h2, h3, p, div, label { color: white !important; }
    .stApp::before {
        content: "";
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, #eee, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 40px 70px, #fff, rgba(0,0,0,0));
        background-repeat: repeat; background-size: 200px 200px;
        z-index: -1;
    }
</style>
""", unsafe_allow_html=True)

st.title("Thumba to Space 🚀")
st.subheader("From Thiruvananthapuram to the Stars")
st.write("India's space journey started in Thumba!")
st.write("Built from Kilimanoor, Trivandrum!")

next_launch = datetime.datetime(2026, 9, 15, 10, 30)
now = datetime.datetime.now()
diff = next_launch - now
col1, col2, col3 = st.columns(3)
col1.metric("Days", diff.days)
col2.metric("Hours", diff.seconds//3600)
col3.metric("Next", "Gaganyaan")

st.divider()
st.header("🚀 Kilimanoor Rocket Builder")
name = st.text_input("Your Name from Kilimanoor:")
if st.button("Launch from Thumba!"):
    if name:
        st.snow()
        st.success(f"{name} launched from Thumba! Jai Hind!")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Thumba_Equatorial_Rocket_Launching_Station.jpg/330px-Thumba_Equatorial_Rocket_Launching_Station.jpg")
        st.write("Thumba is only 30km from Kilimanoor! Same district!")
    else:
        st.warning("Enter your name da!")

st.divider()
st.header("📰 1963 - THUMBA TIMES")
st.write("**Date: 21st Nov 1963 | Place: Thumba, Trivandrum**")
st.write("> 'On this day, a small fishing village launched India to the stars. The rocket was carried on a BICYCLE!'")

col_a, col_b = st.columns(2)
with col_a:
    st.subheader("🚲 Bicycle Rocket!")
    st.write("First rocket parts came on cycle. No trucks then!")
    if st.button("Hear the Old Story"):
        st.info("Dr. APJ Abdul Kalam says: We pushed rocket on bicycle from church to launch pad!")
        st.info("Dr. Vikram Sarabhai was there!")
with col_b:
    st.subheader("⛪ Church = Control Room!")
    st.write("St. Mary Magdalene Church was our first control center!")
    if st.button("View Old Photo"):
        st.snow()
        st.success("Imagine - Church bells and rocket countdown together!")

st.divider()
st.subheader("🛰️ Your Kilimanoor Mission Control")
mission = st.slider("Select Launch Power %", 0, 100, 75)
st.progress(mission)
if mission > 90:
    st.write("🔥 ROCKET READY TO LAUNCH FROM THUMBA! JAI HIND!")
elif mission > 50:
    st.write("⛽ Fueling from Kilimanoor...")
else:
    st.write("🛠️ Building in Raja Ravi Varma's Art Studio...")

st.divider()
st.write("### 📜 Why Kilimanoor to Thumba?")
st.write("Kilimanoor gave India art (Raja Ravi Varma). Thumba gave India space. You connect both!")
dream = st.text_input("What will Kilimanoor launch next?", placeholder="My dream rocket...")
if dream:
    st.success(f"🚀 Kilimanoor will launch: {dream} - Let's go!")
    st.snow()

st.divider()
st.header("🇮🇳 Chandrayaan-3 - We landed on Moon! 🌙")
st.snow()
c1, c2 = st.columns(2)
with c1:
    st.subheader("Aug 23, 2023")
    st.write("India became 1st country to land on Moon's South Pole!")
    st.metric("Mission", "Success", "100%")
with c2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Chandrayaan-3_lander.jpg/640px-Chandrayaan-3_lander.jpg", caption="Vikram Lander")
st.success("From Thumba bicycles to Moon landing - What a journey!")
if st.button("Celebrate with ISRO! 🎉"):
    st.snow()
    st.write("Jai Hind! 🇮🇳")

st.divider()
st.header("🧠 ISRO Quiz - 5 Questions")
q1 = st.radio("1. Where did India launch first rocket in 1963?", ["Thumba", "Delhi", "Sriharikota"], key="q1")
if q1 == "Thumba": st.success("Correct! Thumba, Trivandrum! 🚀")
else: st.error("Nope! It's Thumba!")
q2 = st.radio("2. When did Chandrayaan-3 land?", ["2023", "2020", "2024"], key="q2")
if q2 == "2023": st.success("Yes! Aug 23, 2023! 🌙")
else: st.error("Try again!")
q3 = st.radio("3. Who is the father of Indian space program?", ["Dr. Vikram Sarabhai", "Dr. APJ Abdul Kalam", "Dr. Homi Bhabha"], key="q3")
if q3 == "Dr. Vikram Sarabhai": st.success("Whoa! You're an ISRO fan!")
else: st.error("It's Dr. Vikram Sarabhai!")
q4 = st.radio("4. What was the first control room for ISRO?", ["St. Mary Magdalene Church", "ISRO HQ", "Raja Ravi Varma Studio"], key="q4")
if q4 == "St. Mary Magdalene Church": st.success("Yes! Church was first control room! ⛪")
else: st.error("It was the Church!")
q5 = st.radio("5. What is the next big mission after Chandrayaan-3?", ["Gaganyaan", "Mars Mission", "PSLV-C51"], key="q5")
if q5 == "Gaganyaan": st.success("Hooray! Gaganyaan is next!")
else: st.error("It's Gaganyaan!")

st.divider()
st.header("🎨 From Kilimanoor")
st.write("My hometown Kilimanoor is famous for Raja Ravi Varma - India's greatest painter!")
col1, col2 = st.columns(2)
col1.metric("Raja Ravi Varma", "1848-1906", "Painter")
col2.metric("Thumba First Launch", "1963", "Rocket")

st.divider()
st.header("📅 India's Space Timeline")
year = st.slider("Drag to time travel!", 1963, 2024, 1963)
if year == 1963: st.write("🚲 1963: Rocket carried on bicycle in Thumba!")
elif year < 1980: st.write("🔬 ISRO formed! Learning years.")
elif year < 2008: st.write("🛰️ Building satellites!")
elif year < 2023: st.write("🚀 Mangalyaan to Mars! 2014")
else: st.write("🌙 2023: Moon South Pole! India #1!")

st.divider()
st.header("🎵 Space Vibes - M83 Outro")
st.write("Best song for ISRO journey!")
st.video("https://www.youtube.com/watch?v=S_CKyXG3kA0")
if st.button("🚀 Launch with M83 Music!"):
    st.snow()
    st.success("Playing Outro - From Thumba to Stars ✨")

st.divider()
st.header("🌌 Live Space View")
st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800", caption="Thumba to Space", use_container_width=True)
m1, m2, m3 = st.columns(3)
m1.metric("🚀 ISRO Missions", "130+", "Growing")
m2.metric("🛰️ Satellites", "400+", "In Orbit")
m3.metric("🌙 Moon Landing", "2023", "Success!")
if st.button("🌠 Enter Deep Space Mode"):
    st.snow()
    st.success("Welcome to Deep Space! 384,400 km from Earth!")

st.divider()
st.header("🚀 LEVEL 2 - REAL SPACE SIMULATOR - NEW!")
st.subheader("1️⃣ Rocket Launch Physics from Thumba")
thrust = st.slider("Thrust Power (kN)", 100, 2000, 800)
fuel = st.slider("Fuel kg", 1000, 10000, 5000)
if st.button("IGNITE ENGINES! 🔥"):
    velocity = thrust * 10 / fuel * 100
    altitude = velocity * 5
    st.snow()
    st.progress(min(int(velocity), 100))
    st.metric("Velocity", f"{int(velocity)} m/s")
    st.metric("Altitude", f"{int(altitude)} km")
    if altitude > 100:
        st.success(f"🚀 YOU REACHED SPACE! Karman Line crossed! {altitude}km!")
        st.snow()
    else:
        st.warning(f"Almost! {altitude}km - Need 100km for space!")

st.divider()
st.subheader("2️⃣ Orbit Around Earth Simulator")
angle = st.slider("Orbit Angle", 0, 360, 0)
r = 150
x = r * math.cos(math.radians(angle))
y = r * math.sin(math.radians(angle))
st.write(f"Satellite Position: X={int(x)}, Y={int(y)} | Angle {angle} deg")
st.markdown(f"""
<div style="width:300px;height:300px;border:2px solid white;border-radius:50%;margin:auto;position:relative;background:radial-gradient(circle at center, #1a1a3e 0%, #000 70%);">
    <div style="position:absolute;left:50%;top:50%;width:40px;height:40px;background:linear-gradient(#4CAF50,#2196F3);border-radius:50%;transform:translate(-50%,-50%);"></div>
    <div style="position:absolute;left:{150 + x/2}px;top:{150 + y/2}px;width:10px;height:10px;background:white;border-radius:50%;transform:translate(-50%,-50%);box-shadow:0 0 10px white;"></div>
</div>
""", unsafe_allow_html=True)
st.caption("Earth in center (blue/green), Satellite white dot - Drag slider!")

st.divider()
st.subheader("3 - Deep Space Star Density")
stars = st.slider("How deep into space?", 0, 100, 50)
st.write("Stars:" + "*"*(stars//10) + f" {stars}% deep")
if stars > 80:
    st.success("You are in Interstellar space! Like M83 Outro song!")
    st.snow()

st.divider()
st.write("Made with love from Kilimanoor, Kerala | Thumba to Space 2026")