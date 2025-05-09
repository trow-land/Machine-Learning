# Artemia Tank Monitoring Dashboard (Simulated Data)

This project simulates a real-time monitoring system for Artemia (brine shrimp) culture tanks, intended as a prototype for aquaculture and agritech applications. It combines simulated sensor data with machine learning forecasting and presents the results in a live-updating dashboard using Streamlit.

## Overview

The dashboard:

- Displays live simulated Artemia population counts and temperature readings
- Uses a trained machine learning model to predict future Artemia counts
- Triggers warnings and alerts when population drops are predicted
- Simulates biologically realistic die-off events caused by sustained low temperatures
- Continuously updates every few seconds to mimic a live feed

This is intended as a prototype for applications like early-warning systems in aquaculture environments, particularly where lightweight, deployable systems may be built on devices like Raspberry Pi.

![dashboard](https://github.com/trow-land/Data-Science/blob/main/Artemia_count_dashboard/images/dashboard_snapshot.png)

## Features

- Real-time updating dashboard with line charts and system metrics
- Live simulation of Artemia population and environmental temperature
- Machine learning prediction of next-step Artemia population using historical lag features
- Simulated die-off event if temperature remains below a threshold
- Configurable via local CSV; easily extended to use real sensor input or cloud logging

## File Structure

```
.
├── artemia_dash.py         # Streamlit dashboard code
├── regression_model.joblib      # Pretrained ML model (e.g. LinearRegression)
├── artemia_live.csv             # Live-updating CSV of simulation data
└── README.md
```

## Requirements

- Python 3.8+
- Streamlit
- pandas
- numpy
- scikit-learn
- joblib
- matplotlib

Install dependencies with:

```bash
pip install streamlit pandas numpy scikit-learn joblib matplotlib
```

## Usage

1. Train your regression model in a separate notebook or script using historical data, and save it as a `.joblib` file:

   ```python
   from sklearn.linear_model import LinearRegression
   import joblib
   model = LinearRegression()
   model.fit(X_train, y_train)
   joblib.dump(model, 'regression_model.joblib')
   ```

2. Place the model in the same directory as `artemia_dash.py` or adjust the path accordingly.

3. Launch the dashboard:

   ```bash
   streamlit run artemia_dashboard.py
   ```

4. The dashboard will:

   - Simulate new sensor readings every few seconds
   - Append data to `artemia_live.csv`
   - Recalculate predictions
   - Visualise temperature and population trends
   - Trigger alerts when temperature-induced die-off occurs or prediction suggests major decline

## Customisation

You can modify the simulation behaviour in `artemia_dashboard.py` by adjusting:

- Temperature fluctuation model
- Die-off trigger (e.g. lower threshold or longer exposure)
- Frequency of updates (`time.sleep()`)
- Data source (e.g. replace simulation with real sensor input)

## Future Extensions

- Add image-based object detection (e.g. YOLO or OpenCV-based Artemia counting)
- Deploy on cloud or edge device with scheduled logging and remote access
