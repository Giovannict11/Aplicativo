{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": None,  # Corrigido de 'null' para 'None'
   "id": "79b3b3cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "# Opções extraídas da planilha (3ª opção para cada mecanismo)\n",
    "mecanismos_opcoes = {\n",
    "    \"Perda de Espessura Uniforme\": \"> 50% dos PCEs com ME\",\n",
    "    \"Perda de Espessura Localizada\": \"Varredura > 60% dos trechos retos + 100% de áreas críticas\",\n",
    "    \"Corrosão Externa em Ambientes Agressivos\": \"Inspeção visual em > 75% da área superficial e ensaios NDT em 50% das áreas críticas\",\n",
    "    \"Corrosão Externa em Ambientes em Geral\": \"Inspeção visual em > 75% da área superficial e ensaios NDT em 25% das áreas críticas\",\n",
    "    \"Corrosão Sob Isolamento (com remoção do isolamento)\": \"Para a totalidade da área superficial: 100% de inspeção visual + 50% de ensaios NDT\",\n",
    "    \"Corrosão Sob Isolamento (sem remoção do isolamento)\": \"100% de inspeção visual + >35% de inspeção por NDT\",\n",
    "    \"Componentes Enterrados (inspeção intrusiva)\": \"Inspeção interna empregando PIGs umbilicais ou testes hidrostáticos\",\n",
    "    \"Componentes Enterrados (inspeção não intrusiva)\": \"Inspeção de > 80% do revestimento anticorrosivo e inspeção por CP\"\n",
    "}\n",
    "\n",
    "st.title(\"Seleção de Mecanismos\")\n",
    "st.write(\"Escolha a melhor opção para cada mecanismo\")\n",
    "\n",
    "selecoes = {}\n",
    "for mecanismo, opcao in mecanismos_opcoes.items():\n",
    "    selecoes[mecanismo] = st.selectbox(mecanismo, list(mecanismos_opcoes.values()), index=2)\n",
    "\n",
    "if st.button(\"Avançar\"):\n",
    "    st.session_state[\"selecoes\"] = selecoes\n",
    "    st.session_state[\"fase\"] = \"notas\"\n",
    "    st.experimental_rerun()\n",
    "\n",
    "if \"fase\" in st.session_state and st.session_state[\"fase\"] == \"notas\":\n",
    "    st.title(\"Inserir Notas\")\n",
    "    st.write(\"Atribua uma nota para cada mecanismo\")\n",
    "    \n",
    "    notas_validas = [\"A\", \"B\", \"C\", \"D\"]\n",
    "    notas = {}\n",
    "    for mecanismo in mecanismos_opcoes.keys():\n",
    "        notas[mecanismo] = st.selectbox(f\"Nota para {mecanismo}\", notas_validas, index=3)\n",
    "    \n",
    "    if st.button(\"Salvar e Exibir Resultado\"):\n",
    "        dados = []\n",
    "        for mecanismo in mecanismos_opcoes.keys():\n",
    "            dados.append([mecanismo, st.session_state[\"selecoes\"][mecanismo], notas[mecanismo]])\n",
    "        \n",
    "        df = pd.DataFrame(dados, columns=[\"Mecanismo\", \"Opção Selecionada\", \"Nota\"])\n",
    "        df.to_excel(\"resultado.xlsx\", index=False)\n",
    "        \n",
    "        st.session_state[\"resultado\"] = df\n",
    "        st.session_state[\"fase\"] = \"resultado\"\n",
    "        st.experimental_rerun()\n",
    "\n",
    "if \"fase\" in st.session_state and st.session_state[\"fase\"] == \"resultado\":\n",
    "    st.title(\"Resultado Final\")\n",
    "    \n",
    "    df = st.session_state[\"resultado\"]\n",
    "    st.dataframe(df)\n",
    "    \n",
    "    menor_nota = min(df[\"Nota\"], key=lambda x: [\"D\", \"C\", \"B\", \"A\"].index(x))\n",
    "    st.write(f\"**Menor Nota Atribuída: {menor_nota}**\")\n",
    "    \n",
    "    st.write(\"Os dados foram salvos no arquivo 'resultado.xlsx'\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
