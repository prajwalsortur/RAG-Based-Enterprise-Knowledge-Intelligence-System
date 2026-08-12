# Food Waste Analytics for Restaurants

**A GenAI-powered data science system** that helps restaurants understand, predict, and reduce food waste — and explains those findings in plain language through a Generative AI layer, instead of a static dashboard.

Traditional ML/analytics does the calculation. GenAI does the communication. The system is **not** replacing the data science pipeline with AI — it puts an intelligent, conversational front-end on top of a real analytics engine.

The system does three things:
- **Understands the past** — analyzes historical prep, sales, and waste data to find patterns
- **Predicts the future** — forecasts expected waste and recommends prep quantities *(planned)*
- **Explains itself in natural language** — a GenAI layer turns numbers into a conversational report a manager can query directly, e.g. *"Why did we waste so much paneer this week?"* *(in progress)*

## Build Progress

| Phase | Description | Status |
|---|---|---|
| 1 | Define the problem | 🟢 Done |
| 2 | Data collection / simulation | 🟢 Done (`generate_data.py`) |
| 3 | Data cleaning & EDA | 🟢 Done (`app.py` dashboard) |
| 4 | Feature engineering | 🔴 Not started |
| 5 | Predictive modeling | 🔴 Not started |
| 6 | GenAI layer (structured summary + prompt) | 🟡 Structured summary done; LLM call stubbed |
| 7 | Connect model output → GenAI | 🔴 Not started (no model yet to connect) |
| 8 | Interface (chat / auto-reports) | 🟡 Chat UI shell built; not yet grounded in real LLM |
| 9 | Evaluation & business impact | 🔴 Not started |
| 10 | Packaging & presentation | 🟡 In progress (this README) |

## Critical Design Rule

The LLM **never** sees raw, unaggregated data and is **never** asked to do arithmetic. All numeric computation happens in Python; the LLM only receives pre-computed, structured summaries and reasons/writes in natural language around them. This is the single biggest safeguard against hallucinated numbers in GenAI analytics projects — and it's already reflected in `build_structured_summary()` in `app.py`.

## System Architecture

```
Raw data (prep/sold/waste, dish, date, weather, events, cost)
        │
        ▼
Cleaning & preprocessing (missing values, category encoding)
        │
        ▼
Exploratory Data Analysis (trends by dish / day / weather / cost)         ✅ Done
        │
        ▼
Feature engineering (lag features, rolling averages, day-type flags)      ⏳ Planned
        │
        ▼
Predictive model — waste forecast per dish per day (RF / XGBoost)         ⏳ Planned
        │
        ▼
Structured summary layer (Python → clean JSON/text, NOT raw rows)         ✅ Done
        │
        ▼
GenAI layer (LLM reasons over the structured summary only)                🟡 Stubbed
        │
        ▼
Interface — chat UI and/or auto-generated weekly report                   🟡 Chat shell built
```

## Features (Implemented)

- 📊 Interactive Streamlit dashboard with date, dish, and weather filters
- 📈 KPIs — total waste units, total waste cost, avg waste/day, top wasted dish
- 📉 Trend charts — waste over time, avg waste by weekday, waste by dish, waste by weather
- 🧪 Synthetic data generator (`generate_data.py`) with realistic built-in relationships: weekend footfall effects, rainy-day over-prep, promotion/event demand spikes, festival waste spikes, dish-level perishability
- 🧠 Structured summary builder (`build_structured_summary()`) — the grounding layer for the GenAI system
- 💬 "Ask the analyst" chat tab — UI and summary pipeline done; LLM call is a canned placeholder pending API integration

## Roadmap (Remaining Phases)

### Phase 4 — Feature Engineering
- Lag features (yesterday's waste, last week's average waste per dish)
- Rolling averages (7-day rolling mean of sales/waste)
- Categorical encoding for dish, weather, day type
- Weekend / holiday / promotion flags

### Phase 5 — Predictive Modeling
- Baseline: Linear Regression
- Upgrade: Random Forest or XGBoost for non-linear patterns
- Evaluate with MAE/RMSE, broken down per dish
- Optional classification model: "high waste risk day" (yes/no)

### Phase 6 — GenAI Layer
- Pick LLM provider (OpenAI / Anthropic Claude / Gemini) and wire it into `call_llm()`
- Write the system prompt: role ("restaurant operations analyst"), available data, and a hard constraint to only use provided numbers
- Test against a fixed set of manager questions to confirm grounded, non-hallucinated answers

