# AWS-Full-Stack-Project
Following the AWS Fullstack Guide




# A) Reference:

The reference is the Full Stack application guide for AWS Documentation.

https://aws.amazon.com/getting-started/learning-path-full-stack-developer/






# B) Architicture:


Note, These links will not be working when I am done with the application.  
I will turn every thing off so that I do not get out of AWS Free Tier.

## B-1) AWS Amplify:

https://dev9463.d1pi9xfkfb20dm.amplifyapp.com/  

This is the link of the Frontend Application.  
It is just a Hello World Page.





## B-2) AWS-Labda Function:


This is a very basic lambda function.  
- Inputs (JSON):
	- firstName (String)
	- lastName (String)
- Output:
	- "Hello from Lambda, " + firstname + lastName
- Example:
	- Input:
```json
{
  "firstName": "Omar",
  "lastName": "Magdy"
}
```
	- Output:
```json
{
  "statusCode": 200,
  "body": "\"Hello from Lambda, Omar Magdy\""
}
```





## B-3) Amazon API Gateway:


- https://67nbvuy3t1.execute-api.us-east-2.amazonaws.com/dev  
	- Method: POST
	- Reuest Body: JSON
	- Inputs:
		- firstName (String)
		- lastName (String)

Example:  

Input:

```bash
curl --location --request POST 'https://67nbvuy3t1.execute-api.us-east-2.amazonaws.com/dev' \
--header 'Content-Type: application/json' \
--data-raw '{
    "firstName":"Omar",
    "lastName":"Magdy"
}'
```
I have also used a Postman collection to test the request.  

Output:


```bash
{
    "statusCode": 200,
    "body": "\"Hello from Lambda, Omar Magdy\""
}
```









