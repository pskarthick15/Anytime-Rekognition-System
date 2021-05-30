import csv 
import boto3
import cv2
import numpy as np
from colorama import Fore, Back, Style
print(Fore.CYAN + "Welcome to anytime_rekog demo service\nWe are glad to inform you that we provide services in computer vision features")
print(Style.RESET_ALL)

print(Fore.YELLOW+"Please choose from the below demo services provided by us:\n1. Object and scene detection\n2. Image moderation\n3. Facial analysis\n4. Celebrity recognition\n5. Multiple celebrity recognition\n6. Text analysis")
print(Style.RESET_ALL)
val = input("Enter your desired option")
if val=='1':
    #Object and scene detection
    with open('credentials.csv','r') as input:
        next(input)
        reader=csv.reader(input)
        for line in reader:
            access_key_id=line[2]
            secret_access_key= line[3]

    photo='airplane.jpg'
    #Convert to base 64 encoding
    client=boto3.client('rekognition', region_name='ap-south-1',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)

    with open(photo,'rb') as source_image:
        source_bytes=source_image.read()

    response=client.detect_labels(Image={'Bytes':source_bytes},MaxLabels=2,MinConfidence=95)
    print(Fore.MAGENTA+"We have used an airplane that is to be detected by aws rekognition. Lets see what it detects!")
    print(Style.RESET_ALL)
    image = cv2.imread('airplane.jpg')
    window_name = 'Rekognition Image'
    imS = cv2.resize(image, (960, 540))
    cv2.imshow(window_name,imS)
    cv2.waitKey(7000)
    print("The 2 best predicted labels for your object are: \n",response['Labels'][0]['Name']," with a confidence of ",response['Labels'][0]['Confidence'],end='\n')
    print(response['Labels'][1]['Name'],"with a confidence of ",response['Labels'][1]['Confidence'],end='\n')
    source_image.close() 
    
if val=='2':
    #Image moderation
    with open('credentials.csv','r') as input:
        next(input)
        reader=csv.reader(input)
        for line in reader:
            access_key_id=line[2]
            secret_access_key=line[3]

    photo='terrorist.jpg'
    #Convert to base 64 encoding
    client=boto3.client('rekognition', region_name='ap-south-1',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)


    with open(photo,'rb') as source_image:
        source_bytes=source_image.read()

    response=client.detect_moderation_labels(Image={'Bytes':source_bytes})
    print(Fore.MAGENTA+"We have used an image of a terrorist that is to be detected by aws rekognition. Lets see what it detects!")
    print(Style.RESET_ALL)
    image = cv2.imread('terrorist.jpg')
    window_name = 'Rekognition Image'
    imS = cv2.resize(image, (960, 540))
    cv2.imshow(window_name,imS)
    cv2.waitKey(7000)
    print("labels detected are:\n")
    print(response)
    source_image.close()

if val=='3':
    #Facial Analysis
    with open('credentials.csv','r') as input:
        next(input)
        reader=csv.reader(input)
        for line in reader:
            access_key_id=line[2]
            secret_access_key=line[3]

    photo='family.jpg'
    #Convert to base 64 encoding
    client=boto3.client('rekognition', region_name='ap-south-1',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)


    with open(photo,'rb') as source_image:
        source_bytes=source_image.read()

    response=client.detect_faces(Image={'Bytes':source_bytes},Attributes=['ALL'])
    print(Fore.MAGENTA+"We have used a family photo that has 4 members. Lets see what our aws rekognition detects!")
    print(Style.RESET_ALL)
    image = cv2.imread('family.jpg')
    window_name = 'Rekognition Image'
    imS = cv2.resize(image, (960, 540))
    cv2.imshow(window_name,imS)
    cv2.waitKey(7000)
    print("The information found from image analysis are:\n")
    #As multiple faces are detected attributes for each of them are to be displayed
    for key,value in response.items():
        if key=='FaceDetails':
            for people_att in value:
                print(people_att)
                print("================================================================================================================")
    source_image.close()


