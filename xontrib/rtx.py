import sys, subprocess
from os             	import environ
from pathlib        	import Path
from xonsh.built_ins	import XSH

__all__ = ()
base     	= 'rtx'
base_path	= Path(f'~/bin/{base}').expanduser()

envx             	= XSH.env
get_cmd          	= XSH.commands_cache.locate_binary
get_cmd_lazy     	= XSH.commands_cache.lazy_locate_binary
isCmdCacheFresh  	= False

# Get user config
_log             	= int(envx.get('XONTRIB_RTX_LOGLEVEL', 1)) # 0 none, 1 error, 2 warning, 3 extra
_lis_cmd_trans   	= False if envx.get('XONTRIB_RTX_NEWLINE_REFRESH', True) == False else True
cmd_pos_chunk_def	= ['.tool-versions']
cmd_pos_chunk    	= envx.get('XONTRIB_RTX_CHUNK_LIST', cmd_pos_chunk_def)
_lis_cmd_pos     	= False if cmd_pos_chunk == False else True
if _lis_cmd_pos:
  if not (user_t := type(cmd_pos_chunk)) == list:
    if _log >= 1:
      print_color(f"{{BLUE}}xontrib-rtx:{{RED}} error:{{RESET}} {{BLUE}}XONTRIB_RTX_CHUNK_LIST{{RESET}} config should be {{BLUE}}{list}{{RESET}}, not {{BLUE}}{user_t}{{RESET}}: {cmd_pos_chunk} ")
    cmd_pos_chunk	= cmd_pos_chunk_def
  for i,chunk in enumerate(cmd_pos_chunk):
    if not (user_t := type(chunk)) == str:
      if _log >= 1:
        print_color(f"{{BLUE}}xontrib-rtx:{{RED}} error:{{RESET}} {{BLUE}}XONTRIB_RTX_CHUNK_LIST{{RESET}} items should be {{BLUE}}{str}{{RESET}}, not {{BLUE}}{user_t}{{RESET}}: item#{i+1} = {chunk} ")
      cmd_pos_chunk	= cmd_pos_chunk_def
      break

bin	= None
def get_bin(base=base): # get Path to binary if exists
  global isCmdCacheFresh
  bin   = get_cmd_lazy(base, ignore_alias=True) # find lazily
  if not bin and not isCmdCacheFresh:           # refresh cache if not found, try again
    isCmdCacheFresh = True
    bin = get_cmd(     base, ignore_alias=True)
  if not bin and base_path.exists():          # try the default path
    bin = base_path
  if not bin:
    PATH = envx.get("PATH")
    if _log >= 1:
      print_color(f"{{BLUE}}xontrib-rtx:{{RED}} error:{{RESET}} can't find '{{BLUE}}{base}{{RESET}}' in either\n  commands cache: {PATH} or\n  default path: {base_path}")
    return None
  else:
    _color = envx.get('XONTRIB_RTX_FORCE_COLOR', True)
    if _color:
      envx[   'FORCE_COLOR'] = True
      environ['FORCE_COLOR'] = envx.get_detyped('FORCE_COLOR')
    return bin

# Hook Events
def listen_init():
  update_env()

def listen_cd(olddir:str, newdir:str, **_):
  update_env()

def listen_transform(cmd:str, **_):
  if cmd == '\n': # update on ↩ to check if .tool-versions is updated
    update_env()
  return cmd

def listen_cmd_pos(cmd:str, rtn:int, out:str or None, ts:list, **_):
  # test: track chunks in successful commands to notice when '.tool-versions' can be changed
  if not rtn and any(ch in cmd for ch in cmd_pos_chunk):
    update_env()

# def listen_prompt(): # can replace all of the ↑, but too general
  # update_env()

def update_env():
  ctx = XSH.ctx

  rtx_hook_proc  = subprocess.run([bin,'hook-env','-s','xonsh'],capture_output=True)
  rtx_hook       = rtx_hook_proc.stdout # ↑ set $__RTX_DIR, $__RTX_DIFF, $__RTX_WATCH
  rtx_hook_err   = rtx_hook_proc.stderr

  if rtx_hook_err:
    print(rtx_hook_err.decode().rstrip(), file=sys.stderr)
  if rtx_hook:
    execx(rtx_hook.decode(), 'exec', ctx, filename='rtx')

# Activate
def _activate_rtx():
  global bin
  if (bin := get_bin()):                            	# if rtx exists register events↓
    events.on_post_init          (listen_init     ) 	# startup (initialization finished)
    events.on_chdir              (listen_cd       ) 	# dir change
    if _lis_cmd_trans:                              	#
      events.on_transform_command(listen_transform) 	# on ⏎ (!chains with other transfroms!)
    if _lis_cmd_pos:                                	#
      events.on_postcommand      (listen_cmd_pos  ) 	# after a command is executed
    #events.on_precommand         (listen_cmd      )	# before a command is executed
    #events.on_pre_prompt         (listen_prompt   )	# before showing the prompt

_activate_rtx()
