"""Pruebas del Sprint 1: traducen los criterios de aceptación de Jira."""
import pytest

from taskflow import GestorTareas


@pytest.fixture
def gestor():
    g = GestorTareas()
    g.agregar("Preparar demo", "alta")
    g.agregar("Escribir README", "media")
    g.agregar("Revisar PR de la pareja", "alta")
    return g


# TF-11 Bug: títulos duplicados
def test_no_permite_titulos_duplicados(gestor):
    with pytest.raises(ValueError):
        gestor.agregar("  preparar DEMO ")
