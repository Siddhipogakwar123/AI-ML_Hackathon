# README: Google Lens Pro Max

---

## Overview

**Google Lens Pro Max** is an intelligent search system that combines image recognition and user prompts to provide relevant web search results. Users can upload an image along with a prompt to find similar objects or variations based on their needs. This project enhances search efficiency by integrating visual inputs with contextual queries.

### Example Use Cases

- **Input Image**: Red Bull can  
  **Prompt**: Show me other products in the same category  
  **Output**: Web search showing energy drinks  

- **Input Image**: A black hoodie with a Superman logo  
  **Prompt**: Show me t-shirts with the same design  
  **Output**: Web search showing black t-shirts with Superman logos  

---

## Folder Structure
1. main.py
2. requirement.txt


---

## How to Run the Application

### Step 1: Clone the Repository

git clone https://github.com/your-username/google-lens-pro-max.git
cd google-lens-pro-max/ml_hackathon

### Step 2: Install Dependencies

pip install -r requirements.txt

### Step 3: Configure API Keys
Update the search_web() function in main.py with your Tavily API key.

### Step 4: Run the Application
python main.py

---
## Tech Stack

- **Python 3.12.4 or higher**: The programming language used to implement the project.
- **Transformers Library**: A library for natural language processing, used to load and work with the model.
- **Pillow**: A Python Imaging Library (PIL) fork used for image processing tasks.
- **Tavily API**: A free-tier web search API used to perform web searches based on the image and user prompt.

---

## Our Solution

### Overview of the Repository

This project integrates image recognition, prompt-based query generation, and web search capabilities into one seamless system. The goal is to enhance the search experience by allowing
users to perform searches using both visual input (images) and contextual prompts. Traditional search engines rely primarily on text-based queries, which limits the ability to search 
effectively for visual content or contextual relationships between objects. Our solution addresses this limitation by combining multiple technologies.

### Function description

### `search_web(query)`
Performs a web search using the Tavily API based on the provided query and returns the search results, including titles, URLs, and related images.

### `display_results(results)`
Formats and prints the search results from the `search_web` function to the console, displaying the response time, titles, images (if available), and URLs in a structured format.

### `process_image_and_prompt(image_path, prompt)`
Processes an input image along with a user-defined prompt to extract relevant information using a machine learning model, returning a description or relevant details about the object in the image.

---

## Citations and References

1. **Moondream2 Model**:  
   The open-source **Moondream2** model by Vikhyat Kumar is employed to process the image and extract keywords.  
   - [https://github.com/vikhyat/moondream](https://github.com/vikhyat/moondream)
     
2. **Tavily API**:  
   Tavily API is used to perform web searches based on the processed image and prompt.  
   - [Tavily API Documentation](https://tavily.com/)

3. **Pillow (PIL)**:  
   The `Pillow` library, a fork of the original PIL, is used for image processing.  
   - [Pillow Documentation](https://pillow.readthedocs.io/)

4. **Transformers Library**:  
   Hugging Face’s `transformers` library is utilized for loading the Moondream2 model and tokenizer for prompt processing.  
   - [Transformers Documentation](https://huggingface.co/transformers/)

---

## Contributors

1. Ashutosh Tandon  
2. Himesh Chandrakar  
3. Siddhi Pogakwar

---
