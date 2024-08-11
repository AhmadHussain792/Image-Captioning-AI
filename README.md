# Image-Captioning-AI

This repository contains a simple Gradio web application that generates captions for uploaded images using a pretrained AI model. The application leverages the Salesforce BLIP (Bootstrapping Language-Image Pre-training) model to generate descriptive captions for images.

# Features
Image Captioning: Upload any image, and the AI model will generate a relevant caption for it.

User-Friendly Interface: The app uses Gradio to provide a simple and intuitive interface for interacting with the AI model.

# Requirements
The python version I used and the python libraries are all mentioned in the "REQUIREMENTS.TXT" file

# Code Overview
The necessary libraries are imported

![image](https://github.com/user-attachments/assets/b4450a10-0aeb-4f50-be7a-de543f6faf04)

A pre-trained model is loaded from Hugging Face model hub

![image](https://github.com/user-attachments/assets/ea6a7035-fa4f-4d06-a5eb-b56ca3a0d204)

- AutoProcessor: This is responsible for processing the input image and text, converting them into a format that the model can understand.

- BlipForConditionalGeneration: This is the actual image captioning model that generates captions based on the processed input.

Image Captioning function 

![image](https://github.com/user-attachments/assets/c656e183-c22b-459c-afc9-5b4d0fbc98f0)

- input_image: the image is taken in the form of a NumPy array which is how images are typically represented in python.

- Image.fromarray(input_image).convert("RGB"): converts the NumPy array into a PIL image in RGB format, which is the format expected by the BLIP model.

- the image and text prompt are processed by the processor, converting them into tensors that the model can work with. The return_tensors='pt'  argument ensures that the output is in the form of PyTorch tensors.

- The generated output is a sequence of tokens, which are then decoded into a human-readable string using 'processor.decode'.

Gradio Interface

![image](https://github.com/user-attachments/assets/30838835-1882-4de8-8bca-083ca761aa4a)

- gr.Interface: This creates a web interface for the function, allowing users to upload images and receive captions.

- fn: the argument specifies the function to be called.

- inputs and outputs: Define the input as an image and the output as text.

- title and description: these arguments store text which is displayed on the front-end.

- launch(share=True): This launches the interface and provides a public link for sharing.

# Final Outcome
![image](https://github.com/user-attachments/assets/8b1c7414-89fe-4e77-96c9-febd38fc5b18)

![image](https://github.com/user-attachments/assets/eb3cce12-1a36-41fc-8ce2-56ef3bad7e1b)






