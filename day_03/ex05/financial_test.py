import pytest
import sys

from financial import run

@pytest.mark.parametrize('args', [("AAPL", "Total Revenue"), ("MSFT", "Total Revenue")])
def test_run_returns_correct_name(monkeypatch, args):
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', ['financial', *args])
        assert run()[0] == "Total Revenue"

@pytest.mark.parametrize('args', [("AAPL", "Total Revenue"), ("MSFT", "Total Revenue")])
def test_run_returns_type(monkeypatch, args):
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', ['financial', *args])
        assert type(run()) == tuple

@pytest.mark.parametrize('args', [("APELE", "Total Revenue"), ("MAKASOFT", "Total Revenue")])
def test_run_raises_error(monkeypatch, args):
    from financial import ArgError
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', ['financial', *args])
        with pytest.raises(ArgError):
            run()