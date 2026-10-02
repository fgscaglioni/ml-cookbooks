# AGENTS.md

Regras para agentes de código neste repositório. O `README.md` é a narrativa, para humanos: não duplicar aqui.

## O que é

Coleção de notebooks didáticos de ML tabular: cada um autocontido, da carga de dados à avaliação de baseline. Não há código de produção nem pacote instalável — o entregável é o notebook.

- `notebooks/<paradigma>/` — os notebooks. Em `foundational/`, o par didático (`01_tabpfn.ipynb`, `02_mitra.ipynb`) e, em `foundational/cookbooks/`, o par de protocolo completo.
- `data/`, `artifacts_*/`, `splits_fingerprint.json` e os diretórios de modelo do AutoGluon ficam **fora do versionamento**: dado baixado e saída de execução. O `.gitignore` cobre todos.
- `scripts/check_notebooks.py` — o portão do repositório.

## Verificar

```bash
python3 scripts/check_notebooks.py     # da raiz do repo
```

Esperado: `PASSOU: 0 falha(s)` e exit 0. Aviso não bloqueia, falha bloqueia.

Rodar um notebook: a primeira célula de código instala o que falta, com versão fixada; ambiente local no `README.md`. Exige Python 3.12: em 3.14 o pip resolve o beta `autogluon-tabular 0.0.16b20210206` e quebra no scipy. No Colab, GPU para o Mitra.

Os cookbooks são um par ordenado: o `01_*` escreve `splits_fingerprint.json` e o `02_*` confere a igualdade das partições, falhando se divergirem. Rodar o 01 antes do 02.

## Convenções

- Markdown em **português** (o leitor é aluno brasileiro). Identificadores, comentários, docstrings e mensagens de `print` em **inglês**. Nomes de coluna do dataset ficam como estão.
- Commit no padrão `tipo(escopo): descrição`, em português.
- Não commitar, não dar push e não abrir PR por iniciativa própria: entrega completa é o working tree com as mudanças. `push` para `main` publica.
- Toda instalação dentro de notebook leva versão fixada (`==`). Trocar versão é mudança deliberada, com o novo valor no mesmo commit.

## Proibido

- Usar a ferramenta `patch` em `.ipynb`: o `source` é array JSON escapado e o arquivo corrompe. Editar por script — `nbformat` ou substituição literal no texto do arquivo; `json.dumps(nb, indent=1, ensure_ascii=False) + "\n"` reproduz o arquivo byte a byte, mantendo o diff mínimo.
- Repor ou "consertar" outputs: os notebooks são versionados **sem outputs** (sem log de instalação, sem caminho de máquina, sem resultado de run antigo). Não reexecutar para preencher.
- Renomear ou mover notebook sem corrigir as referências de texto **e** de caminho no mesmo commit, junto com o `README.md`, e sem rodar o portão.
- Commitar dado, artefato de execução ou output com caminho absoluto de máquina (`/home/<usuário>/...`): o repositório é público.
- Instalar sem versão fixada.
- Usar `!pip install` em célula de notebook: o `!` chama o pip do PATH, não o do kernel, e num venv criado com `uv venv` (sem pip) falha com `externally-managed-environment` no pip do sistema. Célula de instalação usa `%pip install`; código Python usa `sys.executable -m pip install`.
- Repetir no `AGENTS.md` o que já está no `README.md`.

## Manter

Mudou estrutura, comando, caminho ou convenção: atualizar este arquivo no **mesmo commit** da mudança.
