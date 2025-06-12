![Logos MCTI, CNPEM e ILUM](https://pages.cnpem.br/MLSchool/wp-content/uploads/sites/143/2023/05/logo-ilum.png)
<h1 align='center'> Algoritmos Genéticos para Otimizar Dietas 🥗 </h1>

<p align="center"><strong>Autoras:</strong> Katarina da Silva Vilarins, Maria Emily Nayla Gomes da Silva e Raquel de Godoy Vianna</p>
<p align="center"><strong>Orientador:</strong> Prof. Dr. Daniel R. Cassar</p>

<p align="center">
<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

## 📝 Descrição
<p align="justify">Atualmente, a população mundial enfrenta dificuldades para zelar plenamente por sua saúde. Nesse cenário, rotas para auxiliar no cuidado individual com a alimentação desempenham papel fundamental na busca por um estilo de vida de qualidade. Contudo, a elaboração de uma dieta adequada é trabalhosa e demanda investigação pessoal e profissional voltada para o interesse e motivação do paciente. Diante dessa temática e em conjunto com conceitos apresentados no contexto de algoritmos genéticos, o grupo propôs elaborar uma solução para a busca de dietas, tratando-a como um problema de otimização. Ao se falar em busca de dietas otimizadas, o objetivo é encontrar algumas opções de dietas que se apresentem como as melhores diante das restrições fornecidas. Para isso, adaptamos a função para gerar genes de caixa não binária, considerando que o intervalo razoável de porções de um alimento por dia varia entre 0 e 3. Além disso, desenvolveu-se uma função objetivo que penaliza cada gene fora do intervalo definido — as restrições — e utilizou-se dois tipos de seleção: por torneio e por amostragem universal estocástica.</p>

## 📔 Notebooks e arquivos do projeto
* `Left Hand Matrix from All Observed Food Patterns of Patients.csv`: Dataset utilizado encontrado em: [CSSEHealthcare/Dietary-Behavior-Dataset](https://github.com/CSSEHealthcare/Dietary-Behavior-Dataset) - This repository includes dietary data from the NHANES 2015-2016 survey in a workable format for researchers. Additional samples from hypertension and prediabetic patients are also provided.
* `notebook_principal.ipynb`:
* `funcoes_dieta.py`: Script com as funções criadas para o algoritmo genético no problema de dietas otimizadas.
* `README.md`: descrição geral do projeto.

## 🪼 Funções adaptadas para o problema das dietas otimizadas

## 😁 Conclusão
<p align="justify">Por fim, a função de criação de genes, a função objetivo e a função de seleção — que combina dois métodos: torneio e amostragem universal estocástica — foram devidamente implementadas em conjunto com as de algoritmos genéticos da biblioteca <code>deap</code>, a qual foi fundamental para encontrar, com eficiência, diversas dietas capazes de se adequar às restrições propostas. Ao implementar todas as funções necessárias para adaptar o algoritmo genético ao problema das dietas otimizadas, realizou-se a validação do código com três conjuntos distintos de restrições: uma dieta básica para um estilo de vida saudável, uma com o objetivo de emagrecimento e outra voltada para fisiculturistas. A ideia é demonstrar que, de acordo com o objetivo do indivíduo, haverá diferentes restrições e que, a partir delas e de um dataset com as informações nutricionais dos alimentos, é possível encontrar uma dieta personalizada.</p>

## 🖇️ Informações técnicas
* Linguagem de programação: `Python 3.9`
* Software:  `Jupyter Notebook`
* Bibliotecas e Módulos: `random`, `deap`

 ## 👩‍🦳 Referências

 <!-- 
 ## 🧠 Contribuições dos Colaboradores


#### Para o Projeto:
* Emily Gomes: Atualizações na construção, treinamento e análise da previsão de uma CNN utilizando o Lightning.
* Yasmin Shimizu: Atualizações na construção, treinamento e análise da previsão de uma CNN utilizando o Lightning.

#### Para o Repositório GitHub:
* Emily Gomes: README e upload do notebook Jupyter referente a construção, treinamento e previsão da CNN.
* Yasmin Shimizu: README, upload de imagens e upload do notebook Jupyter referente à figura "24Imagens_MNIST.png".


**Orientação e Revisão:** Prof. Dr. Daniel R. Cassar.
 -->

 <h2 align="center"> :octocat:  Autoras </h2>

<div align="center">


| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/172424897?v=4" width=115><br><sub> Maria Emily Nayla</sub>](https://github.com/MEmilyGomes)<br> [<sub>Ilum - CNPEM</sub>](https://ilum.cnpem.br/)<br> [<sub>Currículo Lattes</sub>](http://lattes.cnpq.br/9482558334105708)<br> | [<img loading="lazy" src="https://github.com/user-attachments/assets/bcfca6b9-f8dd-44ad-ad53-cb44418cdc5c" width=115><br><sub>Katarina Vilarins</sub>](https://github.com/KatarinaVilarins)<br> [<sub>Ilum - CNPEM</sub>](https://ilum.cnpem.br/)<br> [<sub>Linkedin</sub>](https://www.linkedin.com/in/yasminbshimizu/) | [<img loading="lazy" src="https://github.com/user-attachments/assets/abf88829-f67d-4d53-8a36-0bf7d70d21e4" width=115><br><sub>Raquel de Godoy Vianna</sub>](https://github.com/RaquelGVianna)<br> [<sub>Currículo Lattes</sub>](https://lattes.cnpq.br/7590950936353244)<br> [<sub>Linkedin</sub>](https://www.linkedin.com/in/raquel-de-godoy-vianna-58b5b92a7?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
| :---: | :---: | :---: |

 <h2 align="center"> :octocat:  Orientador </h2>

<div align="center">

| [<img loading="lazy" src="https://github.com/user-attachments/assets/463d4753-7fa4-4a42-aa54-409e4150bb51" width=115><br> <sub> Prof. Dr. Daniel R. Cassar </sub>](https://github.com/drcassar)<br> [<sub>Ilum - CNPEM</sub>](https://ilum.cnpem.br/)<br> [<sub>Currículo Lattes</sub>](http://lattes.cnpq.br/1717397276752482) |
| :---: |

#### Para o Projeto e para Repositório GitHub:
* Katarina Vilarins: implementação da função objetivo e comentários no notebook.  
* Emily Gomes: implementação do `deap`, implementação da função objetivo e README.  
* Raquel Vianna: implementação do `deap`, implementação da função mista, implementação da função objetivo e README.  


**Orientação e Revisão:** Prof. Dr. Daniel R. Cassar.
