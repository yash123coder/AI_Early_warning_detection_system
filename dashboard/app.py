# # import sys
# # import os

# # # -------------------------------------------------
# # # Add project root to sys.path FIRST
# # # -------------------------------------------------
# # PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# # if PROJECT_ROOT not in sys.path:
# #     sys.path.insert(0, PROJECT_ROOT)


# # import sys
# # import os
# # import streamlit as st
# # import pandas as pd
# # import altair as alt
# # from datetime import datetime
# # from alerts.helpers import save_risk_history, load_risk_history


# # # -------------------------------------------------
# # # Add project root to sys.path
# # # -------------------------------------------------
# # PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# # if PROJECT_ROOT not in sys.path:
# #     sys.path.append(PROJECT_ROOT)



# # # -------------------------------------------------
# # # Imports from project
# # # -------------------------------------------------
# # from risk_engine.risk_scoring import calculate_risk
# # from nlp.text_risk_extractor import analyze_text
# # from alerts.helpers import load_risk_history

# # # -------------------------------------------------
# # # Page Config
# # # -------------------------------------------------
# # st.set_page_config(page_title="AI Business Intelligence Assistant", layout="wide")
# # st.title("🚀 AI Business Intelligence & Risk Assistant")
# # st.caption("AI-powered business risk & growth analysis")
# # st.divider()

# # # -------------------------------------------------
# # # Session State
# # # -------------------------------------------------
# # if "analyzed" not in st.session_state:
# #     st.session_state.analyzed = False

# # # -------------------------------------------------
# # # Business Type Benchmarks
# # # -------------------------------------------------
# # business_types = {
# #     "Clothing": {"repeat_customer": 35},
# #     "Shoes": {"repeat_customer": 30},
# #     "Healthcare": {"repeat_customer": 50},
# #     "IT Services": {"repeat_customer": 40},
# #     "Other": {"repeat_customer": 40}
# # }

# # business_type = st.selectbox("🏢 Business Type", list(business_types.keys()))
# # benchmark_repeat = business_types[business_type]["repeat_customer"]

# # st.divider()

# # # -------------------------------------------------
# # # KPI Inputs (MATCH ML MODEL FEATURES)
# # # -------------------------------------------------
# # st.subheader("📊 Business KPIs")

# # col1, col2 = st.columns(2)

# # with col1:
# #     monthly_sales = st.number_input("Monthly Sales", min_value=0, value=120)
# #     revenue = st.number_input("Revenue", min_value=0, value=40000)
# #     customer_count = st.number_input("Customer Count", min_value=0, value=300)
# #     repeat_customer_pct = st.slider("Repeat Customer %", 0, 100, benchmark_repeat)

# # with col2:
# #     churn_rate = st.slider("Churn Rate", 0.0, 1.0, 0.42)
# #     support_tickets = st.number_input("Support Tickets", min_value=0, value=80)
# #     marketing_spend = st.number_input("Marketing Spend", min_value=0, value=5000)
# #     avg_product_cost = st.number_input("Average Product Cost", min_value=0, value=500)

# # feedback_text = st.text_area(
# #     "📝 Customer / Employee Feedback",
# #     value="Service quality is poor and support is very slow"
# # )

# # st.divider()

# # # -------------------------------------------------
# # # Analyze Button
# # # -------------------------------------------------
# # if st.button("🔍 Analyze Business"):
# #     st.session_state.analyzed = True

# # # -------------------------------------------------
# # # ANALYSIS SECTION
# # # -------------------------------------------------
# # if st.session_state.analyzed:

# #     # ---------------- ML INPUT ----------------
# #     business_data = {
# #         "monthly_sales": monthly_sales,
# #         "revenue": revenue,
# #         "customer_count": customer_count,
# #         "churn_rate": churn_rate,
# #         "support_tickets": support_tickets,
# #         "marketing_spend": marketing_spend
# #     }

# #     with st.spinner("Running AI analysis..."):
# #         text_result = analyze_text(feedback_text)
# #         result = calculate_risk(business_data, text_result)
# #         save_risk_history(result["risk_score"])

# #     # ---------------- METRICS ----------------
# #     total_cost = marketing_spend + (avg_product_cost * customer_count)
# #     profit = revenue - total_cost

# #     profit_margin = round((profit / revenue) * 100, 2) if revenue else 0
# #     expense_ratio = round((total_cost / revenue) * 100, 2) if revenue else 0

# #     # -------------------------------------------------
# #     # Business Summary
# #     # -------------------------------------------------
# #     st.subheader("📈 Business Summary")

# #     c1, c2, c3 = st.columns(3)

# #     with c1:
# #         st.metric("AI Risk Score", result["risk_score"])
# #         st.metric("Risk Level", result["risk_level"])

# #     with c2:
# #         st.metric("Profit Margin (%)", profit_margin)
# #         st.metric("Expense Ratio (%)", expense_ratio)

# #     with c3:
# #         st.metric("Repeat Customer %", repeat_customer_pct)
# #         st.metric("Customer Churn (%)", round(churn_rate * 100, 2))

