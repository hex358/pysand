# Example of how you setup your module.


TAGS = ["--no-processing"] # _process function won't be called.
USE_MODULES = ["render"]
render = None # This will be assigned by mainloop

modules_dict = {}
def _ready() -> None:
    # print("Test")
    pass

def _process(delta: float) -> None:
    # If processing is not disabled, called every frame.
    # delta:float is time since the last one.
    pass