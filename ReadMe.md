<p align="center">
Initializes rtx (polyglot asdf-like runtime manager)
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=Nice%20xontrib%20for%20the%20xonsh%20shell!&url=https://github.com/eugenesvk/xontrib-rtx" target="_blank">tweet</a>.
</p>


## Installation

To install use pip:

```bash
xpip install xontrib-rtx
# or: xpip install -U git+https://github.com/eugenesvk/xontrib-rtx
```

## Usage


This xontrib will get loaded automatically for interactive sessions.
To stop this, set

```xonsh
$XONTRIBS_AUTOLOAD_DISABLED = {"ptk_shell", }
```


## Examples

...

## Known issues

...

## Releasing your package

- Bump the version of your package.
- Create a GitHub release (The release notes are automatically generated as a draft release after each push).
- And publish with `poetry publish --build` or `twine`

## Credits

This package was created with [xontrib template](https://github.com/xonsh/xontrib-template).
