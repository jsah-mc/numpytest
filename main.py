import numpy as np


def main():
    array_3d = np.array(
        [
            [[1, 2, 3], [4, 5, 6]],
            [[7, 8, 9], [10, 11, 12]],
        ]
    )
    print(array_3d)
    print("shape:", array_3d.shape)
    print("size:", array_3d[1].size)


if __name__ == "__main__":
    main()
