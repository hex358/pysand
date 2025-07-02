# PySand - an Open-Source Particle Sandbox

<img width=400,  src="https://cdn.discordapp.com/attachments/1182918701641650207/1389859647673995395/ffff.png?ex=6866272a&is=6864d5aa&hm=3eb1fcf87797f25f27f81c62d45d00ff1f248f334a8dd3bfabf34a13f107a62c&"></img>
<br>PySand is a minimal but extensible sandbox game written in Python that uses OpenGL for rendering. <br>Here, each element has a corresponding ID and a set of interactions with other such IDs, and it can produce complex behaviours.

## Features

* **Extensible Element System**. Define custom elements with unique properties and interactions.
* **Base Classes**:

  * Powder
  * Liquid
  * Gas
  * Fire
  * Plant
  * Seed
* **Custom Interactions**. Each element can use a set of basic interactions (fire spreading into burnable elements, water flowing, etc.) and extend them using custom interactions.
* **Configurable graphics**. PySand is done from the scratch on OpenGL. It provides basic abstractions and classes for drawing (see `./modules/render.py`). Feel free to add UI elements like buttons and scrollbars, and to configure shaders.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/pysand.git
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

## Configuration

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

> **Note:** To change colors, tweak `shaders/fragment.glsl` manually, as using uniforms impacts performance.

## Creating Elements

* Assign it an unused index in `el.all_elements`.
* Append its RGBA color.
* Add its name to `el.names`.
* Define its behavior in `el.element_types`. Classes Flame, Powder, Plant or Seed just simplify the construction of your element. To assign it packs of interactions (being burnable/hot/liquid/etc.), set property `class_tags`, or for more specific interactions, use `custom_interactions`.
* If you want, add special effects (like bloom or color gradient) in post-processing shaders.

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-element`)
3. Commit your changes (`git commit -am "Add new element"`)
4. Push to the branch (`git push origin feature/my-element`)
5. Open a pull request

## About this Project
Initially I just wanted to see how PyOpenGL is used in real python projects. But over time, taking inspiration from games like [sandboxels](https://github.com/R74nCom/sandboxels), I thought it would be nice to make something similar.<br>Thanks for reading!

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
