# flask-apis-practice

This are just APIs, No Frontend is made for this. But Swagger UI is linked to use.
It can send mail to only registered user in mailgun sandbox.
Redis instance is created in Render.com.
Database instance is hosted in Elephant SQL tiny turtle plan.
As rq and redis is used inside project it need background run along side server run hence it will run in docker or cloud only.
I ran it locally in docker using following commands:
First run background for email APIs: docker run -w /app your-image-name sh -c "rq worker -u <Your Redis URL> emails"
Now run the main app: docker run -p 5000:5000 your-image-name sh -c "flask run --host 0.0.0.0"