# #     # -------------------------------------------------
# #     # SHAP Explainability
# #     # -------------------------------------------------
# #     st.subheader("🔍 Why AI Predicted This Risk")

# #     shap_df = pd.DataFrame({
# #         "Feature": list(result["shap_values"].keys()),
# #         "Impact": list(result["shap_values"].values())
# #     }).sort_values("Impact", key=abs, ascending=False)

# #     shap_chart = alt.Chart(shap_df).mark_bar().encode(
# #         x="Impact",
# #         y=alt.Y("Feature", sort="-x"),
# #         color=alt.condition(
# #             alt.datum.Impact > 0,
# #             alt.value("red"),
# #             alt.value("green")
# #         ),
# #         tooltip=["Feature", "Impact"]
# #     ).properties(height=350)

# #     st.altair_chart(shap_chart, use_container_width=True)

# #     # -------------------------------------------------
# #     # Suggestions
# #     # -------------------------------------------------
# #     st.subheader("💡 Actionable Suggestions")

# #     if result["risk_level"] == "HIGH":
# #         st.error("🚨 High Business Risk")
# #         st.write("- Reduce churn urgently")
# #         st.write("- Improve support response time")
# #         st.write("- Optimize marketing spend")
# #     elif result["risk_level"] == "MEDIUM":
# #         st.warning("⚠ Medium Risk")
# #         st.write("- Improve retention strategy")
# #         st.write("- Track expenses carefully")
# #     else:
# #         st.success("✅ Low Risk – Business is healthy")

# #     # -------------------------------------------------
# #     # NLP Insights
# #     # -------------------------------------------------
# #     st.subheader("🧠 Customer Feedback Intelligence")

# #     c1, c2 = st.columns(2)

# #     with c1:
# #         st.metric("Sentiment", text_result["sentiment"])
# #         st.metric("Confidence", text_result["confidence"])

# #     with c2:
# #         st.write("🔍 Key Issues")
# #         for topic in text_result["topics"]:
# #             st.write(f"- {topic}")

# #     # -------------------------------------------------
# #     # Revenue Trend Chart
# #     # -------------------------------------------------
# #     st.subheader("📊 Revenue Trend (Last 6 Months)")

# #     df_revenue = pd.DataFrame({
# #         "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
# #         "Revenue": [
# #             revenue * 0.7, revenue * 0.8, revenue * 0.85,
# #             revenue * 0.9, revenue, revenue * 1.05
# #         ]
# #     })

# #     st.altair_chart(
# #         alt.Chart(df_revenue).mark_line(point=True).encode(
# #             x="Month",
# #             y="Revenue",
# #             tooltip=["Month", "Revenue"]
# #         ).properties(height=350),
# #         use_container_width=True
# #     )

# #     # -------------------------------------------------
# #     # Profit vs Expense Chart
# #     # -------------------------------------------------
# #     st.subheader("💰 Profit vs Expense Breakdown")

# #     df_profit = pd.DataFrame({
# #         "Category": ["Revenue", "Total Expenses", "Profit"],
# #         "Amount": [revenue, total_cost, profit]
# #     })

# #     st.altair_chart(
# #         alt.Chart(df_profit).mark_bar().encode(
# #             x="Category",
# #             y="Amount",
# #             tooltip=["Category", "Amount"]
# #         ).properties(height=350),
# #         use_container_width=True
# #     )

# #     # -------------------------------------------------
# #     # Risk Trend Over Time
# #     # -------------------------------------------------
# #     st.subheader("📈 Risk Trend Over Time")

# #     history_df = load_risk_history()

# #     if len(history_df) >= 2:
# #         st.altair_chart(
# #             alt.Chart(history_df).mark_line(point=True).encode(
# #                 x="timestamp:T",
# #                 y="risk_score:Q",
# #                 tooltip=["timestamp", "risk_score"]
# #             ).properties(height=350),
# #             use_container_width=True
# #         )
# #     else:
# #         st.info("Not enough historical data yet")

# #     # -------------------------------------------------
# #     # Early Warning Detection
# #     # -------------------------------------------------
# #     if len(history_df) >= 3:
# #         recent = history_df.tail(3)["risk_score"].values

# #         if recent[2] > recent[1] > recent[0]:
# #             st.error("🚨 EARLY WARNING: Risk increasing continuously")
# #         elif recent[2] < recent[1] < recent[0]:
# #             st.success("✅ Risk decreasing — good trend")
# #         else:
# #             st.warning("⚠ Risk fluctuating — monitor closely")
# import sys
# import os
# import streamlit as st
# import pandas as pd
# import altair as alt
# from datetime import datetime

# # -------------------------------------------------
# # Add project root FIRST (FIXES alerts import issue)
# # -------------------------------------------------
# PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# if PROJECT_ROOT not in sys.path:
#     sys.path.insert(0, PROJECT_ROOT)

# # -------------------------------------------------
# # Project Imports
# # -------------------------------------------------
# from risk_engine.risk_scoring import calculate_risk
# from nlp.text_risk_extractor import analyze_text
# from alerts.helpers import save_risk_history, load_risk_history

