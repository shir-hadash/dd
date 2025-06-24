import torch
from diffusers import StableVideoDiffusionPipeline
import imageio

PROMPT = "A cinematic shot of a futuristic city at sunset, flying cars, ultra realistic, 4K"

pipe = StableVideoDiffusionPipeline.from_pretrained(
    "stabilityai/stable-video-diffusion-img2vid",
    torch_dtype=torch.float16
).to("cuda" if torch.cuda.is_available() else "cpu")

video_frames = pipe(PROMPT, num_frames=16, height=576, width=1024).frames

imageio.mimsave("output.gif", video_frames, fps=8)
print("GIF saved as output.gif")
