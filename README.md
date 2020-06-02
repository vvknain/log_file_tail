# log_file_tail
Python server streaming changes in log file real-time to react client


There are two parts to the project

1. python socket server
  - This project is using python 3.6.9 and Tornado framework
  - create a virtual environment before testing with python3
  - go to server directory
  - install the requirements (pip install -r requirements.txt)
  - start server (python server.py)
  - server will start on port 9000
  
2. React Client
  - it is configured using react-redux, redux for state management
  - go to socket_app directory
  - this app is created using npx create-react-app
  - a library is used to display scrolling feed
  - install the dependencies (npm install)
  - start the app (npm start) 
  - access the app at localhost:3000
  
  
3. A script fill_data.py is included in server directory with a data.txt file
  - run the script (python fill_data.py)
  - go to the client, you should see the content of the file getting displayed
  
  
Concurrency Stats:
  - tornado provides concurrency over 5000 connections, which makes it quite scalable
