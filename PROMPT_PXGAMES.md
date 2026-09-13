# Prompt definitivo para o PXgames

Quero que você trabalhe sobre o projeto atual do PXgames e faça uma correção completa, mas NÃO recrie o site do zero.

O problema principal é o sistema de jogos.

IMPORTANTE: anteriormente o projeto conseguiu executar jogos dentro do próprio PXgames, mas depois de uma alteração feita no código o funcionamento dos jogos foi perdido. Portanto, antes de alterar qualquer coisa, ANALISE TODO O PROJETO ATUAL e identifique como o sistema de abertura dos jogos está estruturado.

Use o Preview do Replit para testar o site durante o desenvolvimento.

NÃO considere a tarefa concluída apenas porque o cartão do jogo aparece. O jogo precisa REALMENTE CARREGAR E SER JOGÁVEL DENTRO DO PXgames.

## 1. Regra principal dos jogos

Todos os jogos devem funcionar DENTRO do PXgames.

Quando o usuário clicar em um jogo:
- não deve ser redirecionado para outro site;
- não deve abrir outra aba;
- não deve sair do PXgames;
- o jogo deve aparecer dentro da área de jogo existente;
- o botão Voltar deve retornar ao catálogo;
- o iframe deve ocupar corretamente a área disponível;
- deve funcionar com mouse e teclado;
- deve permitir tela cheia quando o embed permitir.

NÃO use links comuns para páginas de jogos.

Use SOMENTE URLs de EMBED/IFRAME reais e verificáveis.

NÃO INVENTE URLs.

NÃO use uma URL da página normal de um jogo dentro de um iframe achando que ela é um embed.

## 2. Soccer Random

O primeiro jogo que precisa ser restaurado é Soccer Random.

Use como referência um embed REAL do jogo.

Uma fonte que fornece um embed do Soccer Random é:
https://www.bubbleshooter.net/game/soccer-random/

Embed:
https://www.bubbleshooter.net/embed.php?id=1502

Teste PRIMEIRO esse embed.

Existe também:
https://www.miniplay.com/embed/soccer-random

Se o primeiro não funcionar no Preview do Replit, teste o segundo.

NÃO substitua Soccer Random por outro jogo apenas porque o primeiro embed apresentou problema.

O objetivo é fazer o Soccer Random funcionar dentro do PXgames.

## 3. Não quebrar os embeds

Ao implementar os iframes:
- não coloque sandbox restritivo;
- não bloqueie scripts do iframe;
- não coloque elementos transparentes sobre o jogo;
- não capture os eventos de teclado destinados ao jogo;
- não aplique CSS que impeça o jogo de receber interação;
- não utilize JavaScript que remova ou substitua o iframe depois que ele carregar;
- não coloque lazy-loading se isso estiver causando problemas;
- use allowfullscreen quando apropriado;
- permita as funcionalidades necessárias pelo iframe.

Exemplo:

<iframe src="URL_REAL_DO_EMBED" title="Nome do jogo" frameborder="0" scrolling="no" allowfullscreen></iframe>

Adapte isso ao sistema atual do PXgames em vez de duplicar código desnecessariamente.

## 4. Teste o jogo de verdade

Depois de colocar cada jogo:
1. abra o Preview;
2. abra o catálogo;
3. clique no cartão;
4. verifique se o iframe aparece;
5. espere o jogo carregar;
6. teste a interação;
7. teste teclado/mouse quando aplicável;
8. teste o botão Voltar;
9. abra novamente;
10. confirme que não aparece tela branca ou preta causada pelo próprio código do PXgames.

Se um embed específico não funcionar, NÃO invente uma solução.

Descubra se:
- a URL está incorreta;
- o provedor bloqueia iframe;
- existe outro embed oficial do mesmo jogo;
- o código do PXgames está interferindo;
- o CSS está escondendo o iframe;
- algum JavaScript está destruindo o elemento.

Somente depois disso escolha outro embed.

## 5. Categorias

Todas as categorias existentes no catálogo precisam funcionar de verdade.

Exemplos:
- Esportes
- Tabuleiro
- Puzzle
- Arcade
- 2 Jogadores

Se existirem outras categorias no projeto atual, preserve-as.

Ao clicar em uma categoria:
- mostrar os jogos daquela categoria;
- esconder corretamente os jogos das outras categorias;
- permitir retornar para Todos;
- não recarregar o site inteiro;
- não quebrar a navegação.

## 6. Pelo menos 4 jogos por categoria

Cada categoria precisa ter pelo menos 4 jogos REAIS.

Não crie quatro cartões falsos.

Cada cartão deve possuir:
- ID;
- nome;
- categoria;
- descrição;
- thumbnail;
- URL REAL DE EMBED;
- função de abertura;
- funcionamento dentro do PXgames.

