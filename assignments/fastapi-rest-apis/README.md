# 📘 Tarefa: Building REST APIs with FastAPI

## 🎯 Objective

Nesta atividade, você vai construir uma API REST usando FastAPI, praticando criação de rotas, operações CRUD, validação de dados com Pydantic e testes de endpoints no Swagger UI.

## 📝 Tasks

### 🛠️ Criar o Primeiro Endpoint

#### Descrição
Configure um projeto FastAPI com endpoint de saúde e endpoint de boas-vindas para validar que o servidor está funcionando corretamente.

#### Requisitos
O programa completo deve:

- Criar um app FastAPI em um arquivo starter-code.py
- Implementar GET /health retornando status da aplicação
- Implementar GET / retornando mensagem de boas-vindas em JSON
- Permitir execução local com comando uvicorn starter-code:app --reload

### 🛠️ Implementar CRUD de Itens

#### Descrição
Implemente uma API de tarefas (to-do) com armazenamento em memória para criar, listar, buscar por ID, atualizar e remover itens.

#### Requisitos
O programa completo deve:

- Definir modelo Pydantic para entrada de dados (exemplo: title, done)
- Implementar endpoints: POST /items, GET /items, GET /items/{item_id}, PUT /items/{item_id}, DELETE /items/{item_id}
- Retornar códigos HTTP adequados (201, 200, 404)
- Manter dados em uma estrutura em memória (lista ou dicionário)

### 🛠️ Validar Dados e Documentar API

#### Descrição
Melhore sua API com validações e confirme o comportamento usando a documentação interativa gerada automaticamente pelo FastAPI.

#### Requisitos
O programa completo deve:

- Adicionar validações de campos no modelo (por exemplo, título obrigatório e tamanho mínimo)
- Tratar erros com HTTPException para recursos não encontrados
- Testar todos os endpoints no Swagger UI em /docs
- Incluir pelo menos um exemplo de payload válido e um inválido durante os testes
