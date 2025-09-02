# AWS Project: EC2 Instance with IAM Role for Read-Only Access to S3 Bucket

## 1. Objective
The objective of this project is to demonstrate how an EC2 instance can access S3 buckets using an **IAM role with read-only permissions**, without the need for manual credentials.

---

## 2. Creating the IAM Role

1. An **IAM role** named `EC2-S3-Access-Role` was created.
2. A **custom read-only policy for S3** was attached, which includes permissions such as:
	- `s3:ListBucket`
	- `s3:GetObject`
3. This role was associated with the EC2 instance.

![custom policy](images/5.PNG)

![assigned IAM role](images/IAM.PNG)

---
## 3. Accessing the Instance
1. Connected to the instance using **SSH from the local machine**:
```bash
ssh -i "C:\Users\Home\Desktop\testAmazon\EC2\clave.pem" ec2-user@<Public-IP>
```
![opened from cmd](images/localmachine.PNG)

## 4. Testing Access to S3
1. Verified that AWS CLI is installed, and listed the buckets:
```bash
aws --version
```
```bash
aws s3 ls
```
![commands](images/8.PNG)

## 5. Creating and Manipulating Files within EC2
1. Created a text file:
```bash
echo "Hello AWS" > test.txt
```
2. Verified the content:
```bash
cat test.txt
```
![test.txt](images/9.PNG)

## 6. Conclusion
The EC2 instance can access S3 buckets without using manual credentials, thanks to the IAM role.
Best AWS practices were applied:
- Use of roles instead of static keys.
- Minimum necessary permissions (principle of least privilege).
This project demonstrates the complete flow of EC2 -> IAM -> S3 with read-only permissions, ideal for portfolio or academic practice.
