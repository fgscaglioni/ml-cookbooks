#!/usr/bin/env python3
"""Portao dos notebooks do ml-cookbooks. Somente leitura.

    python3 scripts/check_notebooks.py    # da raiz do repo
    exit 0 = tudo ok; exit 1 = regra violada

Checa: JSON valido e nbformat 4, estrutura da celula (id presente, e outputs e
execution_count em toda celula de codigo), schema nbformat via nbformat.validate quando a
lib esta instalada, nenhum output de erro, run completo (execution_count 1..N), toda
referencia .ipynb resolve para arquivo existente, todo install de tabpfn/autogluon com
versao fixada e .gitignore cobrindo dado e artefato gerado.
"""
import json
import pathlib
import re
import subprocess
import sys

try:
    import nbformat
except ImportError:  # o check estrutural continua valendo sem a lib
    nbformat = None

REPO = pathlib.Path(__file__).resolve().parent.parent
NBDIR = REPO / "notebooks"
IGNORADOS = ("data/exemplo.csv", "artifacts_tabpfn/x.csv", "artifacts_mitra/x.csv",
             "splits_fingerprint.json", "ag_warmup_clf/x", "ag_mitra_reg/x",
             "modelo_mitra_classificacao/x")
LINHA_INSTALL = re.compile(r"install", re.I)

falhas, avisos = [], []


def checa(ok, msg):
    print(("  ok    " if ok else "  FALHA ") + msg)
    if not ok:
        falhas.append(msg)


def avisa(msg):
    print("  aviso " + msg)
    avisos.append(msg)


notebooks = sorted(NBDIR.rglob("*.ipynb"))
checa(bool(notebooks), f"existe notebook em {NBDIR.relative_to(REPO)}/")

for nb_path in notebooks:
    rel = nb_path.relative_to(REPO)
    texto = nb_path.read_text(encoding="utf-8")
    try:
        nb = json.loads(texto)
    except json.JSONDecodeError as e:
        checa(False, f"{rel}: JSON invalido ({e})")
        continue

    checa(nb.get("nbformat") == 4, f"{rel}: nbformat 4")
    faltando = [c for c in nb.get("cells", [])
                if "id" not in c
                or (c.get("cell_type") == "code"
                    and ("outputs" not in c or "execution_count" not in c))]
    checa(not faltando,
          f"{rel}: celula com id, e celula de codigo com outputs e execution_count"
          + (f" (faltam em {len(faltando)})" if faltando else ""))
    if nbformat is None:
        avisa(f"{rel}: nbformat nao instalado, schema nao conferido (pip install nbformat)")
    else:
        try:
            nbformat.validate(nbformat.read(str(nb_path), as_version=4))
            checa(True, f"{rel}: schema nbformat valido")
        except Exception as e:
            checa(False, f"{rel}: schema nbformat invalido -> {getattr(e, 'message', e)}")

    codigo = [c for c in nb["cells"] if c["cell_type"] == "code"]
    fontes = "\n".join("".join(c["source"]) for c in nb["cells"])

    checa(not [o for c in codigo for o in c.get("outputs", []) if o.get("output_type") == "error"],
          f"{rel}: nenhum output de erro")
    contagens = [c.get("execution_count") for c in codigo]
    rodadas = [n for n in contagens if n is not None]
    if rodadas:
        checa(rodadas == list(range(1, len(rodadas) + 1)),
              f"{rel}: run completo, execution_count 1..{len(rodadas)}")
        if len(rodadas) != len(contagens):
            avisa(f"{rel}: {len(contagens) - len(rodadas)} celula(s) sem execution_count (re-run parcial)")

    for alvo in sorted(set(re.findall(r"[A-Za-z0-9_./-]+\.ipynb", fontes))):
        checa((nb_path.parent / alvo).resolve().exists(),
              f"{rel}: cita `{alvo}` e o arquivo existe")

    for linha in fontes.splitlines():
        if "pip" in linha and LINHA_INSTALL.search(linha) and re.search(r"tabpfn|autogluon", linha, re.I):
            checa("==" in linha, f"{rel}: install com versao fixada -> {linha.strip()[:70]}")
        if (achado := re.search(r"ensure\(\s*[\"']([^\"']+)[\"']", linha)):
            checa("==" in achado.group(1), f"{rel}: ensure com versao fixada -> {achado.group(1)}")

    if any(re.search(r"/home/[a-z0-9_]+/", "".join(o.get("text", [])) + json.dumps(o.get("data", {}), ensure_ascii=False))
           for c in codigo for o in c.get("outputs", [])):
        avisa(f"{rel}: output com caminho absoluto de maquina (nao pode ir para repo publico)")

if (REPO / ".git").exists():
    for alvo in IGNORADOS:
        checa(subprocess.run(["git", "check-ignore", "-q", alvo], cwd=REPO).returncode == 0,
              f".gitignore cobre {alvo}")
    for nb_path in notebooks:
        checa(subprocess.run(["git", "check-ignore", "-q", str(nb_path.relative_to(REPO))], cwd=REPO).returncode != 0,
              f"{nb_path.relative_to(REPO)} versionavel")

print()
print(f"{'PASSOU' if not falhas else 'FALHOU'}: {len(falhas)} falha(s), {len(avisos)} aviso(s)")
sys.exit(1 if falhas else 0)
