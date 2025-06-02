import requests
import json
from PIL import Image, ImageDraw
import pyttsx3

# Load Azure credentials from JSON config
with open("config_template.json") as f:
    config = json.load(f)

subscription_key = config["key"]
endpoint = config["endpoint"]

# Azure Vision API URL
analyze_url = endpoint + "vision/v3.2/analyze"

# Path to input image
image_path = "complex_image.jpg"
image_data = open(image_path, "rb").read()

# Request headers and parameters
headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/octet-stream"
}

params = {
    "visualFeatures": "Tags,Description,Objects"
}

# Send request
response = requests.post(
    analyze_url,
    headers=headers,
    params=params,
    data=image_data
)

# Check for errors
response.raise_for_status()

# Parse response
analysis = response.json()

# Extract image caption and confidence
caption = analysis["description"]["captions"][0]["text"]
confidence = analysis["description"]["captions"][0]["confidence"]

# Print raw analysis for debugging
print(json.dumps(analysis, indent=2))

# Print formatted caption
print(f'The image shows: "{caption}" (confidence: {confidence:.2%})')

# List detected objects
print("\nDetected objects in the image:")

if "objects" in analysis and analysis["objects"]:
    for obj in analysis["objects"]:
        name = obj["object"]
        confidence = obj["confidence"]
        print(f"- {name} (confidence: {confidence:.2%})")
else:
    print("No objects detected.")

# Prepare objects for TTS
if "objects" in analysis and analysis["objects"]:
    object_names = [obj["object"] for obj in analysis["objects"]]
    objects_text = ", ".join(object_names)
    object_read_text = f"I can also see: {objects_text}."
else:
    object_read_text = "No objects were detected."

# Text-to-Speech: caption + object list
engine = pyttsx3.init()
full_text = f"The image shows: {caption}. {object_read_text}"
engine.say(full_text)
engine.runAndWait()

# Load image and draw bounding boxes
image = Image.open(image_path)
draw = ImageDraw.Draw(image)

if "objects" in analysis and analysis["objects"]:
    for obj in analysis["objects"]:
        rect = obj["rectangle"]
        label = obj["object"]
        confidence = obj["confidence"]

        x, y, w, h = rect["x"], rect["y"], rect["w"], rect["h"]

        # Draw bounding box and label
        draw.rectangle([x, y, x + w, y + h], outline="red", width=3)
        draw.text((x, y - 10), f"{label} ({confidence:.0%})", fill="red")

# Save and show result
output_path = "output-with-boxes.jpg"
image.save(output_path)
image.show()