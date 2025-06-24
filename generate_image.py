# יש להתקין: pip install diffusers transformers accelerate torch safetensors

from diffusers import StableDiffusionXLPipeline
import torch

prompt = "A hyper-realistic portrait of a young woman, natural lighting, ultra detailed, 8K, photography"

pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

image = pipe(prompt=prompt).images[0]
image.save("output.png")
print("Image saved as output.png")
