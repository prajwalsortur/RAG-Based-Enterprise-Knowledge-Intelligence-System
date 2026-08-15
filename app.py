"""
Food Waste Analytics for Restaurants — Streamlit dashboard.

Phase 3 (EDA) is fully wired up: filters, KPIs, and charts over the
synthetic/real waste_data.csv.

Phase 6-8 skeleton (GenAI layer + chat) is stubbed out in the sidebar tab
"Ask the analyst" — plug in your chosen LLM API in `call_llm()` once you've
picked a provider. The rest of the app (data loading, filtering, aggregation)
does not depend on that choice.

Run:
    streamlit run app.py
"""
import base64
import pandas as pd
import plotly.express as px
import streamlit as st
import joblib
import os

from genai_layer import ask_gemini

st.set_page_config(
    page_title="Food Waste Analytics", 
    layout="wide"
    )

def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(
            image_file.read()
        ).decode()

    st.markdown(
        f"""
        <style>

        /* ================================
           BACKGROUND
           ================================ */

        .stApp {{
            background-image:
                linear-gradient(
                    rgba(0, 0, 0, 0.45),
                    rgba(0, 0, 0, 0.45)
                ),
                url("data:image/png;base64,{encoded_image}");

            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        [data-testid="stHeader"] {{
            background: rgba(0, 0, 0, 0);
        }}

        [data-testid="stSidebar"] {{
            background: rgba(0, 0, 0, 0.75);
        }}


        /* ================================
           GENERAL TEXT
           ================================ */

        .stApp p,
        .stApp label {{
            color: #f5f5f5;
        }}

        h1, h2, h3 {{
            color: #ffffff !important;
            font-weight: 700 !important;
        }}

        [data-testid="stCaptionContainer"] {{
            color: #dddddd !important;
        }}


        /* ================================
           CLEAN KPI CARDS
           ================================ */

        [data-testid="stMetric"] {{
            background: #ffffff !important;
            border-radius: 14px !important;
            padding: 20px !important;
            border: 1px solid #e5e7eb !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.12) !important;
        }}

        /* KPI LABEL */

        [data-testid="stMetric"] [data-testid="stMetricLabel"],
        [data-testid="stMetric"] [data-testid="stMetricLabel"] *,
        [data-testid="stMetric"] label,
        [data-testid="stMetric"] label * {{
            color: #555555 !important;
            -webkit-text-fill-color: #555555 !important;
        }}

        /* KPI VALUE */

        [data-testid="stMetric"] [data-testid="stMetricValue"],
        [data-testid="stMetric"] [data-testid="stMetricValue"] *,
        [data-testid="stMetric"] [data-testid="stMetricValue"] div,
        [data-testid="stMetric"] [data-testid="stMetricValue"] span {{
            color: #222222 !important;
            -webkit-text-fill-color: #222222 !important;
            font-size: 30px !important;
            font-weight: 700 !important;
        }}

        /* KPI DELTA */

        [data-testid="stMetric"] [data-testid="stMetricDelta"],
        [data-testid="stMetric"] [data-testid="stMetricDelta"] * {{
            color: #555555 !important;
            -webkit-text-fill-color: #555555 !important;
        }}

        /* FORCE DARK TEXT INSIDE WHITE METRIC CARDS */

        [data-testid="stMetric"] * {{
            color: #222222 !important;
        }}

        [data-testid="stMetric"] label,
        [data-testid="stMetric"] label * {{
            color: #555555 !important;
        }}


        /* ================================
           TABS
           ================================ */

        button[data-baseweb="tab"] {{
            color: #ffffff !important;
            font-weight: 600 !important;
        }}


        /* ================================
           AI TEXT INPUT
           ================================ */

        .stTextInput input {{
            background-color: rgba(255, 255, 255, 0.95) !important;
            color: #111111 !important;
            border: 2px solid #4CAF50 !important;
            border-radius: 10px !important;
        }}

        .stTextInput label {{
            color: #ffffff !important;
            font-weight: 600 !important;
        }}


        /* ================================
           BUTTONS
           ================================ */

        /* PREDICT WASTE BUTTON */

.stButton button {{
    background-color: #ffffff !important;
    color: #222222 !important;
    border: 2px solid #4CAF50 !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    padding: 10px 24px !important;
}}

.stButton button:hover {{
    background-color: #4CAF50 !important;
    color: #ffffff !important;
    border: 2px solid #4CAF50 !important;
}}

.stButton button p {{
    color: #222222 !important;
    font-weight: 700 !important;
}}

.stButton button:hover p {{
    color: #ffffff !important;
}}

        </style>
        """,
        unsafe_allow_html=True
    )

BACKGROUND_PATH = os.path.join(
    os.path.dirname(__file__),
    "assets",
    "dashboard_background.png"
)

set_background(BACKGROUND_PATH)
DATA_PATH = "data/waste_data.csv"
MODEL_PATH = "models/waste_model.pkl"

model = joblib.load(MODEL_PATH)
if "predicted_waste" not in st.session_state:
    st.session_state.predicted_waste = None

