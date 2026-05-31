# 👾 Mini Tamagotchi em Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/Architecture-Procedural%20%2F%20Clean%20Code-green?style=for-the-badge" alt="Architecture">
  <img src="https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge" alt="Status">
</p>

Um simulador de bichinho virtual (Tamagotchi) baseado em texto, desenvolvido para rodar diretamente no terminal. O foco principal deste projeto foi aplicar boas práticas de desenvolvimento, blindagem de código contra erros de usuários (*crashes*) e garantir possível reutilização do código.

---

## 🎮 Como Jogar

O Tamagotchi inicia com **5 de Energia** e **5 de Fome**. Seu objetivo é manter os status equilibrados escolhendo as ações no menu:

* **1 - Alimentar:** Reduz a fome do pet.
* **2 - Brincar:** Consome energia, mas aumenta a fome (o pet gasta calorias!).
* **3 - Descansar:** Recarrega totalmente os níveis de energia.
* **4 - Ver Status:** Exibe os níveis atuais de Fome e Energia.
* **5 - Sair:** Encerra o jogo.

---

## 🛠️ Destaques Técnicos & Boas Práticas Aplicadas

Este projeto vai além da lógica básica de condicionais e foca em padrões reais de engenharia de software:

### 1. Robustez e Tratamento de Exceções (`try / except / else`)
O jogo é **à prova de falhas na digitação**. Se o usuário digitar letras (como `"asd"`) em um menu numérico, o Python normalmente geraria um erro de valor (`ValueError`) e fecharia o programa. 
Neste código, a falha é capturada de forma limpa:
* O bloco `try` isola estritamente a entrada do usuário.
* O `except ValueError` trata a falha sem derrubar o sistema.
* O bloco `else` garante que as ações do jogo **só sejam processadas se o dado de entrada for 100% seguro**.

### 2. Eliminação de "Números Mágicos" & Constantes Globais
Valores limites de estado não foram espalhados pelo código de forma fixa. Foram definidas **Constantes Globais** (`MAX_ENERGIA`, `MIN_FOME`, etc.) no topo do arquivo, seguindo o padrão de nomenclatura **PEP 8** (letras maiúsculas). Isso permite recalibrar toda a dificuldade ou escala do jogo alterando apenas uma linha.

### 3. Código Auto-documentado (*Clean Code*)
Dentro das funções, todas as taxas de modificação receberam nomes significativos e contextuais, como:
* `buff_alimentar`
* `custo_energia_brincar`
* `buff_descansar`

Isso elimina a necessidade de comentários redundantes e torna a leitura do código natural para qualquer desenvolvedor.

### 4. Modularização Dinâmica e Retornos Múltiplos
As variáveis de estado nunca são manipuladas diretamente de forma global pelas funções, evitando efeitos colaterais. O código utiliza passagem de parâmetros limpa e aproveita o recurso nativo de **desempacotamento de tuplas** do Python para retornar múltiplos valores simultâneos (como na função `brincar`, que altera e retorna `energia` e `fome` ao mesmo tempo).

---

## 💻 Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Paradigma:** Programação Estruturada / Procedural

---

## 🧑‍💻 Autor

**Vinicius Müller**
* 🎓 Acadêmico de Sistemas de Informação (1º Semestre, Faculdade Antonio Meneghetti)
* 🎯 Desenvolvido como projeto de consolidação de lógica, modularização e tratamento de dados.

---
<p align="center">
<i>🛡️ "Crux Sacra Sit Mihi Lux" 🛡️</i>
</p>
