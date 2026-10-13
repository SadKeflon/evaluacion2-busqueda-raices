
from src.scripts.graficos_convergencia import generar_convergencia


def test_generar_convergencia(tmp_path):
    carpeta_graficos = tmp_path / "graficos"
    carpeta_datos = tmp_path / "datos"

    archivos = generar_convergencia(
        carpeta_graficos, carpeta_datos
    )

    assert len(archivos) == 6

    for archivo in archivos:
        assert archivo.exists()
        assert archivo.stat().st_size > 0


def test_convergencia_raiz_doble(tmp_path):
    archivos = generar_convergencia(
        tmp_path / "graficos",
        tmp_path / "datos"
    )

    nombres = [archivo.name for archivo in archivos]

    assert "convergencia_raiz_doble.png" in nombres
