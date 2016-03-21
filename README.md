This is just a basic prototype

Install all the required packages as specified in requirements.txt  

Steps to run 

1) Open terminal and type "python app.y"

2) Open browser and enter "http://localhost:5000/"

Functionality 

My prototype takes input from "HTML form" on the event of clicking "Build Graph" button . The data from form fields is then transferred to server using JSON . I have used comma separated input for the demonstration , which we can modify as per the project needs .  The server , written in python is now resposible for algorithm part . In my prototype server , process the input from " form field " , makes use of Pygal library and display interactive graphs as shown in the video attached . (currently I am  plotting the Yaxis values, which tells the % Increase in Population vs Time( in year) ) . 

Also "Clear" button clears the graph , when the button is clicked .
