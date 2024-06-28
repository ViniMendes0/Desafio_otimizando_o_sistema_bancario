
* Objetivo geral


1- Separar as funçoes existentes de saque, deposito e extrato em funçoes. Criar
duas novas funçoes: cadastrar usuario (cliente) e cadastar conta bancaria.


* Desafio

Precisamos deixar o nosso codigo mais modularizado, para isso vamos criar funçoes 
para as operaçoes existentes: sacar, depositar e visualiazar extrato. Alem disso
para a versão 2 do nosso sistema precisamos criar duas novas funçoes: criar usuario
(cliente do banco) e criar conta corrente (vincular com usuario).


* Separação em funçoes 

Devemos criar funçoes para todas as operaçoes do sistema. Para exercitar tudo
o que aprendemos neste modulo, cada função vai ter uma regra na passagem de 
argumentos. O retorno e a forma como serão chamados, pode ser definida por vc
da forma que achar melhor.



* Saque 

A função saque deve receber os argumentos apenas por nome (keyword only).
Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, 
limite_saques. Sugestão de retorno saldo e extrato.


* Deposito

A função deposito deve receber os argumentos apenas por posição (positional only).
Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.


* Extrato

A função extrato deve receber os arguementos por posição e nome (positional 
only e keyword only). Arguementos posicionais: saldo, argumentos nomeados:extrato.


* Novas funçoes 

Precisamos criar duas novas funçoes: criar usuario e criar conta corrente.
Fique a vontade para adicionar mais funçoes, exemplo: listar contas.


* Criar usuario (cliente)

O programa deve armazenar os usuarios em uma lista, um usuario é composto
por: nome, data de nascimentos, cpf e endereço. O endereço é uma string com
o formato logradouro, nro - bairro - cidade/sigla estado. Deve ser armazenado 
somente os numeros do cpf. Não podemos cadastrar 2 usuarios com o mesmo cpf.



* Criar conta corrente

O programa deve armazenar contas em uma lista, uma conta é composta por: 
agencia, número da conta e usuario. O numero da conta é sequencial, iniciando 
em 1. O numero da agencia é fixo "0001". O usaurio pode ter mais de uma conta 
, mas uma conta pertence a somente um usuario.


* Dica


Para vincular um usaurio a uma, filtre a lista de usuario buscando o numero do cpf
informado para cada usuario da lista.



