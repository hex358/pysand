# PySand - an open-source particle sandbox

<img width=400,  src="https://media.discordapp.net/attachments/1182918701641650207/1392125835758010391/q.png?ex=686e65b7&is=686d1437&hm=ecf314358538bc3e06f889a9b30f53c29df16d9d8addbc00902e82ed0c19183b&=&format=webp&quality=lossless&width=950&height=859"></img>
<br>PySand is a minimal but extensible sandbox game. It's written in Python, rendering api is OpenGL.

## Features

* **Base Classes**:
  * Powder
  * Liquid
  * Gas
  * Fire
  * Plant
  * Seed
* **Custom Interactions**. Each element can use a set of basic interactions (fire spreading into flammable elements, water flowing, etc.) and extend them using custom interactions.
* **Configurable graphics**. PySand provides basic abstractions and classes for drawing (see `./modules/render.py`). Feel free to utilise UI elements like buttons and scrollbars, and to configure shaders.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/hex358/pysand.git
   cd pysand
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```


3. Start the sandbox with:

    ```bash
    python main.py
    ```

Use the UI to place elements and watch them interact.

## Modding

PySand ships with a default element config interface `./config.py` (for more complex modifications, change the `./modules/element_storage.py` itself). You can add or modify element definitions:

```python
import modules.element_storage as el
from modules.element_storage import *

# Define custom colors (RGBA tuples)
el.colors = [
    (0.2, 0.2, 0.2, 1.0),  # AIR
    (0.75, 0.69, 0.50, 1.0),
    # ...
]

# Map indices to element names
el.names = [
    "AIR", "SAND", "WATER", "STONE", "WOOD", "LAVA", "VAPOR",
    # ...
]

# Set element categories and behaviors
el.all_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 99]
el.gases = [0, 6]
el.liquids = [2, 5, 14]
# ...

# Define element types with properties and interactions
el.element_types = {
    1: Powder(index=1, gravity_direction=-1, density=80),
    2: Powder(index=2, evaporates_into=6, density=40, custom_interactions=[
        Interaction(with_powder=7, itself_turns_into=2, other_turns_into=8, probability=100)
    ]),
    11: Flame(11, spread_speed=60, dissolve_in=[0,6]),
    # ...
}
```

> **Note:** To change colors, tweak `shaders/fragment.glsl` manually.

## Creating Elements

* Assign it an unused index in `el.all_elements`.
* Append its RGBA color.
* Add its name to `el.names`.
* Define its behavior in `el.element_types`. Classes `Flame`, `Powder`, `Plant` or `Seed` just simplify the construction of your element.<br> To assign it packs of interactions (being burnable/hot/liquid/etc.), set property `class_tags`, or for more specific interactions, use `custom_interactions`.
* Optionally, add special effects (like bloom or color gradient) in post-processing shaders.

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-element`)
3. Commit your changes (`git commit -am "Add new element"`)
4. Push to the branch (`git push origin feature/my-element`)
5. Open a pull request

## About this project
Initially I just wanted to gain experience with OpenGL. But over time, taking inspiration from games like [sandboxels](https://github.com/R74nCom/sandboxels), I thought it would be nice to make something similar.<br>Thanks for reading!

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
