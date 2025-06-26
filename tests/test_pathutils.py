from core.pathutils import url_to_local_path

def test_basic_mapping(tmp_root, monkeypatch):
    monkeypatch.setattr("config.settings.BACKUP_ROOT", tmp_root)
    out = url_to_local_path("/f17-something")
    assert out.endswith("categorias/f17-something.html")