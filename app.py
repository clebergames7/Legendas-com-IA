import streamlit as st
from google import genai

# Configuração da página da web
st.set_page_config(page_title="Gerador de Legendas IA", page_icon="📱")
st.title("📱 Gerador Inteligente de Legendas")
st.write("Crie posts engajantes para suas redes sociais em segundos.")

# Entrada da API Key de forma segura na barra lateral
with st.sidebar:
    api_key = st.text_input("Insira sua Gemini API Key:", type="password")
    st.markdown("[Obtenha sua chave aqui](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br)")

# Formulário principal
produto = st.text_input("O que você quer divulgar? (Ex: Caneca personalizada, Curso de Excel)")
tom_voz = st.selectbox("Qual o tom do texto?", ["Profissional", "Engraçado", "Persuasivo", "Descontraído"])

if st.button("Gerar Legendas"):
    if not api_key:
        st.error("Por favor, insira sua API Key na barra lateral.")
    elif not produto:
        st.warning("Por favor, digite o que você quer divulgar.")
    else:
        with st.spinner("A IA está pensando..."):
            try:
                # Inicializa o cliente oficial da API do Gemini
                client = genai.Client(api_key=api_key)
                
                # Cria o comando (prompt) para a IA
                prompt = f"Escreva 3 opções de legendas criativas para o Instagram sobre: '{produto}'. O tom deve ser {tom_voz}. Inclua emojis e hashtags relevantes."
                
                # Chama o modelo mais rápido e econômico (Gemini 2.5 Flash)
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                
                # Exibe o resultado na tela
                st.success("Pronto! Aqui estão suas opções:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Erro ao conectar com a IA: {e}")
