from PIL import Image, ImageFilter, ImageOps
import os


def main():
    print("Digital Image Filter and Color Converter")
    print("1. Grayscale")
    print("2. Black and White (Threshold)")
    print("3. Blur Image")
    print("4. Color Invert")

    image_path = input("Enter image path: ").strip().strip('"')

    if not os.path.isfile(image_path):
        print("Error: Image file not found!")
        return

    try:
        image = Image.open(image_path).convert("RGB")
    except Exception as e:
        print("Error opening image:", e)
        return

    print("Choose a filter:")
    choice = input("Enter choice (1-4): ")

    if choice == "1":
        result = ImageOps.grayscale(image)

    elif choice == "2":
        grayscale = ImageOps.grayscale(image)
        result = grayscale.point(
            lambda pixel: 255 if pixel >= 128 else 0
        )

    elif choice == "3":
        result = image.filter(ImageFilter.BLUR)

    elif choice == "4":
        result = ImageOps.invert(image)

    else:
        print("Invalid choice!")
        return

    output_path = os.path.splitext(image_path)[0] + "_processed.png"
    result.save(output_path)

    print("Image processed successfully!")
    print("Saved at:", output_path)

    result.show()


if __name__ == "__main__":
    main()