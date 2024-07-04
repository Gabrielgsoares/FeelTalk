
# Projeto FeelTalk

[Click here](README_EN.md) for the English version of this README.

## Introdução

O FeelTalk foi criado para ajudar pessoas com limitações físicas e deficiência na fala, possibilitando que possam se comunicar com amigos, familiares e colegas de trabalho. O objetivo do projeto é combater o isolamento social e promover a interação entre as pessoas.

## Visão Geral do Código do Projeto

### Componentes Principais
- **main.py**: Ponto de entrada principal da aplicação.
- **guiHome.py**: Gerencia a interface da tela inicial.
- **guiExpressions.py**: Lida com a interface para seleção e exibição de expressões.
- **tracking.py**: Contém funcionalidades relacionadas ao rastreamento e interpretação de entradas dos usuários.

### Bibliotecas Utilizadas
- **tkinter**: Para criação da interface gráfica.
- **opencv-python**: Utilizada para processamento de imagens e funcionalidades de rastreamento.
- **numpy**: Para operações numéricas necessárias no processamento de imagens.
- **pillow**: Para manipulação de arquivos de imagem dentro da aplicação.

### Estrutura de Arquivos
```
ProjetoFeelTalk/
├── src/
│   ├── projeto_FeelTalk/
│   │   ├── assets/
│   │   │   ├── frame0/
│   │   │   ├── frame1/
│   │   │   ├── frame2/
│   │   ├── guiExpressions.py
│   │   ├── guiHome.py
│   │   ├── main.py
│   │   ├── tracking.py
|   |   ├── run_both.py
├── README_PT.md
├── README_EN.md
└── requirements.txt
```

## Como Executar

Para executar o código, siga estes passos:

1. Certifique-se de que o Python está instalado em sua máquina.
2. Instale as bibliotecas necessárias utilizando o comando:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script principal para iniciar a aplicação:
   ```bash
   python src/projeto_FeelTalk/run_both.py
   ```

---