# # -------------------------------------------------
# # Page Config
# # -------------------------------------------------
# st.set_page_config(page_title="AI Business Intelligence Assistant", layout="wide")
# st.title("🚀 AI Business Intelligence & Risk Assistant")
# st.caption("AI-powered business risk & early warning system")
# st.divider()

# # -------------------------------------------------
# # Session State
# # -------------------------------------------------
# if "analyzed" not in st.session_state:
#     st.session_state.analyzed = False

# # -------------------------------------------------
# # Business Type Benchmarks
# # -------------------------------------------------
# business_types = {
#     "Clothing": {"repeat_customer": 35},
#     "Shoes": {"repeat_customer": 30},
#     "Healthcare": {"repeat_customer": 50},
#     "IT Services": {"repeat_customer": 40},
#     "Other": {"repeat_customer": 40}
# }

# business_type = st.selectbox("🏢 Business Type", list(business_types.keys()))
# benchmark_repeat = business_types[business_type]["repeat_customer"]

# st.divider()

# # -------------------------------------------------
# # KPI Inputs
# # -------------------------------------------------
# st.subheader("📊 Business KPIs")

# col1, col2 = st.columns(2)

# with col1:
#     monthly_sales = st.number_input("Monthly Sales", min_value=0, value=120)
#     revenue = st.number_input("Revenue", min_value=0, value=40000)
#     customer_count = st.number_input("Customer Count", min_value=0, value=300)
#     repeat_customer_pct = st.slider("Repeat Customer %", 0, 100, benchmark_repeat)

# with col2:
#     churn_rate = st.slider("Churn Rate", 0.0, 1.0, 0.42)
#     support_tickets = st.number_input("Support Tickets", min_value=0, value=80)
#     marketing_spend = st.number_input("Marketing Spend", min_value=0, value=5000)
#     avg_product_cost = st.number_input("Average Product Cost", min_value=0, value=500)

# feedback_text = st.text_area(
#     "📝 Customer / Employee Feedback",
#     value="Service quality is poor and support is very slow"
# )

# st.divider()

# # -------------------------------------------------
# # Analyze Button
# # -------------------------------------------------
# if st.button("🔍 Analyze Business"):
#     st.session_state.analyzed = True

# # -------------------------------------------------
# # Analysis Section
# # -------------------------------------------------
# if st.session_state.analyzed:

#     business_data = {
#         "monthly_sales": monthly_sales,
#         "revenue": revenue,
#         "customer_count": customer_count,
#         "churn_rate": churn_rate,
#         "support_tickets": support_tickets,
#         "marketing_spend": marketing_spend
#     }

#     with st.spinner("Running AI analysis..."):
#         text_result = analyze_text(feedback_text)
#         result = calculate_risk(business_data, text_result)
#         save_risk_history(result["risk_score"])

#     # -------------------------------------------------
#     # Metrics
#     # -------------------------------------------------
#     total_cost = marketing_spend + (avg_product_cost * customer_count)
#     profit = revenue - total_cost

#     profit_margin = round((profit / revenue) * 100, 2) if revenue else 0
#     expense_ratio = round((total_cost / revenue) * 100, 2) if revenue else 0

#     st.subheader("📈 Business Summary")

#     c1, c2, c3 = st.columns(3)

#     with c1:
#         st.metric("AI Risk Score", result["risk_score"])
#         st.metric("Risk Level", result["risk_level"])

#     with c2:
#         st.metric("Profit Margin (%)", profit_margin)
#         st.metric("Expense Ratio (%)", expense_ratio)

#     with c3:
#         st.metric("Repeat Customer %", repeat_customer_pct)
#         st.metric("Customer Churn (%)", round(churn_rate * 100, 2))

#     # -------------------------------------------------
#     # Explainability (FIXED)
#     # -------------------------------------------------
#     st.subheader("🔍 Why AI Predicted This Risk")

#     shap_df = pd.DataFrame({
#         "Feature": result["shap_values"].keys(),
#         "Impact": result["shap_values"].values()
#     }).sort_values("Impact", key=abs, ascending=False)

#     shap_chart = alt.Chart(shap_df).mark_bar().encode(
#         x=alt.X("Impact", scale=alt.Scale(domain=[-50, 50])),
#         y=alt.Y("Feature", sort="-x"),
#         color=alt.condition(
#             alt.datum.Impact > 0,
#             alt.value("#ff4b4b"),
#             alt.value("#2ecc71")
#         ),
#         tooltip=["Feature", "Impact"]
#     ).properties(height=350)

#     st.altair_chart(shap_chart, use_container_width=True)

#     # -------------------------------------------------
#     # Suggestions
#     # -------------------------------------------------
#     st.subheader("💡 Actionable Suggestions")

#     if result["risk_level"] == "HIGH":
#         st.error("🚨 High Business Risk")
#         st.write("- Reduce churn urgently")
#         st.write("- Improve support response time")
#         st.write("- Optimize marketing spend")
#     elif result["risk_level"] == "MEDIUM":
#         st.warning("⚠ Medium Risk")
#         st.write("- Improve retention strategy")
#         st.write("- Track expenses carefully")
#     else:
#         st.success("✅ Low Risk – Business is healthy")

