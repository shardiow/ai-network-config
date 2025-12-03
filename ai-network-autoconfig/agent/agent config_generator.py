import openai

def generate_config(vendor, intent):
    prompt = f"""
    You are a network engineer. Generate a full production-grade 
    {vendor} network configuration based on this intent:

    {intent}

    Follow best practices and ensure syntax accuracy.
    """

    response = openai.ChatCompletion.create(
        model="gpt-5.1",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]
