from nudenet import NudeDetector

# Initialize the detector
detector = NudeDetector()

# Run detection on an image
result = detector.detect('blurman.jpeg')  # Make sure 'image.jpg' is in the same directory
print(result)

# Optionally, you can run detection on a batch of images

print(result)
