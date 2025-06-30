<!-- # 📘 usuarios_service – API de Usuários

Microsserviço responsável por autenticação, cadastro, gerenciamento e controle de permissões de usuários.

---

## ✅ Endpoints principais

### 🔐 Login JWT
- `POST /api/usuarios/login/`

```json
{
  "email": "usuario@teste.com",
  "password": "senha123"
}
```

**Resposta:**
```json
{
  "access": "token...",
  "refresh": "token..."
}
```

---

### 👤 Ver usuário logado
- `GET /api/usuarios/me/`

**Requer token JWT no header:**
```
Authorization: Bearer <access_token>
```

---

### 🔄 Atualizar senha
- `PUT /api/usuarios/senha/`

```json
{
  "senha": "NovaSenha123"
}
```

---

### 📥 Criar usuário
- `POST /api/usuarios/usuarios/`

```json
{
  "nome": "João",
  "email": "joao@teste.com",
  "senha": "senha123",
  "tipo": "usuario",
  "setor_id": 1,
  "cargo_id": 2,
  "grupo_ids": [1, 2]
}
```

---

### 📋 Listar usuários (requer admin)
- `GET /api/usuarios/usuarios/`

Filtros disponíveis:
- `?search=joao`
- `?tipo=analista`
- `?setor_id=3&cargo_id=1`

---

### ✏️ Atualizar usuário
- `PUT /api/usuarios/usuarios/<id>/`

---

### 🗑️ Deletar usuário (soft delete)
- `DELETE /api/usuarios/usuarios/<id>/`

---

### 📦 Dados básicos de um usuário
- `GET /api/usuarios/<id>/dados_basicos/`

```json
{
  "id": 3,
  "nome": "João",
  "email": "joao@teste.com",
  "tipo": "analista",
  "setor_id": 2
}
```

---

## 🧱 Permissões

| Recurso              | Restrição                         |
|----------------------|-----------------------------------|
| `/usuarios/`         | Somente admin                     |
| `/me/`, `/senha/`    | Qualquer usuário autenticado      |
| `update/delete`      | Somente admin ou o próprio usuário | -->
