# 🌧️ Experimento de Mineração de Dados - Tabatinga/AM

## Objetivo da Análise
O objetivo deste experimento é utilizar técnicas de mineração de dados para descobrir padrões que expliquem o regime de chuvas em Tabatinga-AM. Especificamente, busca-se prever a classificação de um mês (como `MuitoChuvoso`, `Normal` ou `MuitoSeco`) com base em atributos como quantidade de chuva, dias de chuva e estação do ano.

## Tarefa e Algoritmo
A tarefa escolhida foi **Classificação**, e o algoritmo utilizado foi o **J48 (Árvore de Decisão)**.

**Justificativa:**
A tarefa de classificação é adequada porque a base de dados já possui um atributo-alvo definido, `Classificacao_Chuva`, que foi criado durante a etapa de Feature Engineering. O algoritmo J48 foi escolhido por sua alta interpretabilidade. Ele gera uma árvore de decisão que é fácil de entender e explicar, o que é essencial para um trabalho acadêmico, e é robusto para trabalhar com dados numéricos e categóricos.

## Atributos Utilizados
Os atributos selecionados para o experimento, além do alvo `Classificacao_Chuva`, foram:
*   `Ano` (Numérico)
*   `Maxima` (Numérico)
*   `Total` (Numérico)
*   `NumDiasDeChuva` (Numérico)
*   `NumDiasSemChuva` (Numérico)
*   `Estacao` (Categórico)

## Configurações e Avaliação
*   **Método de Avaliação:** Foi utilizada a validação cruzada com 10 folds (10-fold cross-validation), que é o padrão recomendado para obter uma estimativa confiável do desempenho do modelo.
*   **Parâmetros Principais (J48):** Foram utilizados os parâmetros padrão do Weka:
    *   `confidenceFactor`: 0.25
    *   `minNumObj`: 2
    *   `unpruned`: False (poda ativada)

## Resultados e Interpretação

### Resultados Obtidos no Weka

*   **Acurácia:** 99,8%
*   **Instâncias Classificadas Corretamente:** 499 de 500
*   **Matriz de Confusão:**
    | Classes Reais \ Previstas | MuitoChuvoso | Normal | MuitoSeco |
    | :--- | :--- | :--- | :--- |
    | **MuitoChuvoso** | 147 | 0 | 0 |
    | **Normal** | 1 | 169 | 0 |
    | **MuitoSeco** | 0 | 0 | 183 |

### Interpretação dos Resultados
A árvore de decisão gerada é extremamente simples e direta:

```bash
Total <= 133.9: MuitoSeco (183.0)
Total > 133.9
| Total <= 267.7: Normal (170.0)
| Total > 267.7: MuitoChuvoso (147.0)
```

Isso significa que o modelo descobriu que a **única variável necessária para classificar os meses é o `Total` de chuva**. As regras são:

1.  **Meses com `Total` menor ou igual a 133.9 mm:** Classificados como `MuitoSeco`.
2.  **Meses com `Total` entre 133.9 mm e 267.7 mm:** Classificados como `Normal`.
3.  **Meses com `Total` maior que 267.7 mm:** Classificados como `MuitoChuvoso`.

**Discussão:** Essas regras são quase idênticas à definição da variável `Classificacao_Chuva` que criamos durante a Feature Engineering. Isso explica a acurácia de 99,8% e o erro de apenas 1 instância na matriz de confusão. O modelo basicamente "reaprendeu" a regra que nós criamos, o que valida que nossa engenharia de atributos estava correta.

## Discussão Crítica
*   **Padrões:** O padrão mais forte encontrado pelo algoritmo é a relação direta entre o `Total` de chuva e a sua classificação. Outras variáveis como `Estacao` ou `Ano` não foram utilizadas na árvore porque o `Total` é um preditor perfeito da classe.
*   **Limitações:** A principal limitação do modelo é que ele é uma "verificação" da nossa própria regra. Ele não descobriu um novo padrão desconhecido, mas sim confirmou a regra que definimos. Outra limitação é a lacuna de dados entre 1999 e 2015, embora o modelo tenha tido um desempenho excelente.
*   **Riscos:** O modelo não deve ser usado para prever em bases onde a variável `Total` não é uma medida confiável ou onde a relação entre `Total` e a classe é diferente.

**Conclusão:** Este experimento demonstra com sucesso a aplicação de um algoritmo de classificação e a capacidade de interpretar seus resultados. Ele também serve como um exemplo de como uma boa engenharia de atributos pode levar a modelos de alta acurácia e simples interpretação.
