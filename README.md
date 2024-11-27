# IoT-Based Elderly Care Monitoring System

<p align="center">
<img src="https://github.com/user-attachments/assets/74b90c01-30f9-400b-9e97-856649443762" height="500"/>
</p>

## Overview

This repository presents the final implementation of an Internet of Things (IoT) project aimed at monitoring the health and safety of elderly individuals in nursing homes. This solution combines IoT and Artificial Intelligence (AI) to deliver real-time monitoring of physical incidents (like falls) and emotional well-being through a network of connected devices and sensors. It is designed to improve the quality of care for elderly residents, especially in environments where human resources are scarce and personalized attention is limited.

## Motivation

The rapid growth of the elderly population demands urgent solutions to ensure their safety and quality of life. Statistics indicate that the number of people aged over 65 years is expected to increase significantly by 2050, raising challenges for caregiving. According to the World Health Organization, a significant proportion of elderly people face mental health issues such as depression and anxiety, which are often undetected due to a shortage of qualified caregivers. This project aims to leverage the Internet of Things (IoT) to develop a robust, scalable solution for continuous monitoring of elderly individuals in nursing homes.

## Problem Statement

There is a clear lack of personalized care for elderly individuals in nursing homes due to insufficient staffing. This shortage leads to undetected signs of mental health disorders and physical incidents that can harm the well-being of the elderly. In a typical nursing home, a single caregiver is often responsible for multiple residents, limiting their ability to monitor each person's health closely. As a result, the detection of conditions like anxiety, depression, and physical injuries such as falls may be delayed or overlooked.

Our project addresses this gap by developing an IoT-based monitoring system capable of identifying:
- **Falls**: One of the most common physical risks for elderly individuals.
- **Emotional Changes**: Detecting emotional distress based on facial expressions to help caregivers take timely action.


## Objectives

The primary objectives of this IoT solution are:
- To **detect falls** and provide immediate alerts to caregivers.
- To **analyze emotional states** using image processing and machine learning techniques.
- To enable **real-time monitoring** using connected devices, ensuring continuous care for the elderly.
- To provide a **mobile application** that facilitates quick access to alerts, notifications, and overall monitoring of the health status of elderly residents.



## Proposed Solution

### Description of the System

The proposed solution consists of a **fall and emotional monitoring system** for elderly individuals. It integrates a network of IoT devices such as accelerometers, cameras, and microcontrollers to monitor health events. The system uses AI techniques to process video feeds, detect falls, and assess the emotional state of elderly individuals. When an incident is detected, an alert is immediately sent to the assigned caregiver via a mobile application and WhatsApp messages.

The project includes the following core components:
- **IoT Sensors**: To monitor movement and detect potential incidents.
- **Camera**: Captures facial expressions for emotional analysis.
- **ESP32 Microcontroller**: Collects data from sensors and facilitates communication.
- **Server-Side AI Processing**: Analyses data from cameras and sensors.
- **Mobile Application**: Presents information to caregivers, including alerts, history, and live monitoring.


### Methodology and Architecture

The development followed an **iterative methodology**, focusing on testing and refining both hardware and software components. The key phases include:
1. **Requirements Analysis**: Defining functional requirements, such as fall detection and emotion monitoring.
2. **Architecture Design**: Designing the IoT architecture, defining publishers, subscribers, and brokers for efficient data transmission.
3. **Component Selection**: Choosing appropriate hardware, such as ESP32 and MPU6050, for its connectivity features and compatibility.
4. **System Development**:
   - **Sensor Integration**: Integrating accelerometers with ESP32 for fall detection.
   - **AI Integration**: Using models trained in **TensorFlow** and **YOLO** to process video feeds for emotion and fall detection.
   - **MQTT Protocol**: Implementing MQTT for lightweight, real-time data communication.
5. **Application Development**: Creating a mobile application in **Flutter** for data presentation and alert notifications.
6. **Experimental Validation**: Testing the solution under different conditions, refining accuracy, and minimizing false positives.

<p align="center">
<img height="400" alt="Screenshot 2024-11-27 at 12 31 49 p m" src="https://github.com/user-attachments/assets/267db647-5e11-4732-aa2d-181e35049322">
</p>

## System Components

### Hardware Components
- **ESP32 Microcontroller**: Processes sensor data and handles communication. Selected for its Wi-Fi and Bluetooth connectivity, making it ideal for IoT projects.
- **MPU6050 Accelerometer and Gyroscope**: Detects falls based on changes in acceleration and angular velocity.
- **Camera (Logitech C920 HD Pro)**: Captures video for emotional analysis.
- **Raspberry Pi**: Used for video streaming and additional processing capabilities.


