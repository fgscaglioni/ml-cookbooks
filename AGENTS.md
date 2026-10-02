# AGENTS.md

- Nunca editar `.ipynb` com a ferramenta `patch`: corrompe o JSON. Trocar linha por script, validando antes de escrever.
- Nunca usar `!pip` em célula de notebook; usar `%pip`, que instala no kernel.
- Instalar sempre com versão fixada (`==`).
- Nunca commitar dado, artefato de execução ou caminho absoluto de máquina (`/home/...`).
- Nunca renomear, mover nem reestruturar notebook sem corrigir as referências de texto e de caminho e o `README.md` no mesmo commit.
- Nunca commitar, dar push nem abrir PR por iniciativa própria: a entrega é o working tree.
- Commits no padrão `tipo(escopo): descrição`; markdown em português, código e prints em inglês.
- Rodar `python3 scripts/check_notebooks.py` antes de commitar; esperado `PASSOU: 0 falha(s)`.
- Ambiente local em Python 3.12; a receita está no `README.md`.