#     # -------------------------------------------------
#     # Risk Trend
#     # -------------------------------------------------
#     st.subheader("📈 Risk Trend Over Time")

#     history_df = load_risk_history()

#     if len(history_df) >= 2:
#         st.altair_chart(
#             alt.Chart(history_df).mark_line(point=True).encode(
#                 x="timestamp:T",
#                 y="risk_score:Q",
#                 tooltip=["timestamp", "risk_score"]
#             ).properties(height=350),
#             use_container_width=True
#         )
#     else:
#         st.info("Not enough historical data yet")

#     # -------------------------------------------------
#     # Early Warning
#     # -------------------------------------------------
#     if len(history_df) >= 3:
#         recent = history_df.tail(3)["risk_score"].values

#         if recent[2] > recent[1] > recent[0]:
#             st.error("🚨 EARLY WARNING: Risk increasing continuously")
#         elif recent[2] < recent[1] < recent[0]:
#             st.success("✅ Risk decreasing — good trend")
#         else:
#             st.warning("⚠ Risk fluctuating — monitor closely")
# import sys
# import os
# import streamlit as st
# import pandas as pd
# import altair as alt

# # -------------------------------------------------
# # Project Root
# # -------------------------------------------------
# PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# if PROJECT_ROOT not in sys.path:
#     sys.path.insert(0, PROJECT_ROOT)

# # -------------------------------------------------
# # Imports
# # -------------------------------------------------
# from risk_engine.risk_scoring import calculate_risk
# from nlp.text_risk_extractor import analyze_text
# from alerts.helpers import save_risk_history, load_risk_history

# # -------------------------------------------------
# # Page Config
# # -------------------------------------------------
# st.set_page_config(page_title="AI Business Intelligence Assistant", layout="wide")
# st.title("🚀 AI Business Intelligence & Risk Assistant")
# st.caption("AI-powered business risk & growth analysis")
# st.divider()

# # -------------------------------------------------
# # Session State
# # -------------------------------------------------
# if "analyzed" not in st.session_state:
#     st.session_state.analyzed = False

# # -------------------------------------------------
# # KPI Inputs
# # -------------------------------------------------
# st.subheader("📊 Business KPIs")

# col1, col2 = st.columns(2)

# with col1:
#     monthly_sales = st.number_input("Monthly Sales", value=120)
#     revenue = st.number_input("Revenue", value=40000)
#     customer_count = st.number_input("Customer Count", value=300)

# with col2:
#     churn_rate = st.slider("Churn Rate", 0.0, 1.0, 0.42)
#     support_tickets = st.number_input("Support Tickets", value=80)
#     marketing_spend = st.number_input("Marketing Spend", value=5000)

# avg_product_cost = st.number_input("Average Product Cost", value=500)

# feedback_text = st.text_area(
#     "📝 Customer / Employee Feedback",
#     "Service quality is poor and support is very slow"
# )

# # -------------------------------------------------
# # Analyze Button
# # -------------------------------------------------
# if st.button("🔍 Analyze Business"):
#     st.session_state.analyzed = True

# # =================================================
# # ANALYSIS
# # =================================================
# if st.session_state.analyzed:

#     business_data = {
#         "monthly_sales": monthly_sales,
#         "revenue": revenue,
#         "customer_count": customer_count,
#         "churn_rate": churn_rate,
#         "support_tickets": support_tickets,
#         "marketing_spend": marketing_spend
#     }

#     with st.spinner("Running AI analysis..."):
#         text_result = analyze_text(feedback_text)
#         result = calculate_risk(business_data, text_result)
#         save_risk_history(result["risk_score"])

#     # -------------------------------------------------
#     # SUMMARY
#     # -------------------------------------------------
#     st.divider()
#     st.subheader("📈 Business Summary")

#     total_cost = marketing_spend + (avg_product_cost * customer_count)
#     profit = revenue - total_cost

#     c1, c2, c3 = st.columns(3)
#     c1.metric("AI Risk Score", result["risk_score"])
#     c1.metric("Risk Level", result["risk_level"])
#     c2.metric("Profit", profit)
#     c3.metric("Churn %", round(churn_rate * 100, 2))

#     # -------------------------------------------------
#     # WHY AI PREDICTED THIS RISK
#     # -------------------------------------------------
#     st.divider()
#     st.subheader("🔍 Why AI Predicted This Risk")

#     shap_df = pd.DataFrame({
#         "Feature": result["shap_values"].keys(),
#         "Impact": result["shap_values"].values()
#     }).sort_values("Impact", key=abs, ascending=False)

#     st.altair_chart(
#         alt.Chart(shap_df).mark_bar().encode(
#             x="Impact",
#             y=alt.Y("Feature", sort="-x"),
#             color=alt.condition(
#                 alt.datum.Impact > 0,
#                 alt.value("#ff4b4b"),
#                 alt.value("#00c853")
#             ),
#             tooltip=["Feature", "Impact"]
#         ).properties(height=350),
#         use_container_width=True
#     )

