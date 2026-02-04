import json
import boto3
iam=boto3.resource('iam')
print("enter user name")
user_name=input()
def create_iam_users(user_name):
    
    print('connecting to Iam')
   
    try:
        user = iam.create_user(UserName=user_name)
       
        print(f"iam user with name '{user}' created successfully")
        return True
    
    except Exception as e:
        
        
        print("Couldn't create user", user_name)
        return user

create_iam_users(user_name)
