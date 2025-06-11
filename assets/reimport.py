
import sys
to_flush = []
def reimport(enqueue: bool = False, **injected):
    def wrap(cls):
        if enqueue: to_flush.append((cls,injected)); return cls
        for name, value in injected.items():
            setattr(cls, name, value)
        return cls
    return wrap

def flush():
    for cls, injected in to_flush:
        for name in injected:
            setattr(cls, name, getattr(sys.modules["__main__"], name))
    to_flush.clear()