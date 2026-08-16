# 🍽️ Food Waste Analytics for Restaurants
### Data Analytics + Machine Learning + LLM/Generative AI + Streamlit

> An end-to-end AI-powered restaurant analytics system that combines **Data Analytics, Machine Learning forecasting, and Large Language Model (LLM) capabilities** to analyze food waste, predict future waste, and generate actionable business insights through an interactive Streamlit application.

---

## 🚀 Project Overview

Food waste is a major operational and financial challenge for restaurants. Over-preparation, changing demand, promotions, festivals, weekends, weather conditions, and historical consumption patterns can contribute to unnecessary food waste.

This project provides an end-to-end solution that transforms restaurant waste data into:

- 📊 Interactive analytics
- 📈 Machine Learning predictions
- 🤖 LLM-powered insights
- 💡 Business recommendations
- 🎯 Decision-support information

The application combines **Data Analytics + Machine Learning + LLM/Generative AI + Streamlit** into a single workflow.

---

## 🎯 What This Project Does

The system performs four major functions:

### 1. 📊 Data Analytics

Analyzes historical restaurant food-waste data to identify:

- Total waste
- Waste cost
- Average daily waste
- Most wasted dishes
- Weekday vs weekend patterns
- Weather-related patterns
- Promotional effects
- Festival-related effects
- Historical waste trends

Interactive filters allow users to explore the data dynamically.

---

### 2. 🤖 Machine Learning Forecasting

A Machine Learning pipeline predicts future food waste using historical and operational features.

The project evaluates:

- Baseline model
- Random Forest Regressor
- XGBoost Regressor

Models are evaluated using:

- MAE — Mean Absolute Error
- RMSE — Root Mean Squared Error

The best-performing model based on MAE is selected and saved for application use.

---

### 3. 🧠 LLM / Generative AI Layer

The project integrates **Google Gemini as the Large Language Model (LLM)**.

The LLM is used to convert analytical results and Machine Learning outputs into understandable business insights.

The AI assistant can help answer questions such as:

```text
Which dish generates the most waste?

How does weekend waste compare with weekday waste?

What are the major food-waste patterns?

What does the forecast indicate?

What actions can reduce food waste?

Which areas should the restaurant focus on?
