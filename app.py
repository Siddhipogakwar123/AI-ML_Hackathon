from transformers import AutoModelForCausalLM, AutoTokenizer
import streamlit as st
from PIL import Image
import io 
# from tavily import TavilyClient

# Load the Moondream2 model
model_id = "vikhyatk/moondream2"
revision = "2024-08-26"
model = AutoModelForCausalLM.from_pretrained(
    model_id, trust_remote_code=True, revision=revision
)
tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

def search_web(query):
    """Search the web using Tavily API."""
    from tavily import TavilyClient
    client = TavilyClient(api_key="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")
    response = client.search(query, max_results=5, include_images=True)
    return response


def display_results(results):
    """Display the search results."""
    st.write(f"**Response Time:** {results['response_time']} seconds\n")
    st.write("### Top Search Results ###")

    for i, result in enumerate(results['results'], 1):
        st.write(f"**Result {i}:**")
        st.write(f"  - **Title:** {result.get('title', 'No Title')}")

        # if 'images' in result and result['images']:
        #     image_url = result['images'][0]
        #     st.image(image_url, caption="Related Image", use_column_width=True)
        # else:
        #     st.write("  - **Image:** No image available")

        st.write(f"  - **URL:** [{result['url']}]({result['url']})")
        st.write("-" * 40)  # Separator

def process_image_and_prompt(image, prompt):
    """Encode image and generate an answer from the prompt."""
    # No need to re-open the image; use it directly
    enc_image = model.encode_image(image)

    # Combine image information with user prompt
    question = f"{prompt}"
    answer = model.answer_question(enc_image, question, tokenizer)

    return answer.strip()

def main():
    st.title("AI-Powered Image Search")
    st.write("Upload an image and enter a prompt to generate search results.")

    # Image uploader
    uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

    # User prompt input
    prompt = st.text_input("Enter a prompt:")

    if uploaded_image and prompt:
        # Load image from uploaded byte stream
        image = Image.open(io.BytesIO(uploaded_image.read()))

        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Process the image and prompt to generate search keywords
        image_info = process_image_and_prompt(image, prompt)
        search_keywords = f"{image_info} {prompt}"

        st.write(f"**Generated Keywords:** {search_keywords}")

        # Perform the search
        results = search_web(search_keywords)
        display_results(results)

if __name__ == "__main__":
    main()
