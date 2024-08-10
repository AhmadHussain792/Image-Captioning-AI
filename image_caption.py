import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


def image_captioning(input_image: np.ndarray):
    raw_image = Image.fromarray(input_image).convert("RGB")

    text = "the image of"
    inputs = processor(images=raw_image, text=text, return_tensors='pt')

    outputs = model.generate(**inputs, min_length=5)

    caption = processor.decode(outputs[0], skip_special_tokens=True)

    return caption


iface = gr.Interface(
    fn=image_captioning,
    inputs=gr.Image(),
    outputs='text',
    title='Image Captioning using AI',
    description="Upload an image, and the AI model will\
     provide a suitable caption for your image! "
)


iface.launch(share=True)
