# Testes -  APIs Públicas com Pytest

Este projeto contém testes de integração para várias APIs públicas, 
usando "pytest" para automatizar e verificar o funcionamento correto.

### APIs Utilizadas
1. Rick and Morty: Informações sobre personagens da série Rick and Morty.
2. Pokémon: Dados sobre Pokémons, como habilidades e características.
3. Piadas Aleatórias: Piadas em várias categorias.
4. Perfis de Usuários Aleatórios: Simulação de banco de dados de usuários.
5. Fatos sobre Gatos: Fatos aleatórios sobre gatos.

# Descrição dos Testes

- Testes de Sucesso: Verificam se as requisições retornam o status code 200 ou o esperado.
- Testes de Erro: Simulam cenários de erro, como requisições inválidas ou dados incorretos.
- Verificação de Dados: Validam se as respostas contêm as informações esperadas, como chaves específicas no JSON ou valores correspondentes.

# Dependências:
pip install -r requirements.txt

# requirements.txt

- pytest
- requests

 