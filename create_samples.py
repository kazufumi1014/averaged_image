from pathlib import Path
import numpy as np
from PIL import Image

output_dir = Path("images")
output_dir.mkdir(exist_ok=True)

size = (200, 200)

samples = [
    ("red.jpg",   (255,   0,   0)),
    ("green.jpg", (  0, 255,   0)),
    ("blue.jpg",  (  0,   0, 255)),
]

for filename, color in samples:
    arr = np.full((*size[::-1], 3), color, dtype=np.uint8)
    Image.fromarray(arr, "RGB").save(output_dir / filename, "JPEG", quality=95)
    print(f"Created {output_dir / filename} {size} color={color}")
