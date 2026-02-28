import speedtest
import time

print("\n🚀 SPEEDPULSE - Internet Speed Tester\n")
print("Initializing...\n")

st = speedtest.Speedtest(secure=True)

# ------------------ BEST SERVER ------------------ #
print("🔎 Finding Best Server...\n")
best = st.get_best_server()

print("=" * 60)
print("               🌐 SERVER REPORT")
print("=" * 60)

print(f"📍 City            : {best['name']}")
print(f"🌎 Country         : {best['country']} ({best['cc']})")
print(f"📌 Coordinates     : {best['lat']} , {best['lon']}")
print(f"🏢 ISP Sponsor     : {best['sponsor']}")
print(f"🖥️  Host Server     : {best['host']}")
print(f"🔗 Upload URL      : {best['url']}")
print(f"📡 Server ID       : {best['id']}")
print(f"📏 Distance        : {round(best['d'], 2)} km")
print(f"⚡ Latency         : {round(best['latency'], 2)} ms")

print("=" * 60)


# ------------------ SPEED TEST ------------------ #
print("\n📥 Testing Download Speed...")
#time.sleep(1)
download_speed = st.download() / 1_000_000  # Convert to Mbps

print("📤 Testing Upload Speed...")
#time.sleep(1)
upload_speed = st.upload() / 1_000_000  # Convert to Mbps


# ------------------ FINAL RESULTS ------------------ #
print("\n" + "=" * 60)
print("               📊 SPEED TEST RESULTS")
print("=" * 60)

print(f"⬇️  Download Speed : {round(download_speed, 2)} Mbps")
print(f"⬆️  Upload Speed   : {round(upload_speed, 2)} Mbps")

print("=" * 60)
print("\n✅ Test Completed Successfully!\n")

