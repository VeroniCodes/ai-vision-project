# AI Vision App with Object Detection and TTS

Welcome to my first public AI project! This app uses the **Azure AI Vision API** to analyze an image, recognize objects, and then **describes it using text-to-speech (TTS)** – providing a helpful tool especially for the visually impaired.

---

## 🔍 What It Does

- Uploads and analyzes an image using **Azure Computer Vision**  
- Detects objects and describes the image with **natural language**  
- Reads the result out loud using **Python's pyttsx3 TTS engine**  
- Highlights objects with bounding boxes drawn on the image  

---

## 🛠 Tech Stack

| Category         | Tool/Library                |
|------------------|-----------------------------|
| Programming      | Python                      |
| AI Services      | Azure AI Vision API         |
| TTS Engine       | pyttsx3                     |
| Image Handling   | PIL (Pillow)                |
| File Management  | dotenv, requests, os, json  |

---

## 🚀 How to Run

1. **Clone this repo** or download the files.
2. Replace `complex_image.jpg` with your own test image (if you wish).
3. Create a file named `config_template.json` with your Azure API credentials:

```markdown
```json
{
  "AZURE_KEY": "your_azure_subscription_key",
  "AZURE_ENDPOINT": "https://your-custom-endpoint.cognitiveservices.azure.com/"
}
```

Alternatively, you can use a .env file for local development.

4. Run the vision-app-public.py file.

The app will analyze the image, read aloud what it sees, and save a new image file (output-with-boxes.jpg) with red rectangles around detected objects.

---

## ⚠️ Notes
You need an Azure subscription to use the Vision API.

Azure offers a free tier with monthly limits — perfect for testing this app!

No sensitive data is stored or transmitted beyond the API call.

---

## 🌐 Language Support
Currently English-only. Localization options can be added later.

---

## 🎯 Project Purpose
This project was built to support visually impaired users by translating images into sound through AI. I’m especially passionate about AI applications that have real social impact.

---

## 🌱 Goals

- Dive deeper into Computer Vision with real-world challenges  
- Evolve this idea into a fully usable assistive AI tool  
- Sharpen my Python skills and grow as a future developer  
- Create meaningful tech that serves people — not just code  

## 👩‍💻 About Me
I’m an entry-level Python & AI enthusiast, currently building hands-on projects to deepen my skills and contribute to meaningful tech.

📫 Connect with me on LinkedIn: [linkedin.com/in/veronika-dudas-szalai](https://www.linkedin.com/in/veronika-dudas-szalai/)  
🌍 Languages: English 🇬🇧 | German 🇩🇪 | Hungarian 🇭🇺  
💻 Open to remote work, freelance projects, and junior roles worldwide.  

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
Feel free to use, modify, or build upon it — just give credit. 💡

