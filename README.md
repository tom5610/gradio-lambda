# gradio-lambda
Demo gradio app on AWS Lambda


## Steps:
1. Create ECR 
```
aws ecr create-repository --repository-name gradio-demo --region us-west-2             
```

2. Install Serverless
```
npm i
```

3. Deploy from local machine 
```
IMAGE=$AWS_ACCOUNT_ID.dkr.ecr.us-west-2.amazonaws.com/$IMAGE_NAME:latest serverless deploy
```

4. Setup Github Action Secrets for automatic deployment

AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY_ID, IMAGE
5. Push code or manually trigger Github Action. The Public URL can be retrieved from https://github.com/neibla/gradio-lambda/runs/7449122633?check_suite_focus=true#step:7:17

For a Streamlit/Cloud Run template see https://github.com/neibla/streamlit-google-cloud-run
