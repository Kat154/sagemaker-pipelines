import time
import os
from sagemaker import get_execution_role, session
import boto3


sts_client = boto3.client('sts')
response = sts_client.assume_role(RoleArn='arn:aws:iam::471112501426:role/service-role/AmazonSageMaker-ExecutionRole-20240619T191533',RoleSessionName='sonia_itc_laptop')
print(f'response{response}')
region = boto3.Session().region_name
# breakpoint()
print(f"region:{region}\n\n ")
# role = get_execution_role()
sm_client = boto3.client('sagemaker', region_name=region)

import time
model_package_group_name = "scikit-iris-detector-" + str(round(time.time()))
model_package_group_input_dict = {
 "ModelPackageGroupName" : model_package_group_name,
 "ModelPackageGroupDescription" : "Sample model package group"
}
# breakpoint()
create_model_package_group_response = sm_client.create_model_package_group(**model_package_group_input_dict)
print('ModelPackageGroup Arn : {}'.format(create_model_package_group_response['ModelPackageGroupArn']))