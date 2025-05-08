import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import time

st.title("Artemia Tank Monitor")

model = joblib.load(r"C:\Users\tom_r\Desktop\crime data\Data-Science\Streamlit\regression_model.joblib")

try:
    df = pd.read_csv("artemia_live.csv")
except FileNotFoundError:
    base_count = 130
    times = pd.date_range("00:00", periods=15, freq="1min")
    df = pd.DataFrame({
        'time': times,
        'artemia_count': np.random.randint(base_count, base_count+5, size=15),
        'temperature': np.random.normal(27, 0.3, size=15)
    })
    df.to_csv("artemia_live.csv", index=False)


cool_counter = 0


placeholder = st.empty()

while True:
    # simulate new sensor readings
    new_temp = 27 + np.sin(time.time() / 60) + np.random.normal(0, 0.2)
    new_time = pd.to_datetime(df['time'].iloc[-1]) + pd.Timedelta(minutes=1)

    # cooling condition check
    if new_temp < 26:
        cool_counter += 1
    else:
        cool_counter = 0

    # Normal conditions
    delta = np.random.randint(-2, 3)
    new_count = df['artemia_count'].iloc[-1] + delta

    # If cooling persists for more than 3 cycles then count significantly drops
    if cool_counter >= 3:
        new_count -= np.random.randint(10, 20)
        st.warning("🔥 Cooling event! Artemia count dropped!")

    new_count = max(new_count, 0)

    # save to csv to simulate a new count
    new_row = pd.DataFrame({'time': [new_time], 'artemia_count': [new_count], 'temperature': [new_temp]})
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv("artemia_live.csv", index=False)

    # Prediction and dash displauy
    if len(df) > 14:
        last_values = df['artemia_count'].iloc[-14:].values.reshape(1, -1)
        prediction = model.predict(last_values)[0]
        prev = df['artemia_count'].iloc[-1]

        with placeholder.container():
            st.metric("Current Artemia Count", int(prev))
            st.metric("Current Temperature (°C)", round(new_temp, 2))
            st.metric("Predicted Next Count", round(prediction, 1))

            if prediction < prev * 0.9:
                st.error("⚠️ Predicted count drop >10%! Check tank conditions.")
            elif prediction < prev:
                st.warning("⚠️ Slight drop in population forecast.")
            else:
                st.success("✅ Population trend looks healthy.")

            st.line_chart(df[['artemia_count', 'temperature',]].tail(400))

    time.sleep(2)
