---
title: 'GenAI and Image Segmentation to spice up Presentations'
date: 2024-02-22T12:00:00+00:00
draft: true
cover:
  image: "slide_with_image.png"
  alt: "slide with image"
  caption: "slide with image"
tags: 
  - GenAI
  - productivity
  - presentations
---


I have been a satisfied user of generative image models such as stable diffusion, Midjourney and DALL·E 2 for over one year now. Admittedly, around 2016 or 2017, when the outputs of Generative Adversarial Networks (GANs) looked super pixelated and weird at times[^ganexample], I did not get the appeal. Especially when compared with discriminative models that were more efficient and performed way better for sentiment classification and so on.

However, like many people, I realized the great potential of generative approaches at the latest after Midjourney V3 and V4 were launched at the end of 2022.
While I mainly used these models to create images of imaginary landscapes and futuristic cityscapes, I have learned to appreciate them for more productive uses.

## Choosing the GenAI model

While **Midjourney** often provides more aesthetic (cooler) images with very diverse art styles, I found **DALL·E 2** from OpenAI to be a lot more reliable in following the given instructions for my use cases (the difference is smaller with Midjourney V6).
This is doubly important to quickly create images that are supposed to express a very specific idea or concept. 
As added benefit, it can, at least semi-reliably, incorporate text into the images .
While it might require a few tries, it generally seems to work.

## Example Use Case: 
For example, the following images were created with variants of the following prompt. While we can argue about the artistic value, it highlights how slides can be refined with little work, while avoding use of the typical pictograms or powerpoint templates:

**Prompt**

> *Create the image of a futuristic insurance building. It has glass walls. In the inside can be seen a large digital brain that represents an AI that enhances the decisions of the firm. The interior should look modern and cozy, as is typical for a modern tech company. Perspective from outside looking in. On the top of the building is a sign that says "Super Insurance". Make sure that it is a perspective from outside overlooking the whole building.*

**Generated images**
{{< images-side-by-side "futuristic_insurance_building_1.png" "Paris" "futuristic_insurance_building_2.png" "Rome" >}}

## Removing the background

To effectively use these images in a presentation, we typically want to remove the background. 
While this might be trivial for an experienced photoshop user, I never really got into that.
However, I found **[Segment Anything](https://segment-anything.com/)** which **Meta** open sourced recently really works wonders for exactly this use case. 
For me, it really opened up a bit more creative space when it comes to giving presentations more visual appeal.
In addition, since it gives so much control over the images, it possibly allows replacing more bullet points with expressive and straight to the point pictures.

### Prompting with segmentation in mind

It pays off to keep in mind that you want to segment the image later on already when writing the prompt.
Sometimes the task can be simplified drastically by specifying stuff like: `XYZ in front of white background`

### Using Segment Anything

The UI that Meta AI provides for the demo already seems to be sufficient for the use cases I am thinking about.
However, since this demo may not be used for commercial purposes, I hope that a mature web app is created soon.
This [hugging face space](https://huggingface.co/spaces/Xenova/segment-anything-web) also provides the model but the usability is comparable yet.
I am assuming that this functionality will be integrated into a variety of web apps that provide image editing services rather soon.

This image shows the positive (green) and negative (red) markers that you can use to mark the outline of the object.
Due to the pattern recognition embedded into the model, in many cases only few markers are even necessary.

{{< image-resize src="segment_anything_workflow.png" alt="slide with image" width="70%" >}}

**Cropped Image on Presentation Slide**
{{< image-resize src="slide_with_image.png" alt="slide with image" width="70%" >}}

# Links
[^ganexample]: https://blog.research.google/2017/04/teaching-machines-to-draw.html?m=1

