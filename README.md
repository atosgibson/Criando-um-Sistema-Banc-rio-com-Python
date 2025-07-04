# Criando-um-Sistema-Banc-rio-com-Python
Este projeto é uma solução simples e funcional para operações bancárias básicas, desenvolvido como parte do bootcamp da [DIO](https://www.dio.me/). O sistema permite realizar **depósitos**, **saques com regras específicas** e **emissão de extrato**.

---

## 🚀 Funcionalidades

- ✅ Depósito de valores positivos
- ✅ Saque limitado a 3 operações diárias
- ✅ Valor máximo por saque: R$ 500,00
- ✅ Verificação de saldo antes do saque
- ✅ Registro detalhado das transações
- ✅ Extrato formatado com histórico de operações
- ✅ Interface interativa via terminal

---

## 📜 Regras do Sistema

### 🔐 Saque
- Máximo de **3 saques por dia**
- Cada saque pode ter o valor **máximo de R$ 500,00**
- Não é possível sacar se o saldo for insuficiente
- Mensagens claras em caso de falha

### 💸 Depósito
- Apenas valores **positivos** são aceitos
- Valores inválidos são rejeitados com aviso

### 🧾 Extrato
- Lista todas as movimentações realizadas
- Exibe o saldo atual ao final
- Valores formatados no padrão monetário brasileiro

---

## 🛠️ Tecnologias Utilizadas

- 🐍 Python 3.x
- 💻 Interface via terminal (CLI)
- 📦 Estrutura simples com variáveis e controle de fluxo (`if`, `while`, `for`)

---

## 🧠 Aprendizados aplicados

Este projeto consolida os conceitos fundamentais de:

- Estruturas condicionais (`if`, `elif`, `else`)
- Estruturas de repetição (`while`)
- Operadores lógicos e relacionais
- Interpolação e formatação de strings (`f-strings`)
- Organização de lógica de negócios

---

## 🔧 Melhorias futuras (sugestões)

- Refatorar em funções (`def`)
- Implementar autenticação de usuário
- Armazenar transações em arquivo `.txt` ou `.json`
- Versão com interface gráfica (GUI)
- Uso de classes e orientação a objetos

---

## 📁 Execução

Basta ter o Python instalado e executar o script:

```bash
python sistema_bancario.py
