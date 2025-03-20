# 📍 Validador de CEP com TDD

Este projeto implementa um **validador de CEP** que verifica se um determinado CEP pertence à cidade informada, utilizando uma base de dados em planilha Excel (`ceps.xlsx`). O código segue a **metodologia TDD (Test-Driven Development)** e o fluxo de versionamento **Gitflow**.

---

## 🚀 **Funcionalidades**
- Valida o **formato** do CEP (8 dígitos, com ou sem hífen).
- Valida se o **nome da cidade** segue o padrão correto.
- Confere se o CEP informado **pertence à cidade** na base de dados (`ceps.xlsx`).
- Testes automatizados:
  - **Testes unitários** ✅

---

## ⚙️ **Como Executar o Projeto**
### 1️⃣ **Instalar as dependências**
Certifique-se de que o Python (versão 3.9 ou superior) está instalado e rode:

```bash
pip install -r requirements.txt
```
*(Se necessário, crie um ambiente virtual antes: `python -m venv venv && source venv/bin/activate` no Linux/macOS ou `venv\Scripts\activate` no Windows.)*

---

### 2️⃣ **Executar a Validação de CEP**
Você pode testar a validação diretamente no Python:

```python
from cep import valida_CEP

print(valida_CEP("69945000", "Acrelandia"))  # Retorna True se válido
```

---

### 3️⃣ **Rodar os Testes Automatizados**
Execute os testes unitários e de integração com:

```bash
pytest cep_test.py -v
```

---

## 🛠️ **Fluxo Gitflow**
Este projeto utiliza **Gitflow** para organizar o desenvolvimento. O fluxo de trabalho esperado é:

1️⃣ Criar uma nova funcionalidade:
```bash
git checkout develop
git pull origin develop
git checkout -b feature/nova-funcionalidade
```
🔹 **Trabalhe no código e faça commits**  
🔹 Após finalizar, **envie para o repositório**:
```bash
git push origin feature/nova-funcionalidade
```
🔹 Abra um **Pull Request** para a branch `develop` e aguarde revisão.

---

## 🔥 **Deploy e Releases**
Quando uma versão estável estiver pronta, siga o fluxo:

1️⃣ Criar a branch de release:
```bash
git checkout develop
git pull origin develop
git checkout -b release/v1.0.0
```
2️⃣ Corrigir possíveis bugs, fazer merge na `main` e criar uma tag:
```bash
git checkout main
git merge release/v1.0.0
git tag -a v1.0.0 -m "Primeira versão estável"
git push origin main --tags
```
3️⃣ Finalmente, **atualizar `develop`**:
```bash
git checkout develop
git merge main
git push origin develop
```

---

## 📋 **Automação com GitHub Actions**
Sempre que houver um **push ou pull request** para a branch `main`, o GitHub Actions executará:

✅ **Testes Unitários**  
✅ **Verificação de Código**

Para acompanhar os resultados, acesse a aba **"Actions"** no GitHub.