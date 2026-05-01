import streamlit as st
import pandas as pd
from collections import Counter
import plotly.express as px

st.set_page_config(layout="wide")

st.markdown("""
<style>
body {background: #0b0f2b;}
.block-container {padding-top: 2rem;}

.card {
    background: linear-gradient(135deg, #1f2a60, #0b0f2b);
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0 0 20px rgba(34,211,238,0.1);
}

.metric {
    font-size: 28px;
    font-weight: bold;
    color: #e0e7ff;
}

.label {
    font-size: 14px;
    color: #94a3b8;
}

.section {
    background: #11163a;
    padding: 20px;
    border-radius: 18px;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

df = pd.read_csv("data/curated/final.csv")

df["rating"] = df["sentiment"].map({
    "positive": 5,
    "neutral": 3,
    "negative": 1
})

st.title("Luggage Intelligence Dashboard")

brand = st.selectbox("Brand", df["brand"].unique())
data = df[df["brand"] == brand]

sent_filter = st.selectbox("Sentiment Filter", ["all","positive","negative","neutral"])
if sent_filter != "all":
    data = data[data["sentiment"] == sent_filter]

total = len(data)
pos = (data["sentiment"] == "positive").sum()
neg = (data["sentiment"] == "negative").sum()
avg_rating = round(data["rating"].mean(), 2) if total > 0 else 0

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f'<div class="card"><div class="metric">{total}</div><div class="label">Total Reviews</div></div>', unsafe_allow_html=True)

with c2:
    st.markdown(f'<div class="card"><div class="metric">{pos}</div><div class="label">Positive</div></div>', unsafe_allow_html=True)

with c3:
    st.markdown(f'<div class="card"><div class="metric">{neg}</div><div class="label">Negative</div></div>', unsafe_allow_html=True)

with c4:
    st.markdown(f'<div class="card"><div class="metric">{avg_rating}</div><div class="label">Avg Rating</div></div>', unsafe_allow_html=True)

c5, c6 = st.columns(2)

with c5:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("Sentiment Distribution")

    sent = data["sentiment"].value_counts().reset_index()
    sent.columns = ["sentiment", "count"]

    fig1 = px.bar(
        sent,
        x="sentiment",
        y="count",
        color="sentiment",
        color_discrete_sequence=["#ec4899", "#22d3ee", "#8b5cf6"]
    )

    fig1.update_layout(plot_bgcolor="#11163a", paper_bgcolor="#11163a", font_color="#e0e7ff")
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c6:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("Brand Comparison (Positive %)")

    comp = df.groupby("brand")["sentiment"].value_counts(normalize=True).unstack().fillna(0)
    comp = (comp["positive"] * 100).reset_index()
    comp.columns = ["brand", "positive_percent"]

    fig2 = px.bar(comp, x="brand", y="positive_percent", color="brand")
    fig2.update_layout(plot_bgcolor="#11163a", paper_bgcolor="#11163a", font_color="#e0e7ff")
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Brand Comparison (Review Count)")
st.bar_chart(df["brand"].value_counts())
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Insight")

percent = round((pos / total) * 100) if total > 0 else 0

if percent > 70:
    st.success(f"{percent}% positive → strong satisfaction")
elif percent > 50:
    st.warning(f"{percent}% positive → mixed sentiment")
else:
    st.error(f"{percent}% positive → issues detected")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Top Complaints")

neg_reviews = data[data["sentiment"] == "negative"]["review_text"]

keywords = {"zipper","wheel","handle","broken","lock","damage","scratch","defect"}

words = []
for r in neg_reviews:
    for w in r.lower().split():
        w = w.strip(".,!?()")
        if w in keywords:
            words.append(w)

common = Counter(words).most_common(8)

if common:
    for w, c in common:
        st.write(f"{w} ({c})")
else:
    st.info("No major recurring issues detected for this brand")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Top Positive Themes")

pos_reviews = data[data["sentiment"] == "positive"]["review_text"]

words = []
for r in pos_reviews:
    for w in r.lower().split():
        w = w.strip(".,!?()")
        if len(w) > 3:
            words.append(w)

common = Counter(words).most_common(8)

if common:
    for w, c in common:
        st.write(f"{w} ({c})")
else:
    st.info("No strong positive themes detected")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Sample Reviews")
st.dataframe(data.sample(min(10, len(data))), use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)