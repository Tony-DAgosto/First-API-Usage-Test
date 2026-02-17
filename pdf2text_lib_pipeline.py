from openai import OpenAI
from dotenv import load_dotenv
from pypdf import PdfReader

load_dotenv()

client = OpenAI()

desiredPdfPath = "./" + "stat_research_paper.pdf" #pdf path you want to be analyzed

#instantiates a pdf reader object which can take a pdf file parameter and extracts its content
reader = PdfReader(desiredPdfPath)

#instantiates a page object which tells the reader object to extract the first page of content from the pdf
page = reader.pages[0]

#instantiates a text variable which tells the page object to extract the text content from the page and store it as a string in the text variable
text = page.extract_text()

def generate_response(user_prompt):

    messages = [
        {"role": "system", "content": "You are a researcher who specializes in analyzing research papers."},
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
    #creates the prompt to send to the API, can be altered for whatever the user wants to ask about the pdf content, then adds the actual pdf content to be analyzed to the end of the prompt
    prompt = "Give me a concise, informative summary of the following research paper: \n\n" + text
    answer = generate_response(prompt)

    with open("response_pdf2txt.txt", "w") as file:
        file.write(answer)
        file.write("\n")
        file.write("-- End of Response --\n")