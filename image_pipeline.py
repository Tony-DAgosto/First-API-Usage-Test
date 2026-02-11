from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def generate_response(pdf_path):
    file = client.files.create( #Tells OpenAI API to create a file object which holds the pdf file content
        file=open(pdf_path, "rb"), #Opens said file in read-binary (rb) mode
        purpose="user_data" #Tells API that the file is uploaded for the purpose of fufilling a user request
    )

    messages = [
        {"role": "system", "content": "You are a researcher who specializes in analyzing research papers."}, #Gives API base instructions to systm type, which is the AI's role in this convo
        {"role": "user", "content": [ {"type": "file", "file": {"file_id": file.id}}, #Tells API the input is a file type, and gives it the file id of the uploaded pdf
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
    client.files.delete(file.id) #Deletes the file from the API to save storage and tokens
    return result

if __name__ == "__main__":
    pdf_path = "./stat_research_paper.pdf" 
    answer = generate_response(pdf_path)

    with open("response_IP.txt", "w") as file:
        file.write(answer)
        file.write("\n")
        file.write("-- End of Response --\n")