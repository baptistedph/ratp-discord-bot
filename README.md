# Bot Discord RATP

Obtenez par de simples commandes les horaires, les stations et le traffic à propos de vos lignes.

### Lancer le bot

#### Windows

```sh
pip install -r requirements.txt
python Client.py
```

#### MacOS

```sh
pip install -r requirements.txt
python3 Client.py
```

### Commandes

- `!commandes` - Liste toutes les commandes.
- `!lignes [metros|rers]` - Liste toutes les lignes de métro ou de RER.
- `!stations [metros|rers] [<line>]` - Liste toutes les stations d'une ligne.
- `!traffic [metros|rers] [<line>]` - Donne les informations à propos du traffic d'une ligne.
- `!prochains [metros|rers] [<line>] [<station>] [aller|retour|aller-retour]` - Liste les prochains passages d'un train.

### Equipe

- [Baptiste DAUPHOUY](https://github.com/baptistedph)
- [Théo DUVAL](https://github.com/The0Duval)