if "forecast_date" not in st.session_state:
    st.session_state.forecast_date = None

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"])
    return df


def build_structured_summary(df: pd.DataFrame) -> dict:
    """
    Phase 6 building block: turn filtered data into a compact, pre-computed
    JSON-able summary. This — NOT the raw dataframe — is what gets sent to
    the LLM later. Keeps numbers grounded and avoids hallucination.
    """
    if df.empty:
        return {}
    top_dish = df.groupby("dish_name")["wasted_qty"].sum().idxmax()
    top_dish_qty = df.groupby("dish_name")["wasted_qty"].sum().max()
    return {
        "date_range": [str(df["date"].min().date()), str(df["date"].max().date())],
        "total_waste_qty": round(df["wasted_qty"].sum(), 1),
        "total_waste_cost": round(df["waste_cost"].sum(), 2),
        "top_wasted_dish": top_dish,
        "top_wasted_dish_qty": round(top_dish_qty, 1),
        "avg_waste_weekday": round(df[~df["is_weekend"]]["wasted_qty"].mean(), 2),
        "avg_waste_weekend": round(df[df["is_weekend"]]["wasted_qty"].mean(), 2),
        "avg_waste_rainy": round(df[df["weather"] == "rainy"]["wasted_qty"].mean(), 2)
        if (df["weather"] == "rainy").any() else None,
    }


def call_llm(question: str, summary: dict) -> str:
    """Send the user's question and structured data to Gemini."""
    return ask_gemini(question, summary)
    """
    Placeholder for Phase 6/7. Swap this out once you pick an LLM API
    (OpenAI / Anthropic / Gemini). The pattern stays the same regardless
    of provider:

        system_prompt = "You are a restaurant operations analyst. Only use
        the numbers provided below. Never invent figures."
        context = json.dumps(summary)
        response = <provider_client>.chat(system_prompt, context, question)
        return response.text

    For now this returns a canned response so the UI is testable end to end.
    """
    return (
        "[LLM not yet connected] Based on the current filters, total waste "
        f"cost is ₹{summary.get('total_waste_cost', 0):,.2f}, and "
        f"'{summary.get('top_wasted_dish', 'N/A')}' is the top wasted dish. "
        "Wire up your chosen LLM API in call_llm() to get a real narrative answer here."
    )


# ---------- Load & filter ----------
df = load_data(DATA_PATH)
# Load feature-engineered data for ML predictions

FEATURE_DATA_PATH = "data/waste_features.csv"

ml_df = load_data(FEATURE_DATA_PATH)

st.sidebar.header("Filters")
date_min, date_max = df["date"].min().date(), df["date"].max().date()
date_range = st.sidebar.date_input("Date range", (date_min, date_max), min_value=date_min, max_value=date_max)
dishes = st.sidebar.multiselect("Dishes", sorted(df["dish_name"].unique()), default=list(df["dish_name"].unique()))
weather_filter = st.sidebar.multiselect("Weather", sorted(df["weather"].unique()), default=list(df["weather"].unique()))

mask = (
    (df["date"].dt.date >= date_range[0])
    & (df["date"].dt.date <= date_range[1])
    & (df["dish_name"].isin(dishes))
    & (df["weather"].isin(weather_filter))
)
fdf = df[mask]

st.title("Food waste analytics")
st.caption("Understand, predict, and (soon) explain restaurant food waste.")

# ---------- KPIs ----------
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total waste (units)", f"{fdf['wasted_qty'].sum():,.0f}")
c2.metric("Total waste cost", f"₹{fdf['waste_cost'].sum():,.0f}")
c3.metric("Avg waste / day", f"{fdf.groupby('date')['wasted_qty'].sum().mean():,.1f}")
c4.metric("Top wasted dish", fdf.groupby("dish_name")["wasted_qty"].sum().idxmax() if not fdf.empty else "—")

tab1, tab2 = st.tabs(["Dashboard", "Ask the analyst"])

