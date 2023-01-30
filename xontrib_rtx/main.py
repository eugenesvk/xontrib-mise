from xonsh.built_ins import XonshSession


def _load_xontrib_(xsh: XonshSession, **_):
    # getting environment variable
    var = xsh.env.get("VAR", "default")

    print("Autoloading xontrib: xontrib-rtx")

    
    from .event_hooks import listen_cd
    xsh.builtins.events.on_chdir(listen_cd)
    
    
    from .aliases import git_log
    xsh.aliases["gl"] = git_log
    