### Phase 7 — Connect Model Output to GenAI
- Single pipeline: `new_data → model prediction → structured summary → LLM call → natural-language output`
- Optional: function/tool-calling so the LLM can call Python functions on demand (e.g. `get_waste_by_dish(dish_name)`)
- Log every LLM call with its grounding data for debugging and rigor

### Phase 8 — Interface
- Finish the chat interface (already scaffolded in `app.py`)
- Add an auto-generated "Weekly Waste Report" as a showcase artifact

### Phase 9 — Evaluation & Business Impact
- Report MAE/RMSE with real-world context (e.g. "average error of 1.2 kg per dish per day")
- Translate waste reduction into ₹/$ saved per month
- Track GenAI answer accuracy against the test question set like a mini QA suite

### Phase 10 — Packaging & Presentation
- Architecture diagram, results, and a one-paragraph business case
- 2–3 minute demo video/GIF of the chat interface
- Deploy (Streamlit Community Cloud, Render, or Hugging Face Spaces)

## Stretch Goals

- RAG over unstructured data (chef notes, supplier remarks) so the LLM can cite qualitative reasons, not just numeric patterns
- Prep-quantity recommendation engine with confidence ranges
- Multi-restaurant support with cross-location benchmarking
- Sustainability metric (CO2-equivalent of food waste) for an ESG angle
- Few-shot prompt tuning for consistent tone and recommendation style

## Tech Stack

| Layer | Tool |
|---|---|
| Language | Python 3.10+ |
| Data manipulation | Pandas, NumPy |
| Modeling *(planned)* | scikit-learn, XGBoost |
| LLM API *(planned)* | OpenAI / Anthropic Claude / Gemini |
| LLM orchestration *(optional)* | LangChain / LlamaIndex |
| App / interface | Streamlit |
| Visualization | Plotly |
| Storage | CSV (current) → SQLite/PostgreSQL if scaling up |
| Deployment *(planned)* | Streamlit Community Cloud, Render, or Hugging Face Spaces |

## Getting Started

### Prerequisites
- Python 3.10+

### Installation

```bash
git clone https://github.com/your-username/food-waste-analytics-restaurants.git
cd food-waste-analytics-restaurants

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### Generate Synthetic Data

```bash
python generate_data.py --months 9 --start-date 2025-01-01 --out data/waste_data.csv
```

### Run the Dashboard

```bash
streamlit run app.py
```

Available at `http://localhost:8501`.

## Project Structure

```
food-waste-analytics-restaurants/
├── app.py                   # Streamlit dashboard (EDA + Ask the analyst tab)
├── generate_data.py          # Synthetic data generator
├── data/
│   └── waste_data.csv
├── requirements.txt
└── README.md

# Planned additions:
├── src/
│   ├── features/              # Phase 4: feature engineering
│   ├── models/                 # Phase 5: training & inference
│   ├── genai/                   # Phase 6-7: LLM prompt & pipeline logic
│   └── rag/                     # Stretch goal: retrieval over unstructured notes
├── reports/                    # Phase 8: auto-generated weekly reports
├── tests/                       # Phase 9: QA suite for model + GenAI accuracy
├── notebooks/                   # Experimentation
└── Dockerfile
```

## Data Schema

| Column | Description |
|---|---|
| `date` | Calendar date |
| `day_of_week` | Day name (Monday–Sunday) |
| `is_weekend` | Boolean weekend flag |
| `weather` | clear / cloudy / rainy / hot |
| `is_festival` | Boolean festival/holiday flag |
| `has_promotion` | Boolean promo flag |
| `dish_name` | Dish name |
| `category` | main / starter / bread / dessert |
| `prepared_qty` | Quantity prepared by kitchen |
| `sold_qty` | Quantity actually sold |
| `wasted_qty` | `prepared_qty - sold_qty` |
| `cost_per_unit` | Cost per unit (₹) |
| `waste_cost` | `wasted_qty * cost_per_unit` |

## Common Pitfalls (Being Actively Avoided)

- ❌ Feeding raw data to the LLM → ✅ structured summary layer already in place
- ❌ Over-scoping the GenAI part → aiming for 5–6 solid, well-answered question types before expanding
- ❌ Unrealistic simulated data → `generate_data.py` deliberately encodes weather/weekend/festival effects
- ❌ No baseline model → Linear Regression baseline planned before XGBoost
- ❌ Skipping business translation → Phase 9 converts model error into ₹/$ impact, not just RMSE

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