#     # -------------------------------------------------
#     # ACTIONABLE SUGGESTIONS
#     # -------------------------------------------------
#     st.divider()
#     st.subheader("💡 Actionable Suggestions")

#     if result["risk_level"] == "HIGH":
#         st.error("🚨 High Business Risk")
#         st.markdown("- Reduce churn urgently")
#         st.markdown("- Improve support response time")
#         st.markdown("- Optimize marketing spend")

#     elif result["risk_level"] == "MEDIUM":
#         st.warning("⚠ Medium Risk")
#         st.markdown("- Improve customer retention")
#         st.markdown("- Monitor expenses")

#     else:
#         st.success("✅ Business is Healthy")

#     # -------------------------------------------------
#     # CUSTOMER FEEDBACK INTELLIGENCE
#     # -------------------------------------------------
#     st.divider()
#     st.subheader("🧠 Customer Feedback Intelligence")

#     c1, c2 = st.columns(2)
#     c1.metric("Sentiment", text_result["sentiment"])
#     c1.metric("Confidence", text_result["confidence"])

#     with c2:
#         st.write("🔍 Key Issues")
#         for t in text_result["topics"]:
#             st.write(f"- {t}")

#     # -------------------------------------------------
#     # REVENUE TREND
#     # -------------------------------------------------
#     st.divider()
#     st.subheader("📊 Revenue Trend (Last 6 Months)")

#     df_rev = pd.DataFrame({
#         "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
#         "Revenue": [
#             revenue * 0.7, revenue * 0.8, revenue * 0.85,
#             revenue * 0.9, revenue, revenue * 1.05
#         ]
#     })

#     st.altair_chart(
#         alt.Chart(df_rev).mark_line(point=True).encode(
#             x="Month",
#             y="Revenue"
#         ),
#         use_container_width=True
#     )

#     # -------------------------------------------------
#     # PROFIT VS EXPENSE
#     # -------------------------------------------------
#     st.divider()
#     st.subheader("💰 Profit vs Expense Breakdown")

#     df_pe = pd.DataFrame({
#         "Category": ["Revenue", "Total Expenses", "Profit"],
#         "Amount": [revenue, total_cost, profit]
#     })

#     st.altair_chart(
#         alt.Chart(df_pe).mark_bar().encode(
#             x="Category",
#             y="Amount"
#         ),
#         use_container_width=True
#     )

#     # -------------------------------------------------
#     # RISK TREND
#     # -------------------------------------------------
#     st.divider()
#     st.subheader("📈 Risk Trend Over Time")

#     history_df = load_risk_history()

#     if len(history_df) >= 2:
#         st.altair_chart(
#             alt.Chart(history_df).mark_line(point=True).encode(
#                 x="timestamp:T",
#                 y="risk_score:Q"
#             ),
#             use_container_width=True
#         )
#     else:
#         st.info("Not enough historical data yet")
# import sys
# import os
# import streamlit as st
# import pandas as pd
# import altair as alt
# from ai_agent.llama_advisor import ask_llama

# # -------------------------------------------------
# # Project Root
# # -------------------------------------------------
# PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# if PROJECT_ROOT not in sys.path:
#     sys.path.insert(0, PROJECT_ROOT)

# # -------------------------------------------------
# # Imports
# # -------------------------------------------------
# from risk_engine.risk_scoring import calculate_risk
# from nlp.text_risk_extractor import analyze_text
# from alerts.helpers import save_risk_history, load_risk_history

# # -------------------------------------------------
# # Page Config
# # -------------------------------------------------
# st.set_page_config(page_title="AI Business Intelligence Assistant", layout="wide")
# st.title("🚀 AI Business Intelligence & Risk Assistant")
# st.caption("AI-powered business risk & growth analysis (Developed By Yash Mandlik)")
# st.divider()

# # -------------------------------------------------
# # Session State
# # -------------------------------------------------

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# if "analyzed" not in st.session_state:
#     st.session_state.analyzed = False

# # -------------------------------------------------
# # KPI Inputs
# # -------------------------------------------------
# st.subheader("📊 Business KPIs")

# col1, col2 = st.columns(2)

# with col1:
#     monthly_sales = st.number_input("Monthly Sales", value=120)
#     revenue = st.number_input("Revenue", value=40000)
#     customer_count = st.number_input("Customer Count", value=300)

# with col2:
#     churn_rate = st.slider("Churn Rate", 0.0, 1.0, 0.42)
#     support_tickets = st.number_input("Support Tickets", value=80)
#     marketing_spend = st.number_input("Marketing Spend", value=5000)

# avg_product_cost = st.number_input("Average Product Cost", value=500)

# # ✅ NEW INPUT
# repeat_customers = st.number_input(
#     "Repeat Customer Count",
#     min_value=0,
#     max_value=customer_count,
#     value=120
# )

# feedback_text = st.text_area(
#     "📝 Customer / Employee Feedback",
#     "Service quality is poor and support is very slow"
# )

