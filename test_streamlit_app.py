import streamlit as st

st.title("Streamlitの動作確認")
st.write("ブラウザーにこの画面が表示されれば成功です。")

name = st.text_input("名前を入力してください")

if name:
    st.success(f"こんにちは、{name}さん！")

grammar = st.selectbox(
    "試してみたい文法項目",
    ["受動態", "関係節", "比較級"],
)
st.write(f"選択中: {grammar}")