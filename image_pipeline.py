from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def generate_response(pdf_path):
    file = client.files.create(
        file=open(pdf_path, "rb"),
        purpose="user_data"
    )

    messages = [
        {"role": "system", "content": "You are a researcher who specializes in analyzing research papers."},
        {"role": "user", "content": [ {"type": "file", "file": {"file_id": file.id}},
                                     {"type": "text", "text": "Give me a concise, informative summary of the attached document. 500 words or less."}
    ]}
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=.6,
        max_tokens=1000,
    )

    result = response.choices[0].message.content
    client.files.delete(file.id)
    return result

if __name__ == "__main__":
    pdf_path = "./stat_research_paper.pdf" 
    answer = generate_response(pdf_path)

    with open("response_IP.txt", "w") as file:
        file.write(answer)
        file.write("\n")
        file.write("-- End of Response --\n")