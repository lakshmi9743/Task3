import gradio as gr
from generator import MarkovChainTextGenerator  # Importing our class from generator.py

def generate_markov_text(corpus, state_size, num_words, seed_text):
    if not corpus.strip():
        return "⚠️ Please provide some training text first!"
    
    generator = MarkovChainTextGenerator(state_size=int(state_size))
    try:
        generator.train(corpus)
    except ValueError as e:
        return f"❌ Error: {str(e)}"
    
    seed = seed_text if seed_text.strip() else None
    result = generator.generate(num_words=int(num_words), seed_text=seed)
    return result

# Default placeholder text
default_text = "The quick brown fox jumps over the lazy dog. The lazy dog decided to sleep all day, while the quick brown fox kept running around the forest looking for food. When the fox found food, the dog woke up and wanted to share. Building interfaces with Gradio makes python applications incredibly fun and easy to share with others."

# Custom UI Styling
custom_css = """
#generate-btn {
    background: linear-gradient(135deg, #4F46E5 0%, #06B6D4 100%) !important; 
    color: white !important; 
    border: none !important;
}
#generate-btn:hover {
    transform: translateY(-1px); 
    box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
}
"""

with gr.Blocks(theme=gr.themes.Base(primary_hue="indigo", secondary_hue="cyan"), css=custom_css) as demo:
    
    gr.HTML("""
        <div style="text-align: center; margin-bottom: 24px; padding-top: 10px;">
            <h1 style="font-size: 2.5rem; font-weight: 800; background: linear-gradient(90deg, #4F46E5, #06B6D4); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 8px; font-family: sans-serif;">
                🎲 Markov Chain Playground
            </h1>
            <p style="font-size: 1.1rem; color: #6B7280; font-family: sans-serif;">
                Transform any text corpus into a generative probability model in seconds.
            </p>
        </div>
    """)
    
    with gr.Row():
        # Left Side: Training Input
        with gr.Column(scale=3):
            with gr.Group():
                gr.Markdown("### 📥 1. Feed the Model")
                corpus_input = gr.Textbox(
                    label="Source Text Corpus",
                    value=default_text,
                    placeholder="Paste a book chapter, lyrics, essays, or code here...",
                    lines=12
                )
        
        # Middle Column: Settings
        with gr.Column(scale=2):
            with gr.Group():
                gr.Markdown("### ⚙️ 2. Configure Settings")
                state_size_input = gr.Slider(
                    minimum=1, maximum=4, value=2, step=1, 
                    label="State Size (N-Gram)",
                    info="1 = Chaos & Fun, 2-3 = Coherent, 4 = Copy-paste heavy"
                )
                num_words_input = gr.Slider(
                    minimum=10, maximum=300, value=60, step=5, 
                    label="Word Budget",
                    info="Maximum length of the generated output"
                )
                seed_input = gr.Textbox(
                    label="Force Start Phrase (Optional)", 
                    placeholder="Enter starting words...",
                    lines=1
                )
            
            generate_btn = gr.Button("🔮 Generate New Text", elem_id="generate-btn", size="lg")
            
        # Right Side: Generation Output
        with gr.Column(scale=3):
            with gr.Group():
                gr.Markdown("### 📤 3. Generated Output")
                output_display = gr.Textbox(
                    label="Result",
                    placeholder="Click 'Generate New Text' to see the magic happen...",
                    lines=12,
                    interactive=False
                )

    generate_btn.click(
        fn=generate_markov_text,
        inputs=[corpus_input, state_size_input, num_words_input, seed_input],
        outputs=output_display
    )

if __name__ == "__main__":
    demo.launch(share=True)