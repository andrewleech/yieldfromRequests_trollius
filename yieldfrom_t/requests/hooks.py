# -*- coding: utf-8 -*-

"""
requests.hooks
~~~~~~~~~~~~~~

This module provides the capabilities for the Requests hooks system.

Available hooks:

``response``:
    The response generated from a Request.

"""
import trollius as asyncio
from trollius import From, Return

HOOKS = ['response']


def default_hooks():
    hooks = {}
    for event in HOOKS:
        hooks[event] = []
    return hooks

# TODO: response is the only one

@asyncio.coroutine
def dispatch_hook(key, hooks, hook_data, **kwargs):
    """Dispatches a hook dictionary on a given piece of data."""

    hooks = hooks or dict()

    if key in hooks:
        hooks = hooks.get(key)

        if hasattr(hooks, '__call__'):
            hooks = [hooks]

        for hook in hooks:
            _hook_data = yield From(hook(hook_data, **kwargs))
            if _hook_data is not None:
                hook_data = _hook_data

    raise Return(hook_data)
