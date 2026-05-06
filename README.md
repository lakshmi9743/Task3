# Prodigy InfoTech - Task 04: Markov Chain Text Generator
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/https://colab.research.google.com/drive/1jvZ0zGchq_q-xdAp8uPJp2XcccmH-2a0?usp=sharing?)
* live demo : https://055016cc6ba3fa2f48.gradio.live

## 📌 Project Overview
This project involves the implementation of a **Markov Chain Text Generator** as part of my internship at **Prodigy InfoTech**. Using probability-based state transitions (n-grams), this system analyzes input training text to build a state-transition matrix, allowing users to automatically generate realistic, context-aware, or highly stylistic synthetic text based on user-defined prompts.

## 🚀 Features
* **Engine:** Custom-built $N$-gram word-level and character-level transition matrix.
* **Tunable Creativity:** Adjustable state-order ($N$) to slide between abstract randomness ($N=1$) and direct mimicry ($N \ge 3$).
* **Interface:** Built a web-based interactive UI using **Gradio** to instantly generate, adjust parameters, and view state pathways.
* **Sample Datasets:** Preloaded with distinct test corpora (Dr. Seuss, Corporate Jargon, Recipes, and Philosophy) to showcase diverse generation styles.

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** `numpy`, `pandas` (for transition matrices), `regex`
* **UI Framework:** `Gradio`
* **IDE/Environment:** VS Code (Visual Studio Code) & Google Colab (T4 GPU)

## 📸 Demo & Results

| Training Corpus | Prompt/Seed | Generated Output |
| :--- | :--- | :--- |
| *Dr. Seuss Rhymes* | `One fish` | *One fish, two fish, red fish, blue fish. Some are sad, and some are glad. And some are very, very bad! Why are they sad? Ask your dad.* |
| *Corporate Jargon* | `We need to` | *We need to synergize our core competencies to holistically circle back and optimize our deep-dive deliverables moving forward.* |
| *Recipe Books* | `Preheat the` | *Preheat the oven to 350 degrees. In a large bowl, whisk the baking pan together until the mixture resembles coarse crumbs.* |


## ⚙️ How to Run

### Option A: Using VS Code (Local Environment)
1. Clone the repository and open the project directory in **VS Code**:
   ```bash
   git clone [https://github.com/yourusername/PRODIGY_GA_04.git](https://github.com/yourusername/PRODIGY_GA_04.git)
   code PRODIGY_GA_04
