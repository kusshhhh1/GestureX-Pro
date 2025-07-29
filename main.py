import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import boto3

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)
ec2 = boto3.resource("ec2", region_name="ap-south-1")

def launch_instance():
    ec2.create_instances(
        ImageId="ami-0ed8adb8b013deb745",
        InstanceType="t2.micro",
        MinCount=1,
        MaxCount=1
    )
    print("EC2 Instance Launched")

def terminate_instances():
    for instance in ec2.instances.all():
        if instance.state['Name'] == 'running':
            instance.terminate()
            print("EC2 Instance Terminated")

while True:
    status, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)

        cv2.putText(img, f'Fingers: {fingers.count(1)}', (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        if fingers == [0, 1, 0, 0, 0]:
            os.system("start chrome")
        elif fingers == [0, 1, 1, 0, 0]:
            os.system("notepad")
        elif fingers == [0, 1, 1, 1, 0]:
            os.system("start spotify")
        elif fingers == [0, 1, 1, 1, 1]:
            launch_instance()
        elif fingers == [1, 1, 1, 1, 1]:
            terminate_instances()

    cv2.imshow("GestureX Cam", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
