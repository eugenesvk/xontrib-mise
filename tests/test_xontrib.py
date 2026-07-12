import pytest

@pytest.fixture(autouse=True) # make all tests automatically request this fixture
def test_it_loads(load_xontrib):
  return load_xontrib("mise")
