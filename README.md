
# Altitudo

Python package to find the elevation / altitude at a given geo coordinate.

[![](https://img.shields.io/pypi/v/altitudo.svg)](https://pypi.python.org/pypi/altitudo) 
[![](https://travis-ci.com/milesgranger/altitudo.svg?branch=master)](https://travis-ci.com/milesgranger/altitudo)
[![](https://readthedocs.org/projects/altitudo/badge/?version=latest)](https://altitudo.readthedocs.io/en/latest/?badge=latest)
[![](https://pyup.io/repos/github/milesgranger/altitudo/shield.svg)](https://pyup.io/repos/github/milesgranger/altitudo/)


# PLEASE NOTE:

### This package is backed by a [service](https://elevation-api.io) which costs _real_ money. In order to keep your application running smoothly, consider making a donation [via DonorBox here](https://donorbox.org/elevation-api)

---

## Usage:

### Via Python:
```python
>>> from altitudo import altitudo
>>> altitudo(lat=39.90974, lon=-106.17188)  # Returns meters by default
... 2624.0

>>> # Request more than a single coordinate
>>> altitudo(lat=[39.90974, 62.52417], lon=[-106.17188, 10.02487])
... [{"lat": 39.90974, "lon": -106.17188, "elevation": 2624.0},{"lat": 62.52417, "lon": 10.02487, "elevation": 1111.0}]
```

### Via CLI
```
altitudo -- 39.90974 -106.17188
2624.0
```

---

### Install:

```pip install --upgrade altitudo```

### Uninstall:
```pip uninstall altitudo```


---

Package to get elevation / altitude from a given geo coordinate


* Free software: The Unlicense
* Documentation: https://altitudo.readthedocs.io.
