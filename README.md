This repository contains the completed project charter generation agent along with the chat interface, the agent is ready to create a project charter, the agent is integrated with the interface by using 
websockets api created by fastapi. The server.py holds the main file which initiates the agent. 
To set up the agent install the requirements.txt by "pip install -r requirements.txt"
The agent is dockerized and can also be run by uvicorn server:app --reload
Make necessary changes in the open ai api key in the utility.py
The chat interface can be run by installing all the necessary node modules by "npm install" or build a docker image by "docker build -t my-nextjs-app"
The interface could be run "docker run -p 3000:3000 my-nextjs-app" or "npm run dev"

