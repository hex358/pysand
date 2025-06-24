
import sys
to_flush = []
def reimport(enqueue: str = "", **injected):
    def wrap(cls):
        if enqueue: to_flush.append((enqueue,cls,injected)); return cls
        for name, value in injected.items():
            setattr(cls, name, value)
        return cls
    return wrap

def flush():
    for module, cls, injected in to_flush:
        for name in injected:
            setattr(cls, name, getattr(sys.modules[module], name))
    to_flush.clear()