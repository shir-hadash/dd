import torch
from diffusers import StableDiffusionPipeline, StableVideoDiffusionPipeline
import imageio

PROMPT = "A cinematic shot of a futuristic city at sunset, flying cars, ultra realistic, 4K"

# שלב 1: יצירת תמונה מהטקסט
sd_pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5"
).to("cpu")
image = sd_pipe(PROMPT).images[0]

image.save("start_image.png")

# שלב 2: יצירת וידאו מהתמונה
svd_pipe = StableVideoDiffusionPipeline.from_pretrained(
    "stabilityai/stable-video-diffusion-img2vid-xt",
    torch_dtype=torch.float32
).to("cpu")

video_frames = svd_pipe(image, num_frames=16, height=576, width=1024).frames

imageio.mimsave("output.gif", video_frames, fps=8)
print("GIF saved as output.gif")
