# Conversor de Temperatura em Python

Este é um projeto simples em Python para conversão entre as escalas **Celsius**, **Fahrenheit** e **Kelvin**. O foco deste projeto é a implementação de **CI/CD** com testes automatizados, linting e formatação de código.

## Funcionalidades
- Converter de Celsius para Fahrenheit e vice-versa.
- Converter de Celsius para Kelvin e vice-versa.
- Converter de Fahrenheit para Kelvin e vice-versa.

## Testes
O projeto utiliza o framework **`unittest`** para rodar os testes unitários do código e **`flake8`** para garantir que o estilo de código esteja conforme as melhores práticas.

### Como Rodar o Projeto

1. **Instalar as dependências**

   Antes de rodar o projeto, instale as dependências do projeto. Execute o seguinte comando:

   ```bash
   pip install -r requirements.txt

2. **Rodar os Testes Unitários**

   utilizando unittest

   ```bash
   python -m unittest discover -s tests
   ```

   se quiser rodar apenas um arquivo de teste específico

   ```bash
   python -m unittest tests/test_conversor_temperatura.py
   ```
3. **Rodar o Linter**

   utilizando flake8

   ```bash
   flake8 src/ tests/
   ```

3. **Formatação Automática do Código**
 
   utilizando black

   ```bash
   black src/ tests/
   ```

## Executar a Aplicação 

   Para rodar a aplicação Flask localmente, execute o seguinte comando no terminal

   ```bash
   python app.py
   ```

### Para converter Celsius para Fahrenheit

http://127.0.0.1:5000/celsius-to-fahrenheit?celsius=25

### Para converter Fahrenheit para Celsius

http://127.0.0.1:5000/fahrenheit-to-celsius?fahrenheit=77


### Para converter Celsius para Kelvin

http://127.0.0.1:5000/celsius-to-kelvin?celsius=25

### Para converter Kelvin para Celsius

http://127.0.0.1:5000/kelvin-to-celsius?kelvin=298.15


### Para converter Fahrenheit para Kelvin

http://127.0.0.1:5000/fahrenheit-to-kelvin?fahrenheit=77

### Para converter Kelvin para Fahrenheit

http://127.0.0.1:5000/kelvin-to-fahrenheit?kelvin=298.15


## CI
A configuração do CI foi feita utilizando GitHub Actions

### Passo 1: Checkout do repositório

Esta ação é responsável por garantir que o pipeline tenha acesso à versão mais recente do código no repositório para que ele possa ser verificado e processado.

### Passo 2: Configuração do ambiente Python

O ambiente Python precisa estar configurado antes de instalar as dependências e executar os testes. A versão do Python é especificada para garantir que o código seja executado na versão correta. Neste caso, qualquer versão da linha 3.x será compatível.

### Passo 3: Limpar o cache do pip

Garantir que o pip instale a versão mais recente dos pacotes e evitar que versões antigas de pacotes causam erros durante o processo de CI.

### Passo 4: Instalar as dependências

O arquivo requirements.txt contém todas as bibliotecas necessárias para o projeto, como flake8, black, flask, etc. Este passo assegura que o ambiente esteja configurado com todas as dependências corretas.

### Passo 5: Rodar os testes com unittest

Os testes são um passo essencial para garantir que o código não tenha falhas antes de ser integrado e também com o uso de TDD garantir que as funcionalidades que forem codificadas estejam de acordo com o esperado. O unittest é uma biblioteca de testes unitários que ajuda a validar que as funcionalidades do seu código estão corretas.

### Passo 6: Linting com flake8

O linting é importante para garantir que o código esteja limpo e siga as boas práticas de codificação. O flake8 ajuda a encontrar erros comuns de estilo, como indentação incorreta, variáveis não utilizadas e outros problemas.

### Passo 7: Formatação automática com black

O black é uma ferramenta de formatação de código que garante que todo o código esteja formatado de maneira consistente, sem a necessidade de revisão manual. Ele pode ajustar a indentação, a largura das linhas e outras questões de estilo.

## requirements.txt
### Explicação:

**pip**: O pip é o gerenciador de pacotes do Python, que é usado para instalar as dependências.

**flask**: A biblioteca Flask é usada para construir a aplicação web (caso você tenha uma API ou front-end simples).

**flake8==4.0.1**: A versão 4.0.1 do flake8 é especificada para garantir que a ferramenta de linting seja compatível com o código e os plugins necessários.

**black==22.10.0**: A versão 22.10.0 do black é especificada para garantir que a ferramenta de formatação de código seja a versão mais recente e compatível.

## .flake8
### Explicação:

**max-line-length = 90**: Define que o comprimento máximo das linhas de código será de 90 caracteres.

**inline-quotes = single**: Especifica que o código deve usar aspas simples para strings de uma linha, garantindo consistência no estilo.

**exclude = .git,__pycache__,bin/***: Exclui os diretórios .git, __pycache__ e bin/ da verificação de linting, já que esses diretórios geralmente não contêm código Python ou são gerados automaticamente.