### Software Tools and Languages
- **Arduino IDE**: Used to program the ESP32 microcontroller.
- **Python**: Implemented for data processing, machine learning model integration, and server-side AI.
- **Flutter**: Mobile application framework for presenting data and generating alerts.
- **OpenCV**: Used for image and video processing to analyze facial expressions.
- **TensorFlow & YOLO**: AI frameworks for training and deploying models for fall and emotion detection.
- **SQLAlchemy and PostgreSQL**: Used for data management, including logging incidents and maintaining an archive of detected events.
  
<p align="center">
<img width="541" alt="Screenshot 2024-11-27 at 12 33 52 p m" src="https://github.com/user-attachments/assets/9d8eafd3-1439-40a2-85b9-22cf73d23efd">
</p>

## System Features

### Real-Time Monitoring
- **Fall Detection**: The system detects falls using both the accelerometer and video analysis, ensuring high reliability.

<p align="center">
   <img height=400 src="https://github.com/user-attachments/assets/3688ed09-33be-400e-9fb6-1fa0291f9ba4" />
</p>

- **Emotion Analysis**: The camera captures facial expressions, which are analyzed to determine emotional states (e.g., happiness, sadness, surprise).

<p align="center">
<img width="437" alt="Screenshot 2024-11-27 at 12 34 51 p m" src="https://github.com/user-attachments/assets/ed7e33a9-781c-4b13-9a77-c670742fd12f">
<img width="700" alt="Screenshot 2024-11-27 at 12 37 58 p m" src="https://github.com/user-attachments/assets/d5be748b-d568-4ad1-a9bc-a5de4cf6c6d6">
</p>

- **Alert System**: Alerts are sent via WhatsApp and a mobile application to notify caregivers in real-time about any incidents or changes detected.

<p align="center">
<img width="181" alt="Screenshot 2024-11-27 at 12 37 29 p m" src="https://github.com/user-attachments/assets/991f220d-8761-43a4-921d-ea045a5624e5">
</p>


### Data Communication
- **MQTT**: Lightweight messaging protocol used for transmitting data between sensors and servers, ensuring efficient communication.
- **WebSockets**: Enables real-time two-way communication, particularly for streaming data.
- **HTTP**: Used for communication between the mobile app and the server for requests like retrieving alerts or accessing history.

### Mobile Application
The **mobile application** was developed using **Flutter** and provides caregivers with:
- A **real-time dashboard** showing the status of residents.
- **Notifications** for falls or emotional changes.
- **Graphs** and data visualizations of residents' emotional trends and incident history.

<p align="center">
<img height="400" src="https://github.com/user-attachments/assets/8716bebf-b0ac-4e95-a1b0-305a1ffa6c31"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="400" src="https://github.com/user-attachments/assets/37cedf43-cb26-4b54-a9d2-56ea7dbdf806"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="400" src="https://github.com/user-attachments/assets/49a3d0b0-47ac-4f0a-85c9-0e5eab03a423"/>
</p>

### Experimental Results and Metrics

#### Fall Detection Experiments
- In controlled environments, the system achieved a **fall detection rate of 87.5%** using accelerometer and camera data.
- Scenarios included different angles of falls and varying positions, demonstrating robustness across conditions.
- 
<p align="center">
<img width="583" alt="Screenshot 2024-11-27 at 12 50 17 p m" src="https://github.com/user-attachments/assets/76de7ffe-eb2a-4aab-9d68-8e67ac2d1022">
</p>

#### Emotion Detection Experiments
- The system detected emotions correctly **82.5%** of the time during validation experiments.
- The model was less accurate in distinguishing subtle emotional expressions, highlighting an area for future improvement.
  
<p align="center">
<img width="370" alt="Screenshot 2024-11-27 at 12 48 54 p m" src="https://github.com/user-attachments/assets/4e8dde05-e2b2-4f9b-b9ca-919b18d13a05">
</p>

### System Limitations and Future Improvements
- **Emotion Detection Accuracy**: The current system demonstrates an accuracy of around 62.5% for emotion detection, suggesting the need for further model training with more diverse data to improve robustness.
- **False Positives in Fall Detection**: During high-motion activities, the sensor sometimes misclassified actions as falls. Future improvements could include refining detection algorithms to minimize these false positives.
- **Scalability**: The architecture was designed to be modular, allowing for future integration of additional sensors or users to enhance its applicability in larger care centers.


## Project Impact

The IoT-Based Elderly Care Monitoring System aims to improve the quality of life for elderly residents in nursing homes by:
- **Reducing the caregiver workload** by automating the monitoring process.
- **Improving response times** to physical incidents or emotional distress.
- **Facilitating personalized care** through continuous data collection and analysis.

With further refinements, this system has the potential to become an essential tool for eldercare, offering peace of mind to both caregivers and families.

## Contributors

- **Pablo Armando Mac Beath Milián** - IRS
- **Ximena Ortiz Gómez** - IRS
- **Luis Antonio Salinas González** - ITC
- **Pedro Luis Castañeda Pastelín** - ITC

