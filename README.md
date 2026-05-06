# ProDigy InfoTech - Task 02: Image Generation with Pre-trained Models
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1qS2CN1DO0kplR5GKqMP14RdH_6yYIVJy?usp=sharing)
* live demo : https://9640cf10b1e1342b16.gradio.live

## 📌 Project Overvie
This project involves the implementation of a **Text-to-Image Generation** pipeline as part of my internship at **ProDigy InfoTech**. Using the **Stable Diffusion v1.5** model, I developed an interactive interface that allows users to generate high-quality, realistic images from textual descriptions.

## 🚀 Features
*   **Model:** Utilizes the pre-trained `runwayml/stable-diffusion-v1-5`.
*   **Performance:** Integrated **DPMSolverMultistepScheduler** for faster and sharper image generation.
*   **Interface:** Built a web-based UI using **Gradio** for seamless user interaction.
*   **Optimization:** Optimized for **CUDA-enabled GPUs** to ensure rapid inference.

## 🛠️ Tech Stack
*   **Language:** Python
*   **Libraries:** `diffusers`, `transformers`, `accelerate`, `torch`
*   **UI Framework:** `Gradio`
*   **Environment:** Google Colab (T4 GPU)

## 📸 Demo & Results

| Prompt | Generated Image |
| :--- | :--- |
| *A hyper-realistic of a panda with cinematic forest lighting.* | ![image](image.webp) |
| *A realistic commercial airplane flying through a clear blue sky.* | ![image(4)](airoplane.webp) |
| *A hyper-realistic macro photograph of a red rose with dew drops.* | ![image(3)](rose.webp) |


## ⚙️ How to Run
1.  Open the provided `.ipynb` notebook in **Google Colab**.
2.  Ensure the Runtime is set to **GPU** (Runtime > Change runtime type > T4 GPU).
3.  Install dependencies:
    ```bash
    pip install diffusers transformers accelerate gradio
    ```
4.  Run all cells to launch the Gradio interface.
5.  Enter your prompt and click **Submit**.

## 🧩 Challenges & Solutions
*   **Quality Issues:** Initial images were grainy. Fixed by switching the scheduler to `DPMSolverMultistepScheduler` and increasing `num_inference_steps` to 50.
*   **Connection Errors:** Encountered `SyntaxError: Unexpected token '<'` due to tunnel timeouts. Resolved by restarting the Gradio cell and using the local URL for stable recording.

---
Created by Mahalakshmi V | Internship Task-02 | ProDigy InfoTech
