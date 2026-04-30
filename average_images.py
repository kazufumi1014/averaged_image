import sys
from pathlib import Path

import numpy as np
from PIL import Image


def average_images(images_dir: str = "images", output_path: str = "averaged.jpg") -> None:
    image_paths = sorted(Path(images_dir).glob("*.jpg")) + sorted(Path(images_dir).glob("*.jpeg"))

    if not image_paths:
        print(f"Error: No JPEG images found in '{images_dir}'")
        sys.exit(1)

    print(f"Found {len(image_paths)} images:")
    for p in image_paths:
        print(f"  {p}")

    arrays = []
    base_size = None

    for path in image_paths:
        img = Image.open(path).convert("RGB")
        if base_size is None:
            base_size = img.size
        elif img.size != base_size:
            print(f"Warning: '{path}' size {img.size} differs from expected {base_size}, skipping.")
            continue
        arrays.append(np.array(img, dtype=np.float64))

    averaged = np.mean(arrays, axis=0).round().astype(np.uint8)
    result = Image.fromarray(averaged, mode="RGB")
    result.save(output_path, "JPEG", quality=95)
    print(f"Saved averaged image to '{output_path}'")


if __name__ == "__main__":
    images_dir = sys.argv[1] if len(sys.argv) > 1 else "images"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "averaged.jpg"
    average_images(images_dir, output_path)
