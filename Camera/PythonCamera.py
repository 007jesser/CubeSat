import time
from picamera import PiCamera
from PIL import Image

# Initialize camera
camera = PiCamera()

# Defining pixel heights and widths for the image
height = 100
width = 100

# Capture the image
camera.resolution = (width, height)
time.sleep(2)  # Allow camera to adjust before capturing (if needed)
camera.capture('image.bmp')

# Threshold cutoff parameters
average_pixel_threshold = 200  # The minimum threshold value to trigger a true pixel
threshold_value = (average_pixel_threshold ** 2) * 3  # The value to check against to trigger a true pixel
minimum_true_pixels = 40  # The number of true pixels required for a hit
lightning_detected = False

# Open and process the image
with Image.open('image.bmp') as img:
    img = img.convert('RGB')  # Ensure the image is in RGB format
    pixels = img.load()

    # Count pixels that meet the threshold criteria
    threshold_count = 0
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixel_intensity = r**2 + g**2 + b**2
            if pixel_intensity >= threshold_value:
                threshold_count += 1

    # Check if lightning is detected based on threshold count
    lightning_detected = threshold_count > minimum_true_pixels

# Output results
print("Threshold Count:", threshold_count)
print("Lightning Detected:", lightning_detected)

# Optionally, you could compress the image before transmission
# img.save('image_compressed.jpg', 'JPEG', quality=75)
