
from src.scripts.graficos_funciones import generar_graficos


def test_generar_seis_graficos(tmp_path):
    archivos = generar_graficos(tmp_path)

    assert len(archivos) == 6

    for archivo in archivos:
        assert archivo.exists()


def test_grafico_raiz_doble(tmp_path):
    generar_graficos(tmp_path)

    archivo = tmp_path / "raiz_doble.png"

    assert archivo.exists()
    assert archivo.stat().st_size > 0
