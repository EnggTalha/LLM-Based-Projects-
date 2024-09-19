import openai
import os

# Set your API key (You can replace 'your-api-key' with your actual key)
api_key = "your openai key"  # Replace with your actual OpenAI API key

# Set up the OpenAI API key (ensure this is securely handled in a production environment)
openai.api_key = api_key 
# or os.getenv("OPENAI_API_KEY")

def generate_response(prompt):
    try:
        # Call the OpenAI API to generate a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Using the ChatCompletion model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    prompt = "What is the capital of France?"
    response = generate_response(prompt)
    print(response)
