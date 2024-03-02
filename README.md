# API Checker Bot

O `api_checker_bot` é um bot do Discord que verifica periodicamente a api Carmak, realiza o login e busca a lista de tarefas do usuário definido e notifica no canal do discord sobre o status das solicitações.

O proncipal objetivo é verificar a disponibilidade a api.


## Funcionalidades

- Verifica periodicamente a api Carmak
- Realiza solicitações à API com base em configurações definidas
- Notifica sobre o status das solicitações por meio do Discord

## Estrutura de pastas

    api_checker_bot/
    ├── app.py
    ├── config.py
    ├── .env.sample
    ├── .gitignore
    └── README.md


## Como Usar

1. **Configuração do Ambiente**

   - Crie um novo arquivo baseado em `.env.sample` chamado `.env`
   - Preencha as variáveis de ambiente no arquivo `.env` com suas próprias configurações:
     - `API_BASE_URL`: URL base da API a ser verificada
     - `USER_EMAIL`: E-mail de login na API
     - `USER_PASSWORD`: Senha de login na API
     - `DISCORD_TOKEN`: Token do bot do Discord
     - `DISCORD_CHANNEL`: ID do canal do Discord para enviar notificações
     - `CALL_INTERVAL_MINUTES`: Intervalo entre as chamadas em minutos (opcional, padrão: 1 minuto)
     - `REQUEST_QUANTITIES`: Quantidade de solicitações a serem feitas em cada chamada (opcional, padrão: 100 solicitações)

2. **Criação do ambiente virtual**

    ```bash
        python -m venv bot_env
        source bot_env/bin/activate  # Linux / MacOS
        bot_env\Scripts\activate  # Windows
    ```

3. **Instalação das Dependências**

    ```bash
        pip install -r requirements.txt
    ````

4. **Executando o Bot**
    ```bash
       python app.py
    ````

5. **Contribuição**

    Para contribuir com este projeto, siga as diretrizes de contribuição abaixo:

    - Faça um fork do repositório
    - Crie uma branch para sua nova funcionalidade (git checkout -b feature/nova-funcionalidade)
    - Faça commit de suas alterações (git commit -am 'Adiciona nova funcionalidade')
    - Faça push para a branch (git push origin feature/nova-funcionalidade)
    - Crie um novo Pull Request
