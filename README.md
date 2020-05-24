Smart Agriculture System based on IoT can monitor soil moisture and climatic conditions to grow and yield a good crop.
The farmer can also get the realtime weather forecasting data by using external platforms like Open Weather API.
Farmer is provided a mobile app using which he can monitor the temperature,humidity and soil moisture parameters along with weather forecasting details.
Based on all the parameters he can water his crop by controlling the motors using the mobile application.
Even if the farmer is not present near his crop he can water his crop by controlling the motors using the mobile application from anywhere.
 Here we are using the Online IoT simulator for getting the Temperature,Humidity and Soil
 
 for the Project development environment is very important for the success of project.
1. Create your GitHub Account, Install GIT tool in your PC/Laptop
2. Create the Project Scope in the Document Writer
3. Install Slack App, Join your team to the Project Channel
4. Choose the right IDE for Coding, Install the same in your Laptop
5. Go through the Project Management Dashboard

 The main goals of this project is as follows-
1.capability to address specific needs.
2. Automated control of motors in the field.
3. A simple user interface to be handeled even by the undereducated farmers.
4. Automated and simple to use method for processing of data.

Here are the steps to install and proceed with required softwares and platforms:-

Create IBM Cloud Account - The IBM® cloud platform combines platform as a service (PaaS) with infrastructure as a service (IaaS) to 
provide an integrated experience. The platform scales and supports both small development teams and organizations, and large enterprise 
businesses. Globally deployed across data centers around the world, the solution you build on IBM Cloud™ spins up fast and performs 
reliably in a tested and supported environment you can trust.

Install The Nodered Locally - Node-RED is built on Node.js, taking full advantage of its event-driven, non-blocking model. This makes 
it ideal to run at the edge of the network on low-cost hardware such as the Raspberry Pi as well as in the cloud.

 Create a device in IBM Watson IoT Platform - IBM IoT Connection Service integrates a bundled set of preselected services to form a 
 public, multitenant SaaS solution on the IBM Cloud framework. so create a device and give it name of your choice and generate device
 credentials like device token, device API key etc.
 
 Install Python IDE - Python is an interpreted, high-level, general-purpose programming language. It supports multiple programming
 paradigms, including structured (particularly, procedural), object-oriented, and functional programming. Python is often described as 
 a "batteries included" language due to its comprehensive standard library.

 Connect The IOT Simulator To Watson IOT Platform - Give the device credentials which you got while creating a Device in IBM IOT Platform  and connect to the Watson IOT simulator. through this simulator you will get temperature,humidity and object temperature values.
you can consider the object temperature value as the soil moisture value.

Configure The Nodered To Get The Data From IBM IOT Platform And Open Weather API :- 

Install The Required Nodes In Your Nodered - Install The Required Nodes In Your Nodered.

Make the required flow according to the conditions and goals of your system which you want to achieve.

Connect To Your IBM IOT Device To Get The Simulator Data.

Create An Account In Open Weather API And Configure Your Open Weather API Platform - OpenWeatherMap is an online service that provides
weather data.  It provides current weather data, forecasts and historical data to more than 2 million customer,it provides Weather 
Triggers API allows developers to set trigger conditions, and allows end-users to monitor trigger execution in real-time. 
you'll get the url from API platform in which you need to edit your city name and credentials to get the values of your particular area. 

Configure Your Nodered To Get The Weather Forecasting Data Using Http Requests.

Configure The Nodes To Display The Weather Parameters Which We Got Form IOT Simulator And Open Weather API In UI.

Building A Web App :- 

Configure The Nodes For Creating Buttons And Sending Commands To IOT Platform.

Configure Your Device To Receive The Data From The Web Application And Control Your Motors.

Write A Python Code To Subscribe To IBM IOT Platform And Get The Commands.

After all this we are required nodered dashboard which is a visualization dashboard so for that we need to install nodered dashboard
by the nodered url/ui and you can see the API values of humidity and soil moisture on dashboard and also percentage of humidity and 
soil moisture on a guage. also dashboard has 2 motor buttons for that you already written a program in paython using paycharm in which 
you need to give credentials of your device so, when you press the button on dashboard you'll get the satus on paycharm that wheather the
motor is ON or OFF.



 
 
 
 
 
 
 
 
 
 
 
