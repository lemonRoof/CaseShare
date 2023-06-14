# CaseShare
![bbb](https://github.com/mphokekana/CaseShare/assets/111887473/6e2db378-2d1a-4c3a-ad8c-b52bbf2be34f)

### The Project

Welcome to CaseShare. CaseShare is a social platform that allows healthcare professionals to connect and collaborate.
Doctors and the whole healthcare team experience a lot of things in relation to their responsibilities. They experience 'aha' moments, ecstacy, and sometimes doubt. There are things they wished they knew; things they wish they would do differently if given another chance.
However, many of these experiences stay personal, or local. This is a problem because many healthcare professionals have something to share, but they don't have a platform to do that. As a result, their experiences stay personal, or local within an institution, and other colleagues is different institutions may find themselves reinventing the wheel.
We hereby propose CaseShare, a solution that allows healthcare professionals across different institutions to come together and collaborate. This tool will allow them to connect to each other, ask questions that other colleagues can answer, discuss cases, message each other, and so much more.
CaseShare will enable healthcare practitioners from different institutions to leverage each other’s knowledge, like the way StackOverflow helps developers.
This tool will not support patient transferring, and shall not be used to hold any patient’s data that can be traced back to them. All images shared should be de-identified for patient privacy.
We believe this project is relevant to the development of medicine and quality of care offered in Africa.

Link of deployed site:
https://caseshare.onrender.com/

BLOG POST 
Mpho Kekana: Linkedin 
https://www.linkedin.com/post/edit/7074120280264126464/

### Installation

To run the Case Share Website locally on your machine, follow these steps:

1. Clone this repository to your local machine using the following command:

https://github.com/mphokekana/CaseShare

2.  To create a virtual environment on a Linux system, you can follow these steps:

Open a terminal window.

Install the python3-venv package if it's not already installed. You can do this by running the following command:

sudo apt-get install python3-venv

Create a directory where you want to store your virtual environment. For example, you can create a directory called "myenv" by running:

mkdir myenv

Navigate into the directory using the cd command:

bash
Copy code
cd myenv
Create a new virtual environment by running the following command:

python3 -m venv env

This will create a new directory named "env" inside your "myenv" directory, which will contain the virtual environment.

Activate the virtual environment by running the activation script:

source env/bin/activate

After running this command, you should see that your prompt has changed to indicate that you are now inside the virtual environment.

You can now install Python packages and work within the virtual environment. Any packages you install will be isolated to this environment and won't interfere with your system-wide Python installation.

To deactivate the virtual environment and return to your normal shell, simply run the following command:

deactivate

Then install requirements from requirements.txt file

Update pip

pip install --upgrade pip

pip install -r requirements.txt

Then run code

Python -m flask run

Open your web browser and visit (http://localhost:5000) to access the CaseShare website.

### Usage
API's
1. Register your application: Most social media platforms require you to register your application and obtain API credentials (such as client ID and client secret) from their developer portal. This registration process ensures that you have permission to access their API and defines the scope of access granted to your application.

2. Authentication and authorization: Implement authentication and authorization mechanisms to allow users to connect their social media accounts to your website. This usually involves using OAuth or a similar protocol provided by the social media platform. Users will be prompted to authorize your application to access their data.

3. Obtain access tokens: Once a user authorizes your application, you'll receive an access token. This token is used to authenticate subsequent API requests on behalf of the user.

4. API requests: Use the social media platform's API endpoints to interact with their services. This can include actions like fetching user profiles, posting content, retrieving user feeds, commenting, liking, and more. Each social media platform will have its own set of API endpoints and documentation specifying how to make requests and handle responses.

5. Data processing and presentation: Retrieve the data from the API responses and process it as needed for your website. You may want to store certain data in your database, display it on user profiles, or incorporate it into your website's features.

6. Handle rate limits and errors: Social media APIs often have rate limits in place to prevent abuse. Ensure that you handle rate limit restrictions appropriately and handle any errors that may occur during API requests.

7. Stay updated: Social media platforms frequently update their APIs and may introduce changes or deprecate certain features. It's important to stay informed about any updates or announcements from the platform to keep your integration up to date.

### Contributing

We welcome contributions to enhance the functionality, features, and user experience of the Sisters Luxe Jewelry website. If you're interested in contributing, please follow the guidelines outlined in our Github.

### License

The CaseShare Website is open-source software licensed under the Github.
![aaa1](https://github.com/mphokekana/CaseShare/assets/111887473/bf7c998a-504b-4dc6-a615-06c7850cd6a9)

### Related projects

1. Doximity: Doximity is a professional networking platform designed for healthcare professionals. It allows doctors, nurses, and other healthcare providers to connect with colleagues, share knowledge, and collaborate on patient care.

2. Sermo: Sermo is a physician-only online community that enables doctors to discuss medical cases, seek advice, and share insights with their peers. It provides a secure and private platform for physicians to engage in professional discussions.

3. Figure 1: Figure 1 is a social platform for healthcare professionals that allows them to share and discuss medical images, such as X-rays, CT scans, and photographs. It enables collaboration and learning through visual case sharing.

4. PatientsLikeMe: PatientsLikeMe is a platform that focuses on connecting patients with similar medical conditions. It allows patients to share their experiences, track symptoms, and learn from each other's insights. It aims to foster support and provide a sense of community among individuals facing similar health challenges.

5. Inspire: Inspire is a healthcare social network that brings together patients, caregivers, and advocates. It provides a space for individuals to share their stories, seek support, and connect with others who are dealing with similar health conditions.

### The Context

This is a Portfolio Project concluding 9 months of Foundations in Software Engineering at Holberton School - ALX.
We were tasked to come up with a project we wanted to work on, and went through 3 rounds of reviews by our peers. The MVP was developed in 14 days from 19 May 2023 to 1 June 2023. 

### Team

- [Uwimana Lowami](https://github.com/Sonlowami) - Medical Imaging Student at University of Rwanda, and talented Software Engineer. He is a passionate learner, and wants to improve the quality of healthcare using technology.

- [Mpho Kekana](https://github.com/mphokekana) - Talented Software Engineer who lives in Johannesburg,South Africa.

### My Social Platform Website Deployment Journey
Introduction
Welcome to the README file of my social platform website deployment journey! This document aims to provide an emotional and sentimental account of the technical challenge I faced during the deployment phase of my Flask-based social platform website. It highlights the obstacles I encountered, the perseverance I exhibited, and the invaluable support I received from my peers that ultimately led to a successful deployment on render.com.

The Obstacle
As I embarked on the journey of deploying my social platform website, I encountered a significant hurdle that seemed insurmountable. Despite my meticulous planning and countless hours of debugging, I found myself unable to deploy the website successfully. It was disheartening to witness my hard work come to a standstill, as my vision of connecting individuals through this platform was put on hold.

Perseverance and Resilience
However, in the face of adversity, I refused to give up. I knew that challenges are an integral part of any technical project, and true growth lies in finding solutions to these roadblocks. With a renewed determination, I delved into online forums, documentation, and tutorials, hoping to find a breakthrough that would breathe life into my vision.

A Serendipitous Encounter
During this critical juncture, fate intervened in the form of a peer who had experienced a similar deployment challenge. Through the vast network of developers and the power of community, I connected with this peer, who generously shared their experience and knowledge. It was a serendipitous encounter that revitalized my hope and infused me with the belief that together, we could overcome any obstacle.

The Turning Point
As I engaged in a conversation with my newfound peer, they shared their successful deployment story on render.com. Their passion for helping others and their willingness to guide me through the intricacies of the deployment process were truly remarkable. Their words of encouragement instilled in me a sense of camaraderie and propelled me to take the leap of faith towards deploying my social platform on render.com.

Triumph and Gratitude
Thanks to the guidance and support of my peer, I successfully deployed my social platform website on render.com. The feeling of accomplishment and elation was indescribable. It was a testament to the power of collaboration, the strength of the developer community, and the resilience of the human spirit.

Conclusion
This README serves as a testament to the challenges faced, the resilience exhibited, and the triumph achieved during my social platform website deployment journey. It reflects the emotional rollercoaster that every developer experiences and showcases the value of seeking support from peers. I am forever grateful to the developer community for fostering an environment of learning, growth, and shared success.

Thank you for taking the time to read this heartfelt account. I hope it resonates with hiring managers who understand that the true measure of a developer extends beyond technical skills and encompasses the ability to overcome obstacles, collaborate effectively, and contribute meaningfully to the tech community.


