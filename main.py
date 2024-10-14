import requests
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image

# Step 1: Load the open-source model Moondream2
model_id = "vikhyatk/moondream2"
revision = "2024-08-26"
model = AutoModelForCausalLM.from_pretrained(
    model_id, trust_remote_code=True, revision=revision)
tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

def search_web(query):
    # api_key = "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"
    from tavily import TavilyClient
    client = TavilyClient(api_key="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")

    # Step 2. Executing a simple search query
    response = client.search(query,max_results=5,include_images=True)

    # Step 3. That's it! You've done a Tavily Search!
    return response



def display_results(results):
    print()
    print(f"**Response Time:** {results['response_time']} seconds\n")

    # Print each result in a structured format

    print("### Top Search Results ###")
    for i, result in enumerate(results['results'], 1):
         print(f"**Result {i}:**")
         print(f"  - **Title:** {result['title']}")
         if results['images']:
        # Select one image for each result based on the current index
             image_url = results['images'][min(i - 1, len(results['images']) - 1)]  # Ensures you don't go out of range
             print(f"  - **Image:** {image_url}")
         else:
             print("  - **Image:** No image available")

         print(f"  - **URL:** [{result['url']}]")
         print("-" * 40)  # Separator for clarity
         print("\n" + "=" * 60)  # Final separator



# Step 3: Process the image and prompt to extract information
def process_image_and_prompt(image_path, prompt):
    # Load and encode the image
    image = Image.open(image_path)
    enc_image = model.encode_image(image)

    # Combine image information with user prompt
    question = f"{prompt}"
    answer = model.answer_question(enc_image, question, tokenizer)

    # Return the answer (e.g., object description)
    return answer

# Testing
image_path = "<IMAGE-PATH>"  # Provide the path to your image
prompt = input("Enter input prompt : ")
print()

# Step 4: Extract image information and combine with prompt
image_info = process_image_and_prompt(image_path, prompt)

# Step 5: Use the extracted information as search keywords
search_keywords = f"{image_info} {prompt}"
print('Input image : ',image_info)
print('Input prompt : ',prompt)
print('Generated output : ')


result = search_web(search_keywords)
display_results(result)
