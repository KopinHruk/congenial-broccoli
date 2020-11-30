import argparse

from utils.inference import load_image, predict


def get_parser():
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('image_path', type=str,
                        help='Path to image to process.')

    return parser.parse_args()



def main():
    args = get_parser()

    image = load_image(args.image_path)

    out = predict(image)

    print(out)


if __name__ == '__main__':
    main()