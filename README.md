# Criando-um-Sistema-Banc-rio-com-Python
Este projeto é uma solução simples e funcional para operações bancárias básicas, desenvolvido como parte do bootcamp da [DIO](https://www.dio.me/). O sistema permite realizar **depósitos**, **saques com regras específicas**, **emissão de extrato**, além de **cadastrar usuários e contas correntes**.

---

## 🚀 Funcionalidades

- ✅ Depósito de valores positivos
- ✅ Saque limitado a 3 operações diárias
- ✅ Valor máximo por saque: R$ 500,00
- ✅ Verificação de saldo antes do saque
- ✅ Registro detalhado das transações
- ✅ Extrato formatado com histórico de operações
- ✅ Cadastro de usuários com CPF único
- ✅ Criação de contas correntes vinculadas aos usuários
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

### 👤 Cadastro de Usuário
- Campos: nome, data de nascimento, CPF (somente números) e endereço
- Endereço no formato: `logradouro, número - bairro - cidade/sigla estado`
- CPF deve ser único — não é permitido duplicatas
- Os usuários são armazenados em uma lista de dicionários

### 🏦 Criação de Conta Corrente
- Cada conta contém:
  - Agência (fixa: `"0001"`)
  - Número da conta (sequencial)
  - CPF do usuário vinculado
- Um usuário pode ter **várias contas**
- Uma conta pertence a apenas **um único usuário**
- As contas são armazenadas em uma lista de dicionários

---

## 🛠️ Tecnologias Utilizadas

- 🐍 Python 3.x
- 💻 Interface via terminal (CLI)
- 📦 Estrutura com listas, dicionários e funções (`def`)

---

## 🧠 Aprendizados aplicados

Este projeto consolida os conceitos fundamentais de:

- Estruturas condicionais (`if`, `elif`, `else`)
- Estruturas de repetição (`while`)
- Funções com e sem parâmetros
- Argumentos posicionais e nomeados
- Dicionários e listas
- Interpolação e formatação de strings (`f-strings`)
- Organização da lógica por funções reutilizáveis

---

## 🔧 Melhorias futuras (sugestões)

- Implementar autenticação de usuário
- Armazenar transações e usuários em arquivos (`.json`, `.csv`)
- Criar interface gráfica (GUI)
- Utilizar classes e orientação a objetos (OOP)
- Validação de CPF e campos obrigatórios

---

## 📁 Execução

Basta ter o Python instalado e executar o script:

```bash
python sistema_bancario.py

