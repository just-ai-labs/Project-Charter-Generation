# # This is the main file to initiate the Agent as a FastAPI WebSocket server

# # Importing the requirements
# import template
# import utility  # All the functionalities
# import variables  # All the variables
# import os
# import asyncio
# import time
# from fastapi import FastAPI, WebSocket
# from fastapi.responses import HTMLResponse

# app = FastAPI()

# # HTML for testing the WebSocket connection (optional)
# html = """
# <!DOCTYPE html>
# <html>
#     <head>
#         <title>WebSocket Test</title>
#     </head>
#     <body>
#         <h1>WebSocket Test</h1>
#         <textarea id="messageInput" cols="30" rows="10"></textarea><br>
#         <button id="sendButton">Send Message</button>
#         <ul id="messages"></ul>
#         <script>
#             var ws = new WebSocket("ws://localhost:8000/ws");
#             ws.onmessage = function(event) {
#                 var messages = document.getElementById("messages");
#                 var message = document.createElement("li");
#                 message.appendChild(document.createTextNode(event.data));
#                 messages.appendChild(message);
#             };
#             document.getElementById("sendButton").onclick = function() {
#                 var input = document.getElementById("messageInput");
#                 ws.send(input.value);
#                 input.value = '';
#             };
#         </script>
#     </body>
# </html>
# """

# @app.get("/")
# async def get():
#     return HTMLResponse(html)

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     print('WebSocket connection established')
    
#     # Initialize the agent
#     print('initialized')
#     request = f"Hi {utility.greeter()} <USER>, welcome to agent 1. I can help you with creating project charter and flowcharts."
#     variables.updates = request
#     await websocket.send_text(request)

#     while True:
#         # Wait for a message from the client
#         response = await websocket.receive_text()
#         print(f"Received message: {response}")
        
#         # Sentiment analysis of the user
#         sys_msg = '''
#             If the input expresses a greeting, such as "Hi," "Hello," or has a similar meaning, assign the context as greeting.
#             If the input is an inquiry, such as "How are you?" or any expression asking about someone's well-being, assign the context as enquiry.
#             If the input requests help related to starting a project or has a similar meaning, assign the context as project.
#             If the input is anything else than the mentioned above or if the input is an inquiry such as "what is your age?" or any expression asking the personal questions like age, salary or anything similar except the name, then assign the context as none.
#             If the input fits into more than one category, concatenate the respective contexts
#         '''
#         variables.user_responses.append(utility.ask_gpt(sys_msg, response))

#         # Process the response as per the original logic
#         variables.request_response.update({request: response})
        
#         # Determine the agent's response based on user input
#         if variables.user_responses[-1] == 'greeting':
#             request = 'How can I help you?'
#             variables.updates = request
#         elif variables.user_responses[-1] == 'greeting, enquiry' or variables.user_responses[-1] == 'enquiry':
#             request = "I'm doing great, Thank you. How can I help you?"
#             variables.updates = request
#         elif variables.user_responses[-1] == 'greeting, enquiry, project' or variables.user_responses[-1] == 'enquiry, project':
#             request = "I'm doing great, Thank you. Let's start the project. How do you want to provide the details?"
#             variables.updates = request
#             await websocket.send_text(request)  # Send the response to the client
#             break
#         elif variables.user_responses[-1] == 'project' or variables.user_responses[-1] == 'greeting, project':
#             request = "Okay let's start the project. How do you want to provide the details?"
#             variables.updates = request
#             await websocket.send_text(request)  # Send the response to the client
#             break
#         else:
#             request = 'I can only help with the project charter and flowchart generation'
#             variables.updates = "What you're asking might be beyond my scope, as I can assist primarily with project charters and flowchart generation"
        
#         # Send the updated agent response to the client
#         await websocket.send_text(request)


# # To run the FastAPI application, use the command:
# # uvicorn server:app --reload



# This is the main file to initiate the Agent as a FastAPI WebSocket server

# Importing the requirements
import template
import utility  # All the functionalities
import variables  # All the variables
import os
import time
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

