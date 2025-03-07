# DOCKER-CHATOPENAI
Dockerize OPENAI Gradio Chat


Please sign up for OpenAI Developer account at https://platform.openai.com/docs/overview use your gmail account.

Please get API-KEY from https://platform.openai.com/settings/organization/api-keys open an account and get an apikey. "Free for limited time"

please set up an .env file in your code folder to place the api key

OPENAI_API_KEY= "input your api key"

create virtual environment file in your code folder

https://www.youtube.com/watch?v=yG9kmBQAtW4

python -m venv ai1

source ai1/Scripts/activate ("ai1" is the name of the file you can name it to your liking) use this for git ai1/Scripts/activate " use this for vscode"

python -m venv filename

source filename/Scripts/activate for git

filename/Scripts/activate for vscode terminal

create virtual-venv file in your vscode terminal or pycharm

for mac https://www.youtube.com/watch?v=Kg1Yvry_Ydk

cd my-project/ virtualenv venv

source venv/bin/activate

Gradio app Chat with Gemini

Please download and set up docker desktop WINDOW,MAC OS,LINUX

IN CDM or Terminal of your code file

CD open1

run command:

docker build -t gradio-chat-app .

docker run -e OPENAI_API_KEY=your_api_key_here -p 7860:7860 gradio-chat-app

![Screenshot 2025-03-06 233339](https://github.com/user-attachments/assets/9dce9e55-9c3d-4b39-85b8-b6618f240178)

