# Sistema de Gerenciamento de Garantias Ford

Todo o código desenvolvido aqui faz parte de um teste para uso de FastAPI e não representa a FORD em qualquer contexto, é usado expressamente para nivelamento.
Este é um sistema de gerenciamento de garantias desenvolvido para a Ford, utilizando FastAPI, SQLAlchemy e PostgreSQL.

## Requisitos

- Python 3.8+
- PostgreSQL 12+
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Androthorn/ford-warranty-system-test-.git
cd ford-warranty-system
```

2. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
```env
POSTGRES_SERVER=localhost
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_DB=ford_db
SECRET_KEY=sua_chave_secreta
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Crie o banco de dados:
```sql
CREATE DATABASE ford_db;
```

6. Execute as migrações:
```bash
alembic upgrade head
```

## Executando a Aplicação

Para iniciar o servidor de desenvolvimento:
```bash
uvicorn app.main:app --reload
```

A aplicação estará disponível em:
- API: http://localhost:8000
- Documentação Swagger: http://localhost:8000/docs
- Documentação ReDoc: http://localhost:8000/redoc

## Testes

Para executar os testes:
```bash
pytest
```

Para executar os testes com cobertura:
```bash
pytest --cov=app tests/
```

## Estrutura do Projeto

```
app/
├── api/
│   └── v1/
│       └── endpoints/
│           ├── auth.py
│           ├── locations.py
│           ├── suppliers.py
│           ├── vehicles.py
│           ├── parts.py
│           ├── purchases.py
│           ├── warranties.py
│           ├── warranty_parts.py
│           └── reports.py
├── core/
│   ├── config.py
│   └── security.py
├── crud/
│   ├── base.py
│   ├── user.py
│   ├── location.py
│   ├── supplier.py
│   ├── vehicle.py
│   ├── part.py
│   ├── purchase.py
│   ├── warranty.py
│   └── warranty_part.py
├── db/
│   ├── base.py
│   ├── session.py
│   └── migrations/
├── models/
│   ├── user.py
│   ├── location.py
│   ├── supplier.py
│   ├── vehicle.py
│   ├── part.py
│   ├── purchase.py
│   ├── warranty.py
│   └── warranty_part.py
└── schemas/
    ├── base.py
    ├── user.py
    ├── location.py
    ├── supplier.py
    ├── vehicle.py
    ├── part.py
    ├── purchase.py
    ├── warranty.py
    └── warranty_part.py
```

## Funcionalidades

### Autenticação
- Registro de usuário
- Login com JWT
- Proteção de rotas

### Gerenciamento de Localizações
- CRUD de localizações
- Busca por mercado
- Busca por país

### Gerenciamento de Fornecedores
- CRUD de fornecedores
- Busca por localização
- Busca por nome

### Gerenciamento de Veículos
- CRUD de veículos
- Busca por modelo
- Busca por ano
- Busca por propulsão

### Gerenciamento de Peças
- CRUD de peças
- Busca por fornecedor
- Busca por nome

### Gerenciamento de Compras
- CRUD de compras
- Busca por tipo
- Busca por peça
- Busca por intervalo de datas

### Gerenciamento de Garantias
- CRUD de garantias
- Busca por veículo
- Busca por peça
- Busca por localização
- Busca por tipo de falha
- Busca por intervalo de datas

### Gerenciamento de Peças de Garantia
- CRUD de peças de garantia
- Busca por garantia
- Busca por peça
- Busca por fornecedor

### Relatórios
- Resumo de garantias
- Custos de garantias
- Tipos de falhas
- Resumo de peças

## Validações de Negócio

### Garantias
- Data de resolução deve ser posterior à data de falha
- Status deve ser um dos valores válidos: pending, in_progress, resolved, cancelled

### Peças de Garantia
- Quantidade deve ser maior que zero
- Preço unitário deve ser maior que zero
- Preço total deve ser igual a quantidade * preço unitário

## Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes. 
