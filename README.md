# FofocaLocal 🗣️

Uma plataforma Django para compartilhamento de fofocas e rumores locais onde usuários podem compartilhar e votar em notícias, rumores e histórias dos bairros de São José dos Campos.

## 📋 Sobre

FofocaLocal é uma plataforma movida pela comunidade que permite aos usuários:
- Compartilhar fofocas, rumores e notícias locais
- Votar se as histórias são verdadeiras ("Confirmo") ou falsas ("Mentira")
- Categorizar histórias por tipo (Comércio, Relacionamento, Obra, Bizarro, Outro)
- Filtrar histórias por áreas de bairros
- Registrar e gerenciar contas de usuário

## 🚀 Funcionalidades

- **Compartilhamento de Histórias**: Criar e compartilhar histórias locais com títulos, descrições e categorias
- **Sistema de Votação**: Votar se as histórias são verdadeiras ou falsas
- **Sistema de Categorias**: Histórias organizadas por tipo (Comércio, Relacionamento, Obra, Bizarro, Outro)
- **Autenticação de Usuários**: Cadastro, login e logout
- **Design Responsivo**: Funciona em desktop e dispositivos móveis

## 🛠️ Stack Tecnológico

- **Backend**: Django 5.2
- **Banco de Dados**: SQLite (desenvolvimento)
- **Frontend**: HTML, CSS, Bootstrap
- **Autenticação**: Sistema de autenticação nativo do Django
- **Formulários**: Django Forms com widget tweaks

## 📦 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (instalador de pacotes Python)

### Instruções de Configuração

1. **Clone o repositório**
   ```bash
   git clone <url-do-repositório>
   cd fofocalocal
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações do banco de dados**
   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Execute o servidor de desenvolvimento**
   ```bash
   python manage.py runserver
   ```

7. **Acesse a aplicação**
   Abra seu navegador e vá para `http://127.0.0.1:8000/`

## 🏗️ Estrutura do Projeto

```
fofocalocal/
├── fofocalocal/         # Configurações principais do Django
│   ├── settings.py      # Configurações do Django
│   ├── urls.py          # Configuração principal de URLs
│   └── wsgi.py          # Configuração WSGI
├── fofocas/             # Aplicação principal
│   ├── models.py        # Modelos do banco de dados
│   ├── views.py         # Funções de visualização
│   ├── forms.py         # Definições de formulários
│   ├── urls.py          # Roteamento de URLs da aplicação
│   └── templates/       # Templates HTML
├── templates/           # Templates globais
├── manage.py            # Script de gerenciamento do Django
└── requirements.txt     # Dependências Python
```

## 🗄️ Modelos do Banco de Dados

### Fofoca (História)
- `titulo`: Título da história
- `descricao`: Descrição da história
- `bairro`: Bairro (Centro, Aquarius, Satélite, etc.)
- `categoria`: Categoria da história (Comércio, Relacionamento, Obra, Bizarro, Outro)
- `votos_confirmo`: Número de votos "verdadeiro"
- `votos_mentira`: Número de votos "falso"
- `criado_em`: Timestamp de criação
- `autor`: Usuário que criou a história

## 🎯 Como Usar

### Para Usuários

1. **Registrar/Entrar**: Crie uma conta ou faça login para acessar todas as funcionalidades
2. **Navegar pelas Histórias**: Veja todas as histórias compartilhadas na página principal
3. **Compartilhar Histórias**: Clique em "Nova Fofoca" para compartilhar sua própria história
4. **Votar**: Use os botões de votação para indicar se uma história é verdadeira ou falsa


## 🤝 Como Contribuir

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

---

**📝 Nota**: Este é um projeto de demonstração criado para a comunidade brasileira. Foi desenvolvido como uma demo para mostrar funcionalidades básicas do Django e não é destinado para uso em produção.

