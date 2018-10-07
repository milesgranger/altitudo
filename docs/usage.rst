=====
Usage
=====

To use Altitudo in a project::

    from altitudo import altitudo

    # Return elevation in meters
    elevation = altitudo(lat=39.90974, lon=-106.17188)

    # ...or feet
    elevation = altitudo(lat=39.90974, lon=-106.17188, feet=True)

    # Pass a list of latitude and longitude coordinates
    elevation = altitudo(lat=[39.90974, 40.93028], lon=[-106.17188, -105.1803099])

Note a single coordinate submission results in a single value.
Givening an iterable of coordinates returns a list of dicts.
