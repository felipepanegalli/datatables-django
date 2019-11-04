# datatables-django
Integração do Datatables com o Django 2.x

#### Gerar tabelas
- Esse é o primeiro passo para fazer funcionar o banco. Basta digitar:
  - python manager.py makemigrations
  - python manager.py migrate
- Após isso popular a tabela com os comandos abaixo

#### Gerar registros para tabela
- Para gerar os registros é muito simples, basta ir em:
  - (endereco):(porta)/faker/quantidade_de_registros(valor inteiro)
- Dependendo da quantidade, é possivel que demore, ao finalizar ele retornará para a página inicial

#### Rotas:
- As rotas estão dividido nos seguintes end-points:
  - admin/ = Rota padrão admin
  - faker/<int:id> = Rota para gerar quantidade x de registros na tabela
  - datatables/ = Rota para o exemplo do datatables
  - / = Rota para o exemplo sem o datatables
  - v1/users/ = Rota da api de usuários (só possui a listagem baseada no faker, não possue o CRUD completo)

#### Agradecimentos
- Henrique Bastos pela disponibilidade.
- Regis Silva, por dar algumas dicas onde pude progredir e finalizar o exemplo.