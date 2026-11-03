import os
import hashlib
import exifread
from PIL import Image, ImageChops, ImageEnhance

def metadata(path):
    print("\n===== IMAGE METADATA =====")
    with open(path, 'rb') as f:
        tags = exifread.process_file(f)
        if tags:
            for tag, value in tags.items():
                print(f"{tag}: {value}")
        else:
            print("No EXIF metadata found.")

def generate_hash(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            h.update(chunk)
    return h.hexdigest()

def ela_analysis(path):
    print("\n===== ERROR LEVEL ANALYSIS =====")
    original = Image.open(path).convert("RGB")
    original.save("temp.jpg", "JPEG", quality=95)
    compressed = Image.open("temp.jpg")
    diff = ImageChops.difference(original, compressed)
    diff = ImageEnhance.Brightness(diff).enhance(30)
    diff.save("ela_result.jpg")
    os.remove("temp.jpg")
    print("ELA completed. Saved as ela_result.jpg")

def analyze_image(path):
    if not os.path.isfile(path):
        print("Image not found!")
        return

    print("\n===== IMAGE FORENSIC REPORT =====")
    print("File:", path)
    img = Image.open(path)
    print("Format:", img.format)
    print("Dimensions:", img.size)
    print("MD5 Hash:", generate_hash(path))

    metadata(path)
    ela_analysis(path)

def compare_images():
    original = input("Enter original image path: ")
    suspected = input("Enter suspected image path: ")

    if not os.path.isfile(original) or not os.path.isfile(suspected):
        print("Image not found!")
        return

    h1 = generate_hash(original)
    h2 = generate_hash(suspected)

    print("\n===== INTEGRITY VERIFICATION =====")
    print("Original Hash:", h1)
    print("Suspected Hash:", h2)

    if h1 == h2:
        print("Result: IDENTICAL FILE CONTENTS")
    else:
        print("Result: DIFFERENT FILE CONTENTS")
        print("Possible modification detected.")

    ela_analysis(suspected)

while True:
    print("\n===== DIGITAL IMAGE FORENSIC TOOL =====")
    print("1. Analyze Image")
    print("2. Compare Original and Suspected Image")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        path = input("Enter image path: ")
        analyze_image(path)

    elif choice == '2':
        compare_images()

    elif choice == '3':
        print("Forensic analysis completed.")
        break

    else:
        print("Invalid choice!")
