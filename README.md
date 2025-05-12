# English-Zamboanga Chavacano Translator

This repository hosts a fine-tuned machine translation model designed to translate English sentences into Zamboanga Chavacano—a Spanish-based creole language predominantly spoken in the Zamboanga Peninsula of the Philippines. The model is based on Facebook's `mbart-large-50-many-to-many-mmt` architecture and has been fine-tuned on a custom-curated parallel corpus.

## 🌐 Live Demo

Experience the translator in action: [Hugging Face Spaces Demo](https://huggingface.co/spaces/meowyboi/en-cbk-translator)
Alternatively, you can access the model directly in [Hugging Face](https://huggingface.co/meowyboi/mbart-large-50-en-cbk-finetuned) for more details or fine-tuning purposes.

## 📊 Model Overview

- **Base Model**: facebook/mbart-large-50-many-to-many-mmt
- **Source Language**: English
- **Target Language**: Zamboanga Chavacano
- **Training Data**:

  - 5,203 sentence pairs

- **Validation Data**:

  - 650 sentence pairs

- **Test Data**:

  - 651 sentence pairs

- **Sentence Length**: 2 to 20 words
- **Evaluation Metric**:

  - **BLEU Score**: 37.74 on the test set

## 📁 Repository Structure

- `app.py`: Main application script for running the translation model.
- `requirements.txt`: List of Python dependencies required to run the application.
- `.devcontainer/`: Configuration files for development container setup.
- `README.md`: Project documentation.

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed (preferably version 3.7 or higher). It's recommended to use a virtual environment to manage dependencies.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/meowyboii/chavacano_translator.git
   cd chavacano_translator
   ```

2. **Create and Activate Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Execute the `app.py` script through a streamlit command to start the translation application:

```bash
streamlit run app.py
```

This will launch the application, allowing you to input English sentences and receive their Zamboanga Chavacano translations.

## 🔧 Development and Customization

The model leverages the Hugging Face Transformers library. To fine-tune or modify the model:

1. **Prepare Your Dataset**:
   Ensure your dataset is in a parallel format with English and corresponding Zamboanga Chavacano sentences.

2. **Modify Training Scripts**:
   Adjust the training scripts to accommodate your dataset and desired training parameters.

3. **Train the Model**:
   Use the Hugging Face `Trainer` API or custom training loops to fine-tune the model.

4. **Evaluate Performance**:
   After training, evaluate the model using BLEU scores or other relevant metrics.

## 📄 License

This project is licensed under the [Apache License 2.0](LICENSE).
