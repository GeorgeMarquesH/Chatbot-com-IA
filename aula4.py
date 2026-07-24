# titulo
# input do chat (campo de mensagem)
# a cada mensagem que o usuario enviar:
    # mostrar a mensagem que o usuario enviou no chat
    # enviar essa mensagem para a IA responder
    # exibir a resposta da IA na tela

# streamlit - apenas com Python cria frontend e backend
# a ia que vamos usar: OpenAI
# pip install openai e streamlit

import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key="")

st.write("# ChatBot com IA") # markdown

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

texto_usuario = st.chat_input("Digite sua mensagem")
# arquivo = st.file_uploader("Selecione um arquivo")


for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)
    # nome
    # user
    # assistant

    # ia respondeu
    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-3.5-turbo"
    )
    # print(resposta_ia.choices[0].message.content)
    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
    # print(st.session_state["lista_mensagens"])