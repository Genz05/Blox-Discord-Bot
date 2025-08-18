
Sobre o Projeto

Este é um bot para Discord criado em Python utilizando a biblioteca discord.py. Sua principal função é fornecer informações sobre o valor de frutas do jogo Blox Fruits, permitindo aos usuários consultar seus preços na loja e em trades, além de comparar valores entre diferentes frutas.

Funcionalidades
!list ou /list: Lista todas as frutas disponíveis no banco de dados.

!valor <fruta> ou /valor <fruta>: Exibe o valor de uma fruta específica na loja e em trades.

!comparar <fruta1> <fruta2> ou /comparar <fruta1> <fruta2>: Compara o valor de duas frutas para saber qual vale mais.

omo Começar
Siga estas instruções para configurar e rodar o bot localmente.

Pré-requisitos
Certifique-se de ter o Python 3.8 ou superior e o pip instalados na sua máquina.

Instalação
Clone este repositório:

Bash

git clone https://www.dio.me/articles/enviando-seu-projeto-para-o-github
cd [pasta-do-seu-projeto]
Instale as dependências necessárias:

Bash

pip install -r requirements.txt
Configuração
Vá até o Portal do Desenvolvedor do Discord e crie uma nova aplicação para o seu bot.

Na aba "Bot", copie o token do seu bot.

Crie um arquivo .env na pasta do projeto e adicione a seguinte linha, substituindo o placeholder pelo seu token:

DISCORD_TOKEN=SEU_TOKEN_AQUI
Certifique-se de habilitar as permissões "MESSAGE CONTENT INTENT", "SERVER MEMBERS INTENT" e "PRESENCE INTENT" na aba "Bot" no Portal do Desenvolvedor.

Execução
Para iniciar o bot, basta rodar o seguinte comando no terminal:

Bash

python main.py

Contribuição
Contribuições são bem-vindas! Se você tiver alguma ideia ou encontrar um bug, sinta-se à vontade para abrir uma issue ou enviar um pull request.

