# Conversor de Temperatura em Python

Este é um projeto simples em Python para conversão entre as escalas **Celsius**, **Fahrenheit** e **Kelvin**. O foco deste projeto é a implementação de **CI/CD** com testes automatizados, linting e formatação de código.

## Funcionalidades
- Converter de Celsius para Fahrenheit e vice-versa.
- Converter de Celsius para Kelvin e vice-versa.
- Converter de Fahrenheit para Kelvin e vice-versa.

## Testes
O projeto utiliza o framework **`unittest`** para rodar os testes unitários do código e **`flake8`** para garantir que o estilo de código esteja conforme as melhores práticas (PEP 8).

### Como Rodar o Projeto

1. **Instalar as dependências**

   Antes de rodar o projeto, instale as dependências do projeto. Execute o seguinte comando:

   ```bash
   pip install -r requirements.txt

2. **Rodar os Testes Unitários**

   utilizando unittest

   ```bash
   python -m unittest discover -s tests


   se quiser rodar apenas um arquivo de teste específico

   ```bash
    python -m unittest tests/test_conversor_temperatura.py

3. **Rodar o Linter**

   utilizando flake8

   ```bash
   flake8 src/ tests/



