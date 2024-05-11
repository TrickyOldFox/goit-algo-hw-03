"""
Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії, переміщає їх до нової директорії
та сортує в піддиректорії, назви яких базуються на розширенні файлів.
"""
import argparse
import os
from os.path import isfile, join
import shutil


argparse = argparse.ArgumentParser()

argparse.add_argument(
    "--input-dist",
    dest="input_dist",
    required=True,
    help="path to input dist"
)
argparse.add_argument(
    "--output-dist",
    dest="output_dist",
    default="dist",
    help="path to output dist"
)


def solve_for_dist(input_dist, output_dist):
    for el in os.listdir(input_dist):
        if isfile(join(input_dist, el)):
            os.makedirs(output_dist, exist_ok=True)
            os.makedirs(
                join(output_dist, os.path.splitext(el)[1][1:]),
                exist_ok=True
            )
            shutil.copy(
                join(input_dist, el),
                join(join(output_dist, os.path.splitext(el)[1][1:]), el)
            )
            continue

        solve_for_dist(join(input_dist, el), join(output_dist, el))


def main() -> None:
    args = argparse.parse_args()
    input_dist = args.input_dist
    output_dist = args.output_dist

    try:
        solve_for_dist(input_dist, output_dist)
    except Exception as e:
        print(f"An error occurred while solving dist {e}")


if __name__ == "__main__":
    main()