# # -------------------------------------------------
# # Analyze Button
# # -------------------------------------------------
# if st.button("🔍 Analyze Business"):
#     st.session_state.analyzed = True

# # =================================================
# # ANALYSIS
# # =================================================
# if st.session_state.analyzed:

#     business_data = {
#         "monthly_sales": monthly_sales,
#         "revenue": revenue,
#         "customer_count": customer_count,
#         "churn_rate": churn_rate,
#         "support_tickets": support_tickets,
#         "marketing_spend": marketing_spend
#     }

#     with st.spinner("Running AI analysis..."):
#         text_result = analyze_text(feedback_text)
#         result = calculate_risk(business_data, text_result)
#         save_risk_history(result["risk_score"])

#     # -------------------------------------------------
#     # SUMMARY
#     # -------------------------------------------------
#     st.divider()
#     st.subheader("📈 Business Summary")

#     total_cost = marketing_spend + (avg_product_cost * customer_count)
#     profit = revenue - total_cost

#     # ✅ NEW CALCULATIONS
#     repeat_customer_pct = (
#         (repeat_customers / customer_count) * 100
#         if customer_count > 0 else 0
#     )

#     profitable_status = "✅ Profitable" if profit > 0 else "❌ Not Profitable"

#     c1, c2, c3, c4, c5 = st.columns(5)
#     c1.metric("AI Risk Score", result["risk_score"])
#     c1.metric("Risk Level", result["risk_level"])
#     c2.metric("Profit", profit)
#     c3.metric("Churn %", round(churn_rate * 100, 2))
#     c4.metric("Repeat Customers %", f"{round(repeat_customer_pct, 2)}%")
#     c5.metric("Business Status","PROFITABLE" if profit > 0 else "LOSS",delta=profit)

#     st.info(f"📊 **Business Profitability Status:** {profitable_status}")

#     # -------------------------------------------------
#     # WHY AI PREDICTED THIS RISK
#     # -------------------------------------------------
#     st.divider()
#     st.subheader("🔍 Why AI Predicted This Risk")

#     shap_df = pd.DataFrame({
#         "Feature": result["shap_values"].keys(),
#         "Impact": result["shap_values"].values()
#     }).sort_values("Impact", key=abs, ascending=False)

#     st.altair_chart(
#         alt.Chart(shap_df).mark_bar().encode(
#             x="Impact",
#             y=alt.Y("Feature", sort="-x"),
#             color=alt.condition(
#                 alt.datum.Impact > 0,
#                 alt.value("#ff4b4b"),
#                 alt.value("#00c853")
#             ),
#             tooltip=["Feature", "Impact"]
#         ).properties(height=350),
#         use_container_width=True
#     )

#     # -------------------------------------------------
#     # ACTIONABLE SUGGESTIONS
#     # -------------------------------------------------
#     # -------------------------------------------------
#     # ACTIONABLE SUGGESTIONS (FIXED LOGIC)
#     # -------------------------------------------------
#     st.divider()
#     st.subheader("💡 Actionable Suggestions")

#     if profit < 0:
#         st.error("🚨 Business is Running in Loss")
#         st.markdown("- Reduce operational costs immediately")
#         st.markdown("- Re-evaluate pricing strategy")
#         st.markdown("- Improve repeat customer retention")
#         st.markdown("- Optimize marketing spend")

#     elif result["risk_level"] == "HIGH":
#         st.error("🚨 High Business Risk")
#         st.markdown("- Reduce churn urgently")
#         st.markdown("- Improve support response time")
#         st.markdown("- Optimize marketing spend")

#     elif result["risk_level"] == "MEDIUM":
#         st.warning("⚠ Medium Risk")
#         st.markdown("- Improve customer retention")
#         st.markdown("- Monitor expenses carefully")

#     else:
#         st.success("✅ Business is Healthy and Profitable")

#     # -------------------------------------------------
#     # AI BUSINESS ADVISOR (LLAMA CHAT)
#     # -------------------------------------------------
#     st.divider()
#     st.subheader("🤖 Ask AI for Business Growth Advice")

#     user_q = st.text_input(
#         "Ask anything to improve your business (sales, profit, retention, costs, etc.)"
#     )

#     if st.button("Ask AI"):
#         context = {
#             "risk_level": result["risk_level"],
#             "profit": profit,
#             "churn": churn_rate,
#             "repeat_pct": repeat_customer_pct,
#             "sentiment": text_result["sentiment"]
#         }

#         with st.spinner("AI is thinking..."):
#             ai_reply = ask_llama(user_q, context)

#         st.session_state.chat_history.append(("You", user_q))
#         st.session_state.chat_history.append(("AI", ai_reply))
#     # -------------------------------------------------
#     # CHAT HISTORY
#     # -------------------------------------------------
#     for role, msg in st.session_state.chat_history[-6:]:
#         if role == "You":
#             st.markdown(f"**🧑 You:** {msg}")
#         else:
#             st.markdown(f"**🤖 AI Advisor:** {msg}")

#     # -------------------------------------------------
#     # CUSTOMER FEEDBACK INTELLIGENCE
#     # -------------------------------------------------
#     st.divider()
#     st.subheader("🧠 Customer Feedback Intelligence")

