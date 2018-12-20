# coding:utf-8

from __future__ import print_function
import boto3

lambda_client = boto3.client("lambda")
code_pipeline = boto3.client("codepipeline")

def lambda_handler(event, context):
    print(event)
    job_id = event["CodePipeline.job"]["id"]
    job = event["CodePipeline.job"]["data"]
    target_lambda = job["actionConfiguration"]["configuration"]["UserParameters"]
    artifact = job["inputArtifacts"][0]
    s3Location = artifact["location"]["s3Location"]
    # Deploy zipped lambda code
    response = lambda_client.update_function_code(
        FunctionName=target_lambda,
        S3Bucket=s3Location["bucketName"],
        S3Key=s3Location["objectKey"],
        Publish=True
    )
    # Notify the task result to codepipeline.
    code_pipeline.put_job_success_result(jobId=job_id)
    return response
