# Perceptify

<p align="center">
<img src="https://github.com/user-attachments/assets/74b90c01-30f9-400b-9e97-856649443762" height="500"/>
</p>

### **Project Overview**
This project provides a comprehensive solution to enhance safety and emotional well-being for the elderly in care facilities. Using IoT devices, computer vision, and AI, the system detects falls and monitors emotional states in real-time, sending automated alerts to caregivers via WhatsApp. By reducing the reliance on constant in-person monitoring, the system ensures timely intervention and improves resource allocation.

---

### **Problem Statement**
By 2050, one in six people worldwide will be over 65, and in Mexico, the population over 60 is expected to double by 2030. Limited caregiver availability (1 caregiver per 10 elderly individuals) heightens the risk of undetected mental health challenges and physical accidents. This project addresses these critical needs through real-time monitoring and automated alert systems.

---

### **Project Objectives**
- **Fall Detection**: Combines ESP32 sensors (accelerometer, gyroscope) with computer vision for accurate fall detection.
- **Emotional Health Monitoring**: Utilizes YOLO-based emotion recognition to identify potential mental health concerns.
- **Immediate Notifications**: Sends alerts to caregivers via WhatsApp for timely responses to detected events.

---

### **System Components**
1. **Hardware**:
   - **ESP32 Microcontroller**: Streams sensor data and video for processing.
   - **MPU6050 Accelerometer/Gyroscope**: Detects motion anomalies indicating falls.
   - **Camera**: Captures real-time video for emotion recognition.

2. **Software and Communication**:
   - **MQTT Protocol**: Transmits sensor data efficiently and securely.
   - **WebSockets**: Streams real-time video feeds to the processing server.
   - **Ubuntu Server**: Hosts AI models and processes data for monitoring and alerting.
   - **YOLO (Computer Vision)**: Detects falls and analyzes facial expressions for emotional health tracking.
   - **WhatsApp Integration**: Sends real-time alerts using `wwebjs` and `jspybridge`.

---

### **WhatsApp Notification System**
#### **Overview**
The system integrates **wwebjs** (a WhatsApp Web JavaScript API) to notify caregivers of falls or emotional distress. This ensures prompt delivery of critical alerts to designated contacts via WhatsApp, enabling caregivers to respond effectively, even when away from monitoring stations.

#### **How It Works**:
1. Detects falls or emotional distress events via sensors and computer vision.
2. Prepares alert details (e.g., timestamp, event type, images) on the server.
3. Uses `wwebjs` to send notifications through WhatsApp, including relevant text and images.

#### **Key Advantages**:
- Ensures timely alerts to caregivers.
- Provides event context with images and timestamps.
- Minimizes false alarms with intelligent event filtering.

---

### **Solution Architecture**
The system follows a modular IoT design:
1. **Sensing**: Collects motion and video data via ESP32 and sensors.
2. **Communication**: Transfers data through MQTT (sensor data) and WebSockets (video feed).
3. **Processing**: Analyzes data on the server using AI and sends alerts when necessary.

---

### **Image Showcase**
#### 1. **Fall Detection via Computer Vision**
   <img width="600" alt="Screenshot 2024-11-08 at 8 47 59 p m" src="https://github.com/user-attachments/assets/76b9b66c-8e2b-4763-9b25-a9688748d490">

   *Accurate identification of a simulated fall.*

#### 2. **Emotion Recognition with YOLO**
   <img width="600" alt="Screenshot 2024-11-08 at 8 50 33 p m" src="https://github.com/user-attachments/assets/f05458d6-f5a0-4d6a-a580-fba913f97045">

   *Analysis of facial expressions to detect emotional states.*

#### 3. **Sensor Data Visualization**
   <img width="600" alt="Screenshot 2024-11-08 at 8 51 48 p m" src="https://github.com/user-attachments/assets/75fd8edc-82ab-4f44-b54c-ef7ee5de131c">

   *Tracking motion data from the MPU6050 sensor.*

---

### **Expected Impact**
This system enhances elderly care by:
- Reducing risks associated with physical accidents and emotional distress.
- Enabling real-time insights for proactive intervention.
- Empowering caregivers with timely, actionable information.

---

### **Contributors**
This project was developed by:
- **Ximena Ortiz Gómez**
- **Luis Antonio Salinas González**
- **Pedro Luis Castañeda Pastelín**
- **Pablo Armando Mac Beath Milián**

---
