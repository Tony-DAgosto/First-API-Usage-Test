from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def generate_response(user_prompt):

    messages = [
        {"role": "system", "content": "You are a kind, old grandmother who loves to teach young people your family recipes in a gentle and nurturing manner."},
        {"role": "user", "content": user_prompt}
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=.95,
        max_tokens=300,
    )

    result = response.choices[0].message.content
    return result

if __name__ == "__main__":
    prompt = "What is your chocolate chip cookie recipe?"
    answer = generate_response(prompt)

    with open("response.txt", "w") as file:
        file.write(answer)
        file.write("\n")
        file.write("-- End of Response --\n")