with tab1:
       # ---------- Interactive Waste Forecast ----------
    st.subheader("🔮 Waste Forecast")
    # Use the day after the latest available historical date
    latest_date = ml_df["date"].max()
    default_forecast_date = latest_date + pd.Timedelta(days=1)

    forecast_date = st.date_input(
        "Forecast date",
        value=default_forecast_date.date(),
        min_value=default_forecast_date.date()
    )

    forecast_date = pd.Timestamp(forecast_date)

    # Automatically determine weekend from forecast date
    is_weekend = 1 if forecast_date.dayofweek >= 5 else 0

    col1, col2 = st.columns(2)

    with col1:
        st.write(
            "Weekend:",
            "Yes" if is_weekend else "No"
        )

    with col2:
        month = forecast_date.month
        st.write("Month:", month)

    col3, col4 = st.columns(2)

    with col3:
        is_festival = st.selectbox(
            "Is it a festival?",
            ["No", "Yes"]
        )

    with col4:
        has_promotion = st.selectbox(
            "Is there a promotion?",
            ["No", "Yes"]
        
        )
        st.write("### Production and Sales Inputs")



    # ---------- Automatically calculate historical features ----------

    daily_waste = (
        ml_df.groupby("date")["wasted_qty"]
        .sum()
        .sort_index()
    )

    previous_date = forecast_date - pd.Timedelta(days=1)
    previous_week_date = forecast_date - pd.Timedelta(days=7)

    # Previous day's total waste
    if previous_date in daily_waste.index:
        previous_waste = daily_waste.loc[previous_date]
    else:
        previous_waste = daily_waste.iloc[-1]

    # Waste from the previous week
    if previous_week_date in daily_waste.index:
        previous_week_waste = daily_waste.loc[previous_week_date]
    else:
        previous_week_waste = daily_waste.iloc[-1]

    # Previous 7-day average waste
    historical_7_days = daily_waste[
        (daily_waste.index < forecast_date)
        & (daily_waste.index >= forecast_date - pd.Timedelta(days=7))
    ]

    if not historical_7_days.empty:
        rolling_7_day_waste = historical_7_days.mean()
    else:
        rolling_7_day_waste = daily_waste.iloc[-1]

    # ---------- Show automatically calculated values ----------

    st.write("### Historical features used by the model")

    f1, f2, f3 = st.columns(3)

    f1.metric(
        "Previous day waste",
        f"{previous_waste:.2f} units"
    )

    f2.metric(
        "Previous week waste",
        f"{previous_week_waste:.2f} units"
    )

    f3.metric(
        "7-day average waste",
        f"{rolling_7_day_waste:.2f} units"
    )

    # ---------- Prediction ----------

    # ---------- Prediction ----------

if st.button("Predict Waste"):

    prediction_features = pd.DataFrame([{
        "is_weekend": is_weekend,
        "is_festival": 1 if is_festival == "Yes" else 0,
        "has_promotion": 1 if has_promotion == "Yes" else 0,
        "previous_waste": previous_waste,
        "previous_week_waste": previous_week_waste,
        "rolling_7_day_waste": rolling_7_day_waste,
        "month": month
    }])

    predicted_waste = model.predict(
        prediction_features
    )[0]

    st.session_state.predicted_waste = float(predicted_waste)
    st.session_state.forecast_date = forecast_date


# ---------- Display Prediction Result ----------

if st.session_state.predicted_waste is not None:

    st.markdown("### 📊 Predicted Food Waste")

    st.success(
        f"Predicted Waste for "
        f"{st.session_state.forecast_date.strftime('%d %B %Y')}: "
        f"**{st.session_state.predicted_waste:.2f} units**"
    )

    st.divider()
    left, right = st.columns(2)

    with left:
        trend = fdf.groupby("date", as_index=False)["wasted_qty"].sum()
        fig = px.line(trend, x="date", y="wasted_qty", title="Waste over time")
        st.plotly_chart(fig, use_container_width=True)

        by_weekday = fdf.groupby("day_of_week", as_index=False)["wasted_qty"].mean()
        order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        by_weekday["day_of_week"] = pd.Categorical(by_weekday["day_of_week"], categories=order, ordered=True)
        by_weekday = by_weekday.sort_values("day_of_week")
        fig2 = px.bar(by_weekday, x="day_of_week", y="wasted_qty", title="Avg waste by day of week")
        st.plotly_chart(fig2, use_container_width=True)

    with right:
        by_dish = fdf.groupby("dish_name", as_index=False)["wasted_qty"].sum().sort_values("wasted_qty", ascending=False)
        fig3 = px.bar(by_dish, x="wasted_qty", y="dish_name", orientation="h", title="Total waste by dish")
        st.plotly_chart(fig3, use_container_width=True)

        by_weather = fdf.groupby("weather", as_index=False)["wasted_qty"].mean()
        fig4 = px.bar(by_weather, x="weather", y="wasted_qty", title="Avg waste by weather")
        st.plotly_chart(fig4, use_container_width=True)

with tab2:
    st.subheader("🤖 AI Food Waste Analyst")

    st.write(
        "Ask questions about your restaurant's food waste, "
        "predictions, and recommendations."
    )

    summary = build_structured_summary(fdf)

    # Keep ML prediction available for GenAI
    if st.session_state.predicted_waste is not None:
        summary["predicted_waste"] = round(
            st.session_state.predicted_waste, 2
        )

    if st.session_state.forecast_date is not None:
        summary["forecast_date"] = str(
            st.session_state.forecast_date.date()
        )

    with st.expander("View data sent to AI"):
        st.json(summary)

    question = st.text_input(
        "Ask your question",
        placeholder="Example: What is causing the most food waste?"
    )

    if st.button("🤖 Ask the AI", type="primary"):
        if question.strip():
            with st.spinner("Analyzing your food waste data..."):
                answer = call_llm(question, summary)

            st.markdown("### AI Recommendation")
            st.write(answer)
        else:
            st.warning("Please enter a question first.")