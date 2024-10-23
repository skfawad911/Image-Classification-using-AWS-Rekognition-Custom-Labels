import boto3

client = boto3.client(
    'rekognition',
    aws_access_key_id=<access-key>,
    aws_secret_access_key=<secret-access>,
    region_name='ap-south-1'
)


# Define your model version ARN and the image details
model_version_arn = <model-arn>
bucket_name = <bucket-name>
image_name = <image-name-in-bucket>

# Call the detect_custom_labels method
response = client.detect_custom_labels(
    ProjectVersionArn=model_version_arn,
    Image={
        'S3Object': {
            'Bucket': bucket_name,
            'Name': image_name
        }
    },
    MinConfidence=60  # Adjust this as needed to get more results
)

# Print the detection results
print(response)