Para encontrar os jogos:

PRIORIDADE 1: fontes que forneçam explicitamente código de iframe/embed para publicação em outros sites.

PRIORIDADE 2: fontes que indiquem claramente que permitem incorporação de seus jogos.

NÃO use simplesmente uma página de jogo como se fosse um embed.

NÃO invente IDs de iframe.

NÃO coloque URLs aleatórias.

Antes de adicionar um jogo, confirme que existe um embed real.

## 7. Esportes

Crie pelo menos 4 jogos reais na categoria Esportes.

Priorize jogos como:
- Soccer Random;
- outros jogos de futebol;
- basquete;
- bilhar/sinuca;
- golfe;
- boliche;
- tênis.

Não é necessário usar exatamente esses exemplos. O requisito é que sejam jogos reais, tenham embed verificável e funcionem dentro do PXgames.

## 8. Tabuleiro

Crie pelo menos 4 jogos reais.

Exemplos de tipos:
- Xadrez;
- Damas;
- Dominó;
- Mahjong ou outro jogo de tabuleiro/puzzle apropriado.

Se determinado jogo não puder ser incorporado, não o use.

## 9. Puzzle

Crie pelo menos 4 jogos reais com embeds funcionais.

Priorize jogos leves que funcionem bem em navegador.

## 10. Arcade

Crie pelo menos 4 jogos reais com embeds funcionais.

Priorize jogos leves e apropriados para rodar em iframe.

## 11. 2 Jogadores

Crie pelo menos 4 jogos reais que tenham modo para dois jogadores ou multiplayer local, desde que o embed seja realmente funcional.

Soccer Random pode aparecer nessa categoria também, caso a estrutura de categorias permita múltiplas categorias para um mesmo jogo.

## 12. Sistema de jogos

Não crie uma função diferente e enorme para cada jogo.

Se o projeto já possui algo semelhante a GAMES, GAME_MODULES, openGame(), game-view ou game-stage, adapte o sistema existente.

Crie uma estrutura centralizada para os jogos, por exemplo:

{
  id,
  nome,
  categoria,
  descricao,
  thumbnail,
  embed
}

E faça o sistema existente abrir o embed correspondente.

## 13. Calculadora secreta

Existe uma calculadora secreta/desbloqueio no início do projeto.

Ela está com problema.

NÃO simplesmente remova essa funcionalidade.

Analise o código atual e descubra por que ela não está funcionando.

Corrija:
- entrada pelo mouse;
- entrada pelo teclado;
- código secreto existente;
- botão de confirmação;
- limpeza;
- desbloqueio;
- comportamento quando o código estiver errado;
- transição para o catálogo.

Não altere o código secreto existente sem necessidade.

## 14. Imagem do canto superior esquerdo

Troque a imagem atual do canto superior esquerdo por uma imagem relacionada a jogos/gaming.

A imagem deve:
- combinar com o PXgames;
- funcionar no Preview;
- continuar funcionando depois da hospedagem;
- não depender de um arquivo local inexistente;
- não quebrar o layout.

Se já existir uma imagem apropriada nos arquivos do projeto, pode reutilizá-la.

## 15. Não destruir o projeto existente

Preserve layout, navegação, header, catálogo, filtros, categorias, calculadora secreta, responsividade e identidade visual sempre que estiverem funcionando.

Faça alterações somente onde necessário.

## 16. Teste final obrigatório

Antes de dizer que terminou, faça uma revisão completa do projeto.

Teste:
- site abre normalmente;
- calculadora secreta funciona;
- catálogo aparece;
- categorias funcionam;
- cada categoria possui pelo menos 4 jogos;
- cartões abrem os jogos;
- jogos aparecem dentro do PXgames;
- Soccer Random funciona;
- não há redirecionamento;
- não há nova aba;
- iframes recebem interação;
- mouse funciona;
- teclado funciona quando necessário;
- tela cheia funciona quando disponível;
- botão Voltar funciona;
- é possível abrir outro jogo depois de voltar;
- não existem URLs de embed inventadas;
- não existem cartões sem jogo real;
- não existem erros JavaScript que impeçam o funcionamento;
- não existem imagens quebradas.

Se um jogo não funcionar no Preview, NÃO marque esse jogo como concluído.

Substitua-o por outro jogo cujo embed seja verificável e funcional.

O objetivo não é apenas montar uma aparência bonita.

O objetivo é entregar um PXgames FUNCIONAL, onde o usuário consiga selecionar uma categoria, escolher um jogo e realmente jogar dentro do próprio site.

No final, mostre um resumo dos jogos adicionados contendo:

NOME | CATEGORIA | FONTE DO EMBED | STATUS DO TESTE

Só considere "FUNCIONANDO" aquilo que foi realmente testado no Preview.