#     c1, c2 = st.columns(2)
#     c1.metric("Sentiment", text_result["sentiment"])
#     c1.metric("Confidence", text_result["confidence"])

#     with c2:
#         st.write("🔍 Key Issues")
#         for t in text_result["topics"]:
#             st.write(f"- {t}")

#     # -------------------------------------------------
#     # REVENUE TREND
#     # -------------------------------------------------
#     st.divider()
#     st.subheader("📊 Revenue Trend (Last 6 Months)")

#     df_rev = pd.DataFrame({
#         "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
#         "Revenue": [
#             revenue * 0.7, revenue * 0.8, revenue * 0.85,
#             revenue * 0.9, revenue, revenue * 1.05
#         ]
#     })

#     st.altair_chart(
#         alt.Chart(df_rev).mark_line(point=True).encode(
#             x="Month",
#             y="Revenue"
#         ),
#         use_container_width=True
#     )

#     # -------------------------------------------------
#     # PROFIT VS EXPENSE
#     # -------------------------------------------------
#     st.divider()
#     st.subheader("💰 Profit vs Expense Breakdown")

#     df_pe = pd.DataFrame({
#         "Category": ["Revenue", "Total Expenses", "Profit"],
#         "Amount": [revenue, total_cost, profit]
#     })

#     st.altair_chart(
#         alt.Chart(df_pe).mark_bar().encode(
#             x="Category",
#             y="Amount"
#         ),
#         use_container_width=True
#     )

#     # -------------------------------------------------
#     # RISK TREND
#     # -------------------------------------------------
#     st.divider()
#     st.subheader("📈 Risk Trend Over Time")

#     history_df = load_risk_history()

#     if len(history_df) >= 2:
#         st.altair_chart(
#             alt.Chart(history_df).mark_line(point=True).encode(
#                 x="timestamp:T",
#                 y="risk_score:Q"
#             ),
#             use_container_width=True
#         )
#     else:
#         st.info("Not enough historical data yet")
import sys
import os
import streamlit as st
import pandas as pd
import altair as alt

# -------------------------------------------------
# Fix module path for Streamlit
# -------------------------------------------------
APP_DIR = os.path.dirname(os.path.abspath(__file__))
if APP_DIR not in sys.path:
    sys.path.insert(0, APP_DIR)

# Now imports will work correctly
from ai_agent.llama_advisor import ask_llama
from risk_engine.risk_scoring import calculate_risk
from nlp.text_risk_extractor import analyze_text
from alerts.helpers import save_risk_history, load_risk_history

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(page_title="AI Business Intelligence Assistant", layout="wide")
st.title("🚀 AI Business Intelligence & Risk Assistant")
st.caption("AI-powered business risk & growth analysis (Developed By Yash Mandlik)")
st.divider()

# -------------------------------------------------
# Session State
# -------------------------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

# -------------------------------------------------
# KPI Inputs
# -------------------------------------------------
st.subheader("📊 Business KPIs")

col1, col2 = st.columns(2)
with col1:
    monthly_sales = st.number_input("Monthly Sales", value=120)
    revenue = st.number_input("Revenue", value=40000)
    customer_count = st.number_input("Customer Count", value=300)
with col2:
    churn_rate = st.slider("Churn Rate", 0.0, 1.0, 0.42)
    support_tickets = st.number_input("Support Tickets", value=80)
    marketing_spend = st.number_input("Marketing Spend", value=5000)

avg_product_cost = st.number_input("Average Product Cost", value=500)

repeat_customers = st.number_input(
    "Repeat Customer Count", min_value=0, max_value=customer_count, value=120
)

feedback_text = st.text_area(
    "📝 Customer / Employee Feedback", "Service quality is poor and support is very slow"
)

# -------------------------------------------------
# Analyze Button
# -------------------------------------------------
if st.button("🔍 Analyze Business"):
    st.session_state.analyzed = True

