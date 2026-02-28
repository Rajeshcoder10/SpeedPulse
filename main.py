import speedtest

st = speedtest.Speedtest()

print("Finding best server...")
st.get_best_server()

print("Download Speed:")
print(round(st.download() / 1_000_000, 2), "Mbps")

print("Upload Speed:")
print(round(st.upload() / 1_000_000, 2), "Mbps")