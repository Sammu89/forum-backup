import pytest


@pytest.fixture
def tmp_root(tmp_path):
    """
    Create an isolated BACKUP_ROOT folder for each test.
    Auto-cleaned by pytest.
    """
    return tmp_path
