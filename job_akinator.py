import streamlit as st

st.set_page_config(page_title="職業アキネーター", page_icon="🧠")
st.title("🧠 職業アキネーター")
st.write("10の質問に答えると、あなたに向いている職業がわかります！")

questions = [
    "新しい技術を学ぶのが好き？",
    "細かいデザインや配色にこだわる？",
    "人の心理を分析するのが得意？",
    "データを見るのが好き？",
    "問題解決が得意？",
    "チームをまとめるのが得意？",
    "文章やストーリーを書くのが好き？",
    "数学・論理的思考が得意？",
    "SNSやトレンドに敏感？",
    "いろんな業界に興味ある？"
]

score_map = {
    0: {"エンジニア": 2},
    1: {"デザイナー": 2},
    2: {"マーケター": 2},
    3: {"エンジニア": 1, "コンサルタント": 1},
    4: {"コンサルタント": 2},
    5: {"コンサルタント": 2},
    6: {"マーケター": 2},
    7: {"エンジニア": 2},
    8: {"マーケター": 2},
    9: {"コンサルタント": 1, "マーケター": 1}
}

scores = {
    "エンジニア": 0,
    "デザイナー": 0,
    "マーケター": 0,
    "コンサルタント": 0
}

with st.form("akinator_form"):
    st.write("以下の質問に答えてください（はい or いいえ）:")
    responses = []
    for i, question in enumerate(questions):
        answer = st.radio(question, ["はい", "いいえ"], key=f"q{i}")
        responses.append(answer)

    submitted = st.form_submit_button("診断する")

if submitted:
    for i, answer in enumerate(responses):
        if answer == "はい":
            for job, point in score_map[i].items():
                scores[job] += point

    recommended = max(scores, key=scores.get)

    st.success(f"🎉 あなたに向いている職業は… **{recommended}** です！")
    st.write("### スコア内訳")
    st.bar_chart(scores)
