# 🏥 Sistema de Gerenciamento Médico

## 📌 Descrição

Este projeto implementa um sistema de gerenciamento de consultas médicas em Python. O sistema organiza os atendimentos de pacientes com base em dois critérios: **prioridade** (normal ou urgente) e **idade** (quanto mais velho, maior prioridade dentro da mesma categoria). Ele é ideal para clínicas, postos de saúde ou qualquer ambiente onde o controle e a ordem de atendimentos precisam seguir critérios objetivos.

---

## 📁 Estrutura de Pastas

```
/entities
├── /patients
│   ├── Age.py
│   ├── Priority.py
│   └── Patient.py
├── /medical
│   ├── MedicalAppointment.py
│   └── MedicalManagementSystem.py

/services
└── MedicalManagementSystemService.py

main.py
README.md
```

---

## ▶️ Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Acesse a pasta do projeto:
```bash
cd seu-repositorio
```

3. Execute o código:
```bash
python index.py
```

4. Informe o número de pacientes e os dados no formato:
```
Nome, Idade, Prioridade
```
Exemplo:
```
3
Maria, 34, urgente
João, 65, normal
Pedro, 80, urgente
```

---

## ✅ Funcionalidades

- Cadastro de pacientes com nome e idade
- Registro de prioridade médica (normal ou urgente)
- Agendamento de consultas com ordenação automática
- Reordenação baseada em critérios: prioridade e idade
- Exibição da fila de atendimento ordenada

---

## 📋 Regras de Negócio

- Prioridades válidas: `normal`, `urgente`
- Idade deve estar entre 0 e 120 anos
- Pacientes com prioridade `urgente` têm preferência sobre `normal`
- Em caso de mesma prioridade, o paciente mais velho é atendido primeiro
- Não permite agendamentos duplicados (mesmo paciente, mesma prioridade)

---

## 👤 Autor

Bruno Batista

- 📧 Email: brunojbatista@hotmail.com  
- 📱 Telefone: +55 (81) 9 9929-0698 — WhatsApp / Telegram  
- 🔗 Linkedin: [https://www.linkedin.com/in/bjnb](https://www.linkedin.com/in/bjnb)
