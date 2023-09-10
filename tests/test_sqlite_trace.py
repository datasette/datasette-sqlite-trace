from datasette.app import Datasette
import pytest


@pytest.mark.asyncio
async def test_sqlite_trace(capsys):
    ds = Datasette()
    response = await ds.client.get("/")
    assert response.status_code == 200
    # Should have printed stuff to stderr
    captured = capsys.readouterr()
    assert "select name from sqlite_master where type='table'" in captured.err
