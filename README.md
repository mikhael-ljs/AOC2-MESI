# AOC2-MESI
Trabalho Prático de Arquitetura e Organização de Computadores 2


Requisitos:
  1. Cada grupo deverá desenvolver um simulador de protocolo de coerência de cache.
  2. A quantidade de núcleos (cores) deve ser ajustável para 4, 8 ou 16.
  3. Em cada núcleo deverá ser simulado um nível de cache diretamente mapeada com
  os seguintes parâmetros ajustáveis:
  a. número de entradas: 16, 32 ou 64;
  b. tamanho de linha: 64 ou 128 bytes.
  4. Obs: todos os endereços e palavras são de 4 bytes.
   
Testes:
  1. Os arquivos core4.txt, core8.txt e core16.txt contêm sequências de referências à
  memória, considerando 4, 8 e 16 núcleos respectivamente.
  2. Cada linha contém o número do core que fez a requisição, o tipo de requisição (R =
  leitura, W = escrita) e o endereço.
  3. O programa deve ler cada um dos arquivos e simular o funcionamento do protocolo
  para cada quantidade de núcleos e para cada configuração de cache (considerar
  caches idênticas para todos os núcleos). Um relatório com as seguintes informações,
  para cada operação de leitura/escrita, deverá ser gerado:
  a. Indicação de cache hit ou cache miss;
  b. A linha da cache e o valor da tag;
  c. A transição de processador;
  d. As transições de barramento nas outras caches, se houver;
  e. Indicação de operação de write-back, se houver;
  f. Indicação de envio direto do valor da linha (cache para cache), se houver e
  for permitido pelo protocolo.
  4. O relatório deverá conter ainda as seguintes informações:
  a. Taxa de erro das caches;
  b. Número total de operações de write-back;
  c. Número total de invalidações forçadas.
