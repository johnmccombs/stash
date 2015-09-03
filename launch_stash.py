# coding: utf-8
"""
Launch StaSh in a more flexible and reliable way.
"""
import os
import sys

module_names = (
    'system.shutil',
    'system.shstreams',
    'system.shscreens',
    'system.shterminal',
    'system.shui',
    'system.shio',
)

# Find out where the launch script is located and import differently
_LAUNCH_DIR = os.path.realpath(os.path.abspath(os.path.dirname(__file__)))

if os.path.isfile(os.path.join(_LAUNCH_DIR, 'stash.py')) \
        and os.path.isfile(os.path.join(_LAUNCH_DIR, '__init__.py')) \
        and os.path.isdir(os.path.join(_LAUNCH_DIR, 'system')):

    if 'stash' in sys.modules:
        stash = sys.modules['stash']
        reload(stash)
        for name in module_names:
            if name in sys.modules:
                reload(sys.modules[name])
    import stash

else:
    if 'stash.stash' in sys.modules:
        stash = sys.modules['stash.stash']
        reload(stash)
        for name in module_names:
            if name in sys.modules:
                reload(sys.modules['stash.' + name])
    else:
        from stash import stash

# noinspection PyProtectedMember
debug = (
    # stash._DEBUG_STREAM,
    # stash._DEBUG_RENDERER,
    # stash._DEBUG_MAIN_SCREEN,
    # stash._DEBUG_MINI_BUFFER,
    # stash._DEBUG_IO,
    # stash._DEBUG_UI,
    # stash._DEBUG_TERMINAL,
    # stash._DEBUG_TV_DELEGATE,
    # stash._DEBUG_RUNTIME,
    # stash._DEBUG_PARSER,
    # stash._DEBUG_EXPANDER,
    # stash._DEBUG_COMPLETER,
)

log_setting = {
    'level': 'INFO'
}

_stash = stash.StaSh(debug=debug, log_setting=log_setting)

_stash.launch()