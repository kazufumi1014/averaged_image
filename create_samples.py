from pathlib import Path
import numpy as np
from PIL import Image

output_dir = Path("images")
output_dir.mkdir(exist_ok=True)

size = (200, 200)

rng = np.random.default_rng(seed=42)

for i in range(1, 101):
    color = tuple(rng.integers(0, 256, size=3).tolist())
    filename = f"image_{i:03d}.jpg"
    arr = np.full((*size[::-1], 3), color, dtype=np.uint8)
    Image.fromarray(arr, "RGB").save(output_dir / filename, "JPEG", quality=95)
    print(f"Created {output_dir / filename} {size} color={color}")
