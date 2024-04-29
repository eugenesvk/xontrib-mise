<p align="center">
Initialize <a href="https://github.com/jdx/mise" target="_blank">mise</a> (polyglot asdf-like runtime manager in Rust)</br>
in a more performant and flexible way
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=Nice%20xontrib%20for%20the%20xonsh%20shell!&url=https://github.com/eugenesvk/xontrib-mise" target="_blank">tweet</a>.
</p>

This xontrib adds a couple of (maybe too tiny to notice) improvements:

  - (no cost) replaces the subprocess syntax for the hook mise function with a pure python syntax, which for some reason improves hook runtime by __~60%__ (but in absolute terms maybe just a dozen or two `ms`)
  - (less convenient) replaces a hook on every prompt paint with hooks on
    - shell launch
    - changing dirs
    - empty commands</br>
      useful to refresh shell status when you edit `.tool-versions` _outside_ of shell (optional)
    - commands that containt custom text chunks</br>
      useful to refresh shell status when you edit `.tool-versions`  _in_ a shell (optional)

## Installation

To install use pip:

```bash
xpip install xontrib-mise
# or: xpip install -U git+https://github.com/eugenesvk/xontrib-mise
```

## Usage

This xontrib requires `mise` to be in `PATH` or `~/bin`; or if it's added to `PATH` via another xontrib (e.g, you installed it via Homebrew and use `xontrib-homebrew`), then you should load this xontrib after the one setting `PATH`

1. Add the following to your `.py` xontrib loading config and `import` it in your xonsh run control file (`~/.xonshrc` or `~/.config/rc.xsh`):
```py
from xonsh.xontribs 	import xontribs_load
from xonsh.built_ins	import XSH
envx = XSH.env

xontribs = [ "mise", # Initializes mise (polyglot asdf-like runtime manager)
 # your other xontribs
]
# ↓ optional configuration variables
if 'mise' in xontribs: # Configure mise only if you're actually loading
  # config var                        	  value             	  |default|alt_cmd¦ comment
  envx['XONTRIB_MISE_CHUNK_LIST']     	= ['.tool-versions']	# |['.tool-versions']|False¦ (feeble attempts to track edits to `.tool-versions` in the command line) update mise status if command contains any of the string chunks in this list; False to disable this listener completely
  envx['XONTRIB_MISE_NEWLINE_REFRESH']	= True              	# |True|False¦ update mise status if command is empty (e.g, ⏎ on a blank line to refresh after editing `.tool-versions` in a text editor); False to disable this listener completely
  envx['XONTRIB_MISE_FORCE_COLOR']    	= True              	# |True|False¦ preserve colored mise output
  envx['XONTRIB_MISE_LOGLEVEL']       	= 1                 	# |1|0¦ print xontrib log messages: 0 none, 1 error; 'mise' stderr is always passed through
# (old variables with _RTX_ in the name continue to work)
xontribs_load(xontribs) # actually load all xontribs in the list
```

2. Or just add this to your xonsh run control file
```xsh
xontrib load mise # Initializes mise (polyglot asdf-like runtime manager)
# configure like in the example above, but replace envx['VAR'] with $VAR
$XONTRIB_MISE_LOGLEVEL = 1
```

## Known issues

- In the future xontrib-mise will be autoloaded, but this is currently blocked due to a [xonsh bug](https://github.com/xonsh/xonsh/issues/5020): too early autoload prevents reading user config; also, autoloading can't be disabled

## Credits

This package was created with [xontrib template](https://github.com/xonsh/xontrib-template)
