# DOCKER-CHATOPENAI
Dockerize OPENAI Gradio Chat


Please sign up for OpenAI Developer account at https://platform.openai.com/docs/overview use your gmail account.

Please get API-KEY from https://platform.openai.com/settings/organization/api-keys open an account and get an apikey. "Free for limited time"

***please set up an .env file in your code folder to place the api key***

place your api key inside .env file inside the quotation.      OPENAI_API_KEY= "input your api key"



Gradio app Chat with OpenAI

Please download and set up docker desktop WINDOW,MAC OS,LINUX.

Please make sure Docker desktop is open ready to build Docker images.

In CDM or Terminal of your code file

CD open1

run command:

docker build -t gradio-chat-app .

docker run -e OPENAI_API_KEY=your_api_key_here -p 7860:7860 gradio-chat-app

![Screenshot 2025-03-06 233339](https://github.com/user-attachments/assets/9dce9e55-9c3d-4b39-85b8-b6618f240178)

