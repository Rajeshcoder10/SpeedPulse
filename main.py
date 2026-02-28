import speedtest

st = speedtest.Speedtest(secure=True)

print("🔎 Finding Best Server...\n")
best = st.get_best_server()

print("=" * 50)
print("        🌐 BEST SERVER DETAILS")
print("=" * 50)

print(f"📍 Location     : {best['name']}, {best['country']}")
print(f"🏢 Sponsor      : {best['sponsor']}")
print(f"🖥️  Host        : {best['host']}")
print(f"📡 Server ID    : {best['id']}")
print(f"📏 Distance     : {round(best['d'], 2)} km")
print(f"⚡ Latency      : {best['latency']} ms")

print("=" * 50)
