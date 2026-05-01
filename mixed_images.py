import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image


def _load_arrays(images_dir: str) -> list[np.ndarray]:
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

    return arrays


def average_images(images_dir: str = "images", output_path: str = "averaged.jpg") -> None:
    arrays = _load_arrays(images_dir)
    result_array = np.mean(arrays, axis=0).round().astype(np.uint8)
    result = Image.fromarray(result_array, mode="RGB")
    result.save(output_path, "JPEG", quality=95)
    print(f"Saved averaged image to '{output_path}'")


def darkest_images(images_dir: str = "images", output_path: str = "darkest.jpg") -> None:
    arrays = _load_arrays(images_dir)
    # ピクセルごと・チャンネルごとに最小値(最も暗い値)を採用
    result_array = np.min(arrays, axis=0).astype(np.uint8)
    result = Image.fromarray(result_array, mode="RGB")
    result.save(output_path, "JPEG", quality=95)
    print(f"Saved darkest image to '{output_path}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine multiple JPEG images into one.")
    parser.add_argument("--mode", choices=["average", "darkest"], default="average",
                        help="average: 平均化 / darkest: 最も暗いピクセルを採用 (default: average)")
    parser.add_argument("--input", default="images", help="Input directory (default: images)")
    parser.add_argument("--output", default=None, help="Output file path (default: averaged.jpg or darkest.jpg)")
    args = parser.parse_args()

    if args.mode == "average":
        output = args.output or "averaged.jpg"
        average_images(args.input, output)
    else:
        output = args.output or "darkest.jpg"
        darkest_images(args.input, output)
