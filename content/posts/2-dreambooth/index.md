---
title: 'Experiments with Dreambooth'
date: 2024-02-24
draft: false
cover:
  image: "images/dreambooth-cover.png"
  alt: "futuristic dreambooth"
tags: 
  - GenAI
---

In mid of 2023 I stumbled upon [Dreambooth](https://dreambooth.github.io/).
Initially I only saw some posts about the paper but a really useful [huggingface space](https://huggingface.co/spaces/multimodalart/dreambooth-training) surfaced quickly after.
For one hackathon I thought it would be interesting to try out how well the face a person (in this case me) is persisted.

Out of interest I wanted to compare the approach I used a few months ago (StableDiffusion 1.5 based) with the results I get from using Midjourney.

# Dreambooth with Stable Diffusion
One kinda obvious drawback is by using StableDiffusion 1.5 we require quite specific prompts to create good results.

**Step 1**

The first step is to collect 15-30 images of the subject that should be captured by the neural network. 
In this case I am simply using 16 images of me.
They are quite diverse regarding perspective, illumination and clothes.
Better results are certainly possible from doing a whole photoshoot to get pictures from all perspectives (front, side, back).

