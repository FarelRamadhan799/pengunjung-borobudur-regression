import joblib
import pandas as pd
import streamlit as st

model = joblib.load("model_forest.joblib")

st.title("Prediksi Pengunjung Borobudur")
st.markdown("Memprediksi jumlah pengunjung Borobudur")

hari_type = st.pills("Hari Type", ["weekend", "weekdays"], default = "weekend")
musim = st.pills("Musim", ["kemarau", "hujan"], default = "kemarau")
suhu_rata_rata = st.slider("Suhu  Rata-rata", 0.0, 50.0, 25.0)
ada_event_budaya = st.pills("Ada Event Budaya?", ["ya", "tidak"], default="ya")
harga_tiket_ribu = st.slider("Harga Tiket(ribu)", 50.0, 100.0, 70.0)

if st.button("prediksi"):
	data_baru = pd.DataFrame([[hari_type, musim, suhu_rata_rata, ada_event_budaya,harga_tiket_ribu]], columns=['hari_type', 'musim', 'suhu_rata_rata', 'ada_event_budaya','harga_tiket_ribu'])
	prediksi = model.predict(data_baru)[0]
	st.success(f"Jumlah Pengunjung yang datang sekitar {prediksi:.0f}")
	st.balloons()
