# Desafio Técnico Trunts.Rocks
***
## Critérios de avaliação
- Bom entendimento do problema a ser resolvido;
- Êxito na implementação da funcionalidade;
- Estrutura do código fonte;
- Documentação e utilização de boas práticas;
- Utilização de ferramentas de desenvolvimento básicas.
***
## Desafio
Criar uma aplicação em uma linguagem de programação de sua preferência que deve ser capaz de ler uma planilha do google sheets, buscar as informações necessárias, calcular e escrever o resultado na planilha.
***
## Regras:
Calcular a situação de cada aluno baseado na média das 3 provas (P1, P2 e P3), conforme a  tabela:

Média (m) Situação:
m<5  - Reprovado por Nota
5<=m<7  - Exame Final
m>=7  - Aprovado

Caso o número de faltas ultrapasse 25% do número total de aulas o aluno terá a situação  "Reprovado por Falta", independente da média.  Caso a situação seja "Exame Final" é necessário calcular a "Nota para Aprovação Final"(naf) de  cada aluno de acordo com seguinte fórmula:

5 <= (m + naf)/2

Caso a situação do aluno seja diferente de "Exame Final", preencha o campo "Nota para  Aprovação Final" com 0.
Arredondar o resultado para o próximo número inteiro (aumentar) caso necessário. Utilizar linhas de logs para acompanhamento das atividades da aplicação.
***
## Linguagem escolhida
<a href="https://www.python.org/"><img src="https://www.python.org/static/img/python-logo.png"></a>
***
## Pré-requisitos
- Python 3.10.7 ou superior
- A ferramenta de gerenciamento de pacotes <a href="https://pypi.python.org/pypi/pip" target="_blank">pip</a>
***
### Instruções para Execução da Aplicação
***
- #### Clone o repositório
  <pre><code>git clone https://github.com/yagowill/desafio-tunts.rocks.git
  cd desafio-tunts.rocks</code></pre>

- #### Crie um ambiente virtual
  <pre><code>python -m venv venv</code></pre>

- #### Ative o ambiente virtual
  **Linux/Mac**
  <pre><code>source venv/bin/activate</code></pre>
  **Windows cmd**
  <pre><code>.\venv\Scripts\activate.bat</code></pre>
- #### Instale as depedências
  <pre><code>pip install -r requirements.txt</code></pre>
- #### Execute o script
  <pre><code>python main.py</code></pre>
***
### Resultado
Link da planilha: <https://docs.google.com/spreadsheets/d/1W4yVT1mnWXM-IfUwjBuwA4YoGjOweaacCgZNFB1zJB0/edit#gid=0>
***
### Referência
Documentação da Google Sheets: <https://developers.google.com/sheets/api/guides/concepts>