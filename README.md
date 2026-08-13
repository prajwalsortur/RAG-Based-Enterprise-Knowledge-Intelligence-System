# 🍽️ Food Waste Analytics & AI-Powered Forecasting System

An end-to-end **Data Science, Machine Learning, and Generative AI application** designed to help restaurants analyze food waste, forecast future waste levels, and generate intelligent data-driven insights.

The system combines **Exploratory Data Analysis, Machine Learning forecasting, structured analytics, and Gemini-powered Generative AI** into an interactive Streamlit application.

---

## 🚀 Project Overview

Food waste is a major operational and financial challenge for restaurants. Large amounts of food can be wasted due to inaccurate demand estimation, over-preparation, inventory issues, and changing customer behavior.

This project provides an AI-powered solution that transforms restaurant waste data into actionable insights.

The application allows users to:

- 📊 Analyze historical food waste data
- 📈 Forecast future food waste using Machine Learning
- 🔍 Identify waste patterns and trends
- 📋 Generate structured analytical summaries
- 🤖 Ask questions about the data using Generative AI
- 💡 Receive AI-powered recommendations and insights
- 🎯 Support better inventory and food preparation decisions

---

## 🎯 Key Objectives

- Analyze restaurant food waste patterns
- Understand major factors contributing to waste
- Build a Machine Learning model for waste forecasting
- Convert analytical results into structured summaries
- Integrate Generative AI for natural-language data analysis
- Provide an interactive dashboard for users
- Demonstrate an end-to-end Data Science + AI/ML workflow

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────────┐
                    │     Restaurant Data     │
                    │      CSV / Dataset      │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     Data Processing     │
                    │     Pandas / NumPy      │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │    EDA & Analytics      │
                    │ Pandas / Plotly / Charts │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴────────────────┐
                 ▼                                ▼
      ┌─────────────────────┐          ┌─────────────────────┐
      │ Machine Learning    │          │ Structured Summary  │
      │ Waste Forecasting   │          │ JSON / Analytics    │
      │ Scikit-learn        │          │ Python              │
      └──────────┬──────────┘          └──────────┬──────────┘
                 │                                │
                 └──────────────┬─────────────────┘
                                ▼
                    ┌─────────────────────────┐
                    │     GenAI Layer        │
                    │    Gemini API / LLM    │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   Streamlit Application │
                    │ Dashboard + AI Assistant │
                    └─────────────────────────┘