# =================================================
# ANALYSIS
# =================================================
if st.session_state.analyzed:

    business_data = {
        "monthly_sales": monthly_sales,
        "revenue": revenue,
        "customer_count": customer_count,
        "churn_rate": churn_rate,
        "support_tickets": support_tickets,
        "marketing_spend": marketing_spend
    }

    with st.spinner("Running AI analysis..."):
        text_result = analyze_text(feedback_text)
        result = calculate_risk(business_data, text_result)
        save_risk_history(result["risk_score"])

    # -------------------------------------------------
    # SUMMARY
    # -------------------------------------------------
    st.divider()
    st.subheader("📈 Business Summary")

    total_cost = marketing_spend + (avg_product_cost * customer_count)
    profit = revenue - total_cost
    repeat_customer_pct = (repeat_customers / customer_count) * 100 if customer_count else 0
    profitable_status = "✅ Profitable" if profit > 0 else "❌ Not Profitable"

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("AI Risk Score", result["risk_score"])
    c1.metric("Risk Level", result["risk_level"])
    c2.metric("Profit", profit)
    c3.metric("Churn %", round(churn_rate * 100, 2))
    c4.metric("Repeat Customers %", f"{round(repeat_customer_pct, 2)}%")
    c5.metric("Business Status", "PROFITABLE" if profit > 0 else "LOSS", delta=profit)
    st.info(f"📊 **Business Profitability Status:** {profitable_status}")

    # -------------------------------------------------
    # WHY AI PREDICTED THIS RISK
    # -------------------------------------------------
    st.divider()
    st.subheader("🔍 Why AI Predicted This Risk")

    shap_df = pd.DataFrame({
        "Feature": result["shap_values"].keys(),
        "Impact": result["shap_values"].values()
    }).sort_values("Impact", key=abs, ascending=False)

    st.altair_chart(
        alt.Chart(shap_df).mark_bar().encode(
            x="Impact",
            y=alt.Y("Feature", sort="-x"),
            color=alt.condition(
                alt.datum.Impact > 0,
                alt.value("#ff4b4b"),
                alt.value("#00c853")
            ),
            tooltip=["Feature", "Impact"]
        ).properties(height=350),
        use_container_width=True
    )

    # -------------------------------------------------
    # ACTIONABLE SUGGESTIONS
    # -------------------------------------------------
    st.divider()
    st.subheader("💡 Actionable Suggestions")

    if profit < 0:
        st.error("🚨 Business is Running in Loss")
        st.markdown("- Reduce operational costs immediately")
        st.markdown("- Re-evaluate pricing strategy")
        st.markdown("- Improve repeat customer retention")
        st.markdown("- Optimize marketing spend")
    elif result["risk_level"] == "HIGH":
        st.error("🚨 High Business Risk")
        st.markdown("- Reduce churn urgently")
        st.markdown("- Improve support response time")
        st.markdown("- Optimize marketing spend")
    elif result["risk_level"] == "MEDIUM":
        st.warning("⚠ Medium Risk")
        st.markdown("- Improve customer retention")
        st.markdown("- Monitor expenses carefully")
    else:
        st.success("✅ Business is Healthy and Profitable")



    # -------------------------------------------------
    # CUSTOMER FEEDBACK INTELLIGENCE
    # -------------------------------------------------
    st.divider()
    st.subheader("🧠 Customer Feedback Intelligence")

    c1, c2 = st.columns(2)
    c1.metric("Sentiment", text_result["sentiment"])
    c1.metric("Confidence", text_result["confidence"])

    with c2:
        st.write("🔍 Key Issues")
        for t in text_result["topics"]:
            st.write(f"- {t}")

    # -------------------------------------------------
    # REVENUE TREND
    # -------------------------------------------------
    st.divider()
    st.subheader("📊 Revenue Trend (Last 6 Months)")

    df_rev = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Revenue": [
            revenue * 0.7, revenue * 0.8, revenue * 0.85,
            revenue * 0.9, revenue, revenue * 1.05
        ]
    })

    st.altair_chart(
        alt.Chart(df_rev).mark_line(point=True).encode(
            x="Month",
            y="Revenue"
        ),
        use_container_width=True
    )

    # -------------------------------------------------
    # PROFIT VS EXPENSE
    # -------------------------------------------------
    st.divider()
    st.subheader("💰 Profit vs Expense Breakdown")

    df_pe = pd.DataFrame({
        "Category": ["Revenue", "Total Expenses", "Profit"],
        "Amount": [revenue, total_cost, profit]
    })

    st.altair_chart(
        alt.Chart(df_pe).mark_bar().encode(
            x="Category",
            y="Amount"
        ),
        use_container_width=True
    )

    # -------------------------------------------------
    # RISK TREND
    # -------------------------------------------------
    st.divider()
    st.subheader("📈 Risk Trend Over Time")

    history_df = load_risk_history()
    if len(history_df) >= 2:
        st.altair_chart(
            alt.Chart(history_df).mark_line(point=True).encode(
                x="timestamp:T",
                y="risk_score:Q"
            ),
            use_container_width=True
        )
    else:
        st.info("Not enough historical data yet")

    # -------------------------------------------------
    # AI BUSINESS ADVISOR (LLAMA CHAT)
    # -------------------------------------------------
    st.divider()
    st.subheader("🤖 Ask AI for Business Growth Advice")
    user_q = st.text_input(
        "Ask anything to improve your business (sales, profit, retention, costs, etc.)"
    )

    if st.button("Ask AI"):
        context = {
            "risk_level": result["risk_level"],
            "profit": profit,
            "churn": churn_rate,
            "repeat_pct": repeat_customer_pct,
            "sentiment": text_result["sentiment"]
        }
        with st.spinner("AI is thinking..."):
            ai_reply = ask_llama(user_q, context)
        st.session_state.chat_history.append(("You", user_q))
        st.session_state.chat_history.append(("AI", ai_reply))

    # -------------------------------------------------
    # CHAT HISTORY
    # -------------------------------------------------
    for role, msg in st.session_state.chat_history[-6:]:
        if role == "You":
            st.markdown(f"**🧑 You:** {msg}")
        else:
            st.markdown(f"**🤖 AI Advisor:** {msg}")