# HTML for testing the WebSocket connection (optional)
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>WebSocket Test</title>
    </head>
    <body>
        <h1>WebSocket Test</h1>
        <textarea id="messageInput" cols="30" rows="10"></textarea><br>
        <button id="sendButton">Send Message</button>
        <ul id="messages"></ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById("messages");
                var message = document.createElement("li");
                message.appendChild(document.createTextNode(event.data));
                messages.appendChild(message);
            };
            document.getElementById("sendButton").onclick = function() {
                var input = document.getElementById("messageInput");
                ws.send(input.value);
                input.value = '';
            };
        </script>
    </body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print('WebSocket connection established')
    
    # Initialize the agent
    print('initialized')
    request = f"Hi {utility.greeter()} <USER>, welcome to agent 1. I can help you with creating project charter and flowcharts."
    variables.updates = request
    await websocket.send_text(request)

    while True:
        # Wait for a message from the client
        response = await websocket.receive_text()
        print(f"Received message: {response}")
        
        # Sentiment analysis of the user
        sys_msg = '''
            If the input expresses a greeting, such as "Hi," "Hello," or has a similar meaning, assign the context as greeting.
            If the input is an inquiry, such as "How are you?" or any expression asking about someone's well-being, assign the context as enquiry.
            If the input requests help related to starting a project or has a similar meaning, assign the context as project.
            If the input is anything else than the mentioned above or if the input is an inquiry such as "what is your age?" or any expression asking the personal questions like age, salary or anything similar except the name, then assign the context as none.
            If the input fits into more than one category, concatenate the respective contexts
        '''
        variables.user_responses.append(utility.ask_gpt(sys_msg, response))

        # Process the response as per the original logic
        variables.request_response.update({request: response})
        
        # Determine the agent's response based on user input
        if variables.user_responses[-1] == 'greeting':
            request = 'How can I help you?'
            variables.updates = request
        elif variables.user_responses[-1] == 'greeting, enquiry' or variables.user_responses[-1] == 'enquiry':
            request = "I'm doing great, Thank you. How can I help you?"
            variables.updates = request
        elif variables.user_responses[-1] == 'greeting, enquiry, project' or variables.user_responses[-1] == 'enquiry, project':
            request = "I'm doing great, Thank you. Let's start the project. How do you want to provide the details?"
            variables.updates = request
            await websocket.send_text(request)  # Send the response to the client
            break
        elif variables.user_responses[-1] == 'project' or variables.user_responses[-1] == 'greeting, project':
            request = "Okay let's start the project. How do you want to provide the details?Text or drop files"
            variables.updates = request
            await websocket.send_text(request)  # Send the response to the client
            break
        else:
            request = 'I can only help with the project charter and flowchart generation'
            variables.updates = "What you're asking might be beyond my scope, as I can assist primarily with project charters and flowchart generation"
        
        # Send the updated agent response to the client
        await websocket.send_text(request)

    # After the agent prompts the user to provide project details
    user_choice = await websocket.receive_text()  # Receive the user's choice from the client
    user_choice = int(user_choice)  # Convert the received message to an integer

    # Further responses of agent based on the user choice of providing information.
    if user_choice == 0:
        request = "Great choice. Kindly write the details here."
        variables.updates = request
        await websocket.send_text(request)  # Send the request to the client
        response = await websocket.receive_text()  # Wait for user to provide details
        variables.request_response.update({request: response})
        utility.record_response(response)
    else:
        request = "Great choice. Kindly drop here."
        variables.updates = request
        await websocket.send_text(request)  # Send the request to the client
        path1 = r'D:\DOWNLOADS\integration\project-docs-agent-branch-sandesh\uploads'
  # Path where files are uploaded
        ls = os.listdir(path1)  # List files in the upload directory
        path2 = ls[-1]  # Get the last uploaded file
        path = path1 + '\\' + path2  # Construct the full path to the file
        text = utility.option_2(path)  # Process the uploaded file
        variables.updates = request
        sys_msg = '''
        Find the punctuality and spacing in the given text and return the corrected in string format. Do not manipulate any information.
        '''
        text = utility.ask_gpt(sys_msg, text)  # Correct the text using the AI model
        utility.record_response(text.strip())  # Record the cleaned text

    # Analyze the template for missing fields
    missing_fields = await utility.text_analysis(template.template, websocket)

    print('req. loop begins')
    # Requirement loop begins:
    while len(missing_fields) > 0:
        missing_fields, end_convo = await utility.response_analysis(missing_fields, websocket)
        print(missing_fields)
        if end_convo == 1:
            break
        if len(missing_fields) == 1:
            missing_fields = utility.text_analysis(template.template)
        missing_fields = utility.text_analysis(missing_fields)

    print('req. loop ends')

    print('text extraction')
    charter_input = utility.text_extraction()  # Extract text for the project charter

    print('charter generation')
    charter = utility.generate_charter(charter_input)  # Generate the project charter
    charter.create_project_charter(rf"D:\DOWNLOADS\integration\project-docs-agent-branch-sandesh\uploads\{variables.project_id}.docx")
  # Save the charter to a file

    variables.complete = 1  # Mark the process as complete
    variables.updates = variables.complete
    await websocket.send_text("Project charter generation completed.")  # Notify the client
    print('completed')

    time.sleep(10)  # Pause before ending the program

    # except Exception as e:
    #     print(f"WebSocket error: {e}")
    #     break  # Break the loop on error to avoid infinite reconnection attempts

#uvicorn server:app --reload
