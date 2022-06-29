# CHANGELOG

Arquivo para documentação das principais alterações sofridas por este conjunto de dados.

O histórico completo das alterações está disponível [aqui](https://github.com/dados-mg/termos-parceria-contratos-gestao/commits/master).

## versão 0.1.0 - Junho/2021

- Representação das informações do conjunto de dados em 4 arquivos, com identificação única de cada termo de parceria e/ou contrato de gestão realizada pela coluna `ID_INSTRUMENTO`, presente em todos os arquivos.

- Redistribuição das informações constantes da versão anterior deste conjunto de dados entre os arquivos `termos-parceria-contratos-gestao` e `repasses`, conforme quadro abaixo:

    - Item redistribuído *sem* alteração na nomenclatura:

        - TIPO_INSTRUMENTO
        - NUM_TERMO_CONTRATO
        - ORGAO_ESTATAL_SIGLA
        - ENTIDADE_PARCEIRA_NOME
        - ENTIDADE_PARCEIRA_SIGLA
        - ENTIDADE_PARCEIRA_CNPJ
        - OBJETO
        - SITUACAO
        - DATA_INICIO_VIGENCIA
        - DATA_FIM_VIGENCIA

    - Item redistribuído *com* alteração na nomenclatura / de-para:

        - CODIGO_ORGAO_ESTATAL: ORGAO_ESTATAL_CODIGO
        - NOME_ORGAO_ESTATAL: ORGAO_ESTATAL_NOME

- Redistribuição das informações constantes da versão anterior deste conjunto de dados para o arquivo repasses, sem alteração de nomenclatura dos itens, conforme listagem abaixo:

    - Item redistribuído *sem* alteração na nomenclatura:

        - ANO 
        - REPASSE_PREVISTO 
        - REPASSE_REALIZADO

-  Inserção, no arquivo `termos-parceria-contratos-gestao`, das colunas:
	- `URL_INTEGRA_TERMO_CONTRATO`: Link para acessar o Contrato de Gestão ou Termo de Parceria;
	- `URL_DOCUMENTOS_TERMO_CONTRATO`: Link para acessar a página principal contendo os documentos do Contrato de Gestão ou Termo de Parceria.

- Inserção, no arquivo `relatorios`, de informações sobre os relatórios das comissões de avaliação, os relatórios de monitoramento e os relatórios gerenciais.

- Inserção, no arquivo `aditivos`, de informações sobre os termos termos aditivos celebrados.

## versão 0.0.1 - Novembro/2019

- Publicação da versão inicial do conjunto de dados