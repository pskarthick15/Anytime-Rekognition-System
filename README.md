# ARS-An-AWS-powered-service
**Description of the application coded in python:**
ARS(Anytime Rekognition System) is a simple computer vision application that uses aws api calls to analyse input images based on the respective service entered by user. I have included 6 services(object detection,image moderation,face recognition, celebrity recognition,detecting a specific celebrity from an image of multiple celebrities,text detection in images)to be used by the application. 


**Folders and files information:**
The different images used to show the demo application are listed inside the this folder/repo. In addition to these,it also requires the users to create new users in their aws account(with permission grants to AWS Rekognition services) and then attach their credentials.csv file with this folder which is used to store the credentials of the users created and give access to the aws rekognition services so that it could be used to make the desired api calls to aws rekognition.This is done by using the boto3 library of python. The folder/repo also has another folder called Outputs that has 6 screenshots of outputs taken after executing the application code in Visual studio code(for all the 6 services that the application provides to the user).
The application code is in the rekognition.py file of this folder/repo.
