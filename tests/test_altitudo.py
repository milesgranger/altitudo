#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `altitudo` package."""

import pytest

from click.testing import CliRunner
from altitudo import cli, altitudo


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ['--', 39.90974, -106.17188])
    print(result.output)
    assert result.exit_code == 0
    assert '2624.0\n' == result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert 'Usage: altitudo [OPTIONS] LAT LON' in help_result.output

def test_altitudo_single_coordinate():
    """Test a single coordinate"""
    elevation = altitudo(lat=39.90974, lon=-106.17188)
    assert isinstance(elevation, float)

def test_altitudo_multi_coordinates():
    elevations = altitudo(lat=[39.90974, 39.90974], lon=[-106.17188, -106.17188])
    assert isinstance(elevations, list)
    assert isinstance(elevations[0], dict)
    assert len(elevations) == 2

def test_altitudo_convert_feet():
    elevation = altitudo(lat=39.90974, lon=-106.17188)
    assert elevation == 2624.0
    elevation = altitudo(lat=39.90974, lon=-106.17188, feet=True)
    assert elevation == 2624.0 * 3.28084
