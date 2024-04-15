# Django Chat Application

This is a real-time chat application built using Django Channels and Django Rest Framework (DRF). Users can register, log in, and join different chat rooms to communicate with others in real-time.

## Features

- Real-time messaging using websockets.
- User registration and authentication via DRF.
- Ability to  join and leave chat rooms.
- Group chat functionality within chat rooms.

## Technologies Used

- Django: Web framework for building the backend.
- Django Channels: Extends Django to handle Websockets and other asynchronous protocols.
- Django Rest Framework (DRF): For building RESTful APIs.
- SQLlite: Database management system.
- HTML/CSS/JavaScript: Frontend development.
- Bootstrap: CSS framework for styling.

## Setup Instructions

1. Clone the repository:

git clone https://github.com/your_username/django-chat-app.git
cd django-chat-app

arduino
Copy code

2. Create a virtual environment:
  venv\Scripts\activate
3. install requitements.txt
  pip install -r requirements.txt
   
4. Access the application in your web browser at `http://localhost:8000`.

## API Endpoints

- `signup/`: Register a new user.
- `accounts/login`: Log in and obtain an authentication token.
- `accounts/logout/`: Log out and invalidate the authentication token.
- `rooms/`: List of chat rooms.
- `/ws/chat/room/<room_id>/`: Websocket endpoint for real-time messaging in a chat room.



![1](https://github.com/Jekmen1/chat_app/assets/151436749/f75e6012-d147-48bf-9c24-8dd564943c42)



