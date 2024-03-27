# Poetry commands

### Step:
1. Per creare un nuovo progetto Poetry si utilizza il comando `new`  seguito dal nome:
```shell
poetry new poetry_exercise
```
che crea le cartelle e i file: 

```shell
poetry_exercise
├── pyproject.toml
├── README.md
├── poetry_exercise
│   └── __init__.py
└── tests
    └── __init__.py
```
In particolare il file  `pyproject.toml` viene usato per la gestione delle dipendenze

2. Per aggiungere una dipendenza si può usare invece:
```shell
poetry add pandas
```
che va ad aggiornare il file `pyproject.toml`.

Il comando aggiunge anche il file  `poetry.lock` che contiene l'elenco di tutte le dipendenze e delle relative versioni.