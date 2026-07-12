import pytest

@pytest.fixture(autouse=True) # make all tests automatically request this fixture
def test_it_loads(load_xontrib):
  return load_xontrib("mise")

# how to actually load and
def test_update():
  # todo: why does this return string during test, but not during actual use
  from xonsh.built_ins import XSH
  envx = XSH.env
  cmd_pos_chunk_def = ['.tool-versions']
  print(f"def = {cmd_pos_chunk_def} type = {type(cmd_pos_chunk_def)}")
  cmd_pos_chunk = envx.get('XONTRIB_MISE_CHUNK_LIST', envx.get('XONTRIB_RTX_CHUNK_LIST', cmd_pos_chunk_def))
  print(f"env = {cmd_pos_chunk} type = {type(cmd_pos_chunk)}")

  # todo: how to load/test individual xontrib functions like update_env
  # from xonsh.xontribs import xontribs_load
  # xontribs_load(['mise'])
  # import mise
  # load_xontrib("mise")
  # import xontrib_mise
  # import xonsh_mise
  # from mise import update_env
  # update_env()
  # help('modules')

  assert 1 == 1
