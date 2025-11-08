import argparse
import os
from pathlib import Path
from rembg import remove
from PIL import Image, UnidentifiedImageError
import sys

# Define the image extensions we want to look for
SUPPORTED_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.tiff')

def process_image(input_path, output_path):
    """
    Removes the background from a single image and saves it.
    """
    try:
        # Open the input image
        with Image.open(input_path) as img:
            # Remove the background
            output_image = remove(img)
            
            # Save the new image
            output_image.save(output_path)
            print(f"Processed: {input_path}")
            print(f"      Saved: {output_path}\n")

    except UnidentifiedImageError:
        print(f"Skipped: Cannot identify image file {input_path}\n")
    except Exception as e:
        print(f"Error processing {input_path}: {e}\n")

def process_image_threshold(input_path, output_path, threshold=240):
    """
    Removes background based on a white-lightness threshold.
    Good for high-contrast sketches and line art.
    """
    try:
        with Image.open(input_path) as img:
            # Convert to RGBA to add an alpha (transparency) channel
            img = img.convert("RGBA")
            
            datas = img.getdata()
            
            new_data = []
            for item in datas:
                # Check if the pixel is "white enough" (R, G, and B are all above threshold)
                if item[0] > threshold and item[1] > threshold and item[2] > threshold:
                    # Make it transparent (Alpha channel = 0)
                    new_data.append((255, 255, 255, 0))
                else:
                    # Keep the original pixel, but ensure it's fully opaque
                    new_data.append((*item[:3], 255))
                    
            img.putdata(new_data)
            img.save(output_path)
            print(f"Processed (Threshold): {input_path}")
            print(f"                Saved: {output_path}\n")

    except UnidentifiedImageError:
        print(f"Skipped: Cannot identify image file {input_path}\n")
    except Exception as e:
        print(f"Error processing {input_path} with threshold: {e}\n")


def get_output_path(input_path, suffix="_nobg"):
    """
    Generates a .png output path for a given input path.
    Example: 'folder/image.jpg' -> 'folder/image_nobg.png'
    """
    # Use pathlib for easy path manipulation
    p = Path(input_path)
    # New stem will be 'filename' + '_nobg'
    new_stem = f"{p.stem}{suffix}"
    # New path will be in the same directory, with the new stem, and a .png extension
    output_path = p.with_stem(new_stem).with_suffix('.png')
    return output_path

def main():
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(
        description="Remove the background from an image or all images in a folder."
    )
    parser.add_argument(
        "input_path",
        type=str,
        help="The path to the input image file or folder."
    )
    parser.add_argument(
        "-s", "--suffix",
        type=str,
        default="_nobg",
        help="The suffix to add to output filenames (default: '_nobg')."
    )
    parser.add_argument(
        "-m", "--method",
        type=str,
        default="rembg",
        choices=["rembg", "threshold"],
        help="The processing method: 'rembg' (AI) or 'threshold' (white-based)."
    )
    parser.add_argument(
        "-t", "--threshold",
        type=int,
        default=240,
        help="Lightness threshold for 'threshold' method (0-255). 255 is pure white. Default: 240"
    )

    args = parser.parse_args()
    
    # --- Check if the input path is valid ---
    if not os.path.exists(args.input_path):
        print(f"Error: Path does not exist: {args.input_path}")
        sys.exit(1) # Exit the script with an error code

    # --- Case 1: The path is a single file ---
    if os.path.isfile(args.input_path):
        if args.input_path.lower().endswith(SUPPORTED_EXTENSIONS):
            output_path = get_output_path(args.input_path, args.suffix)
            if args.method == "rembg":
                process_image(args.input_path, output_path)
            else:
                process_image_threshold(args.input_path, output_path, args.threshold)
        else:
            print(f"Skipped: File is not a supported image type: {args.input_path}")
    
    # --- Case 2: The path is a directory ---
    elif os.path.isdir(args.input_path):
        print(f"Processing directory: {args.input_path}\n")
        
        # Use os.walk to go through all files and subdirectories
        for root, dirs, files in os.walk(args.input_path):
            for file in files:
                if file.lower().endswith(SUPPORTED_EXTENSIONS):
                    # Reconstruct the full path to the image
                    full_input_path = os.path.join(root, file)
                    
                    # Generate the output path
                    output_path = get_output_path(full_input_path, args.suffix)
                    
                    # Process the image
                    if args.method == "rembg":
                        process_image(full_input_path, output_path)
                    else:
                        process_image_threshold(full_input_path, output_path, args.threshold)
    
    else:
        print(f"Error: Path is not a file or directory: {args.input_path}")
        sys.exit(1)

    print("Background removal complete.")

if __name__ == "__main__":
    main()