if val=='4':
    #Celebrity recognition
    with open('credentials.csv','r') as input:
        next(input)
        reader=csv.reader(input)
        for line in reader:
            access_key_id=line[2]
            secret_access_key=line[3]

    photo='Celeb.jpg'
    #Convert to base 64 encoding
    client=boto3.client('rekognition', region_name='ap-south-1',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)


    with open(photo,'rb') as source_image:
        source_bytes=source_image.read()

    response=client.recognize_celebrities(Image={'Bytes':source_bytes})
    print(Fore.MAGENTA+"We have given an input image as the image of Tamil actor Vijay. Lets see what our aws rekognition detects!")
    print(Style.RESET_ALL)
    image = cv2.imread('Celeb.jpg')
    window_name = 'Rekognition Image'
    imS = cv2.resize(image, (960, 540))
    cv2.imshow(window_name,imS)
    cv2.waitKey(7000)
    print("The celebrity information is as follows:\n")
    for key,value in response.items():
        if key=='CelebrityFaces':
            for people in value:
                print(people)
                print("================================================================================================================")
    source_image.close()

if val=='5':
    #multiple celebrity recognition
    with open('credentials.csv','r') as input:
        next(input)
        reader=csv.reader(input)
        for line in reader:
            access_key_id=line[2]
            secret_access_key=line[3]

    photo_ip='Vijay_actor.jpg'
    photo_op='Celeb.jpg'
    #Convert to base 64 encoding
    client=boto3.client('rekognition', region_name='ap-south-1',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)


    with open(photo_ip,'rb') as source_image:
        source_bytes=source_image.read()
    with open(photo_op,'rb') as target_image:
        target_bytes=target_image.read()

    response=client.compare_faces(SourceImage={'Bytes':source_bytes},TargetImage={'Bytes':target_bytes})
    print(Fore.MAGENTA+"We have given an input image of celebrities photo having 3 stars. Vijay, MS Dhoni and cricketer K. Srikanth.Then we have tried to match the face of actor Vijay. Lets see what aws detects!")
    print(Style.RESET_ALL)
    image = cv2.imread('Vijay_actor.jpg')
    image1 = cv2.imread('Celeb.jpg')
    window_name = 'Rekognition Image'
    imS = cv2.resize(image, (960, 540))
    imS1 = cv2.resize(image1, (960, 540))
    Hori = np.concatenate((imS, imS1), axis=1)
    imS2 = cv2.resize(Hori, (960, 540))
    cv2.imshow(window_name,imS2)
    cv2.waitKey(7000)
    print("The matched and unmatched face details are:\n")
    for key,value in response.items():
        if key in ('FaceMatches','UnmatchedFaces'):
            print(key)
            for att in value:
                print(att)
            print("================================================================================================================")
    source_image.close()
    target_image.close()

if val=='6':
    #Text analysis
    with open('credentials.csv','r') as input:
        next(input)
        reader=csv.reader(input)
        for line in reader:
            access_key_id=line[2]
            secret_access_key=line[3]
    photo='msd_quotes1.jpg'
    #Convert to base 64 encoding
    client=boto3.client('rekognition', region_name='ap-south-1',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)


    with open(photo,'rb') as source_image:
        source_bytes=source_image.read()

    response=client.detect_text(Image={'Bytes':source_bytes})
    print(Fore.MAGENTA+"We have giiven a famous quote for aws to detect. It is DEFINITELY NOT\nLEGENDS NEVER RETIRED\n Lets see if aws detects this!")
    print(Style.RESET_ALL)
    image = cv2.imread('msd_quotes1.jpg')
    window_name = 'Rekognition Image'
    imS = cv2.resize(image, (960, 540))
    cv2.imshow(window_name,imS)
    cv2.waitKey(7000)
    print("Texts detected in the image are:\n")
    print(response)
    source_image.close()

print("Thanks for using our demo computer vision application. Hope to see you with our future projects as well!!!")
