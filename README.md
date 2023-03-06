# RuokaApp

FINNISH
Sovelluksen avulla käyttäjien on mahdollista pitää kirjaa syöpöttelyistään ja juopotteluistaan. Sovellusta on mahdollista käyttää usean rekisteröityneen käyttäjän, joilla kaikilla on oma yksityinen profiilinsa sisältäen mm. ruokailuhistorian.

Ohjelmisto on luotu Helsingin Yliopiston Ohjelmistotekniikka -kurssiin liittyväksi harjoitustyökseni.

ENGLISH
With ease of RuokaApp users can bookkeep of personal intake of food and beverages. App can be used by a registered user. Registered user have own private profile including history.


## Python version
FINNISH
Sovelluksen toiminta on testattu ...

ENGLISH
Software is tested with python version ...


## Documentation

- User manual: (./documentation/user_manual.md)
- Software Requirements Specification: (./documentation/srs.md)
- Architectural Description: (./documentation/architecture.md)
- Testing: (./documentation/testing.md)
- Working Time Accounting: (./documentation/work_hours_book.md)
- Changelog: (./documentation/changelog.md)


## Install
FINNISH
i. Asenna riippuvuudet:

```bash
poetry install
```

ii. Suorita alustustoimenpiteet:

```bash
poetry run invoke build
```

iii. Käynnistä sovellus:

```bash
poetry run invoke start
```


## Command line functions

### Run app

FINNISH
Ohjelman suoritus:

```bash
poetry run invoke start
```

### Testing

FINNISH
Suorita testit:

```bash
poetry run invoke test
```


### Test coverage

FINNISH
Testikattavuusraportti:

```bash
poetry run invoke coverage-report
```

Löydät raportin kansiosta _htmlcov_.


### Pylint

FINNISH
[.pylintrc](./.pylintrc) määritykset sisältävä tarkistus:

```bash
poetry run invoke lint
```


