import speedtest

st = speedtest.Speedtest(secure=True)

print("🔎 Finding Best Server...\n")
best = st.get_best_server()

print("=" * 60)
print("               🌐 SPEEDPULSE SERVER REPORT")
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
