import json
import boto3
iam=boto3.resource('iam')
print("enter user name")
user_name=input()
def delete_iam_users(user_name):
    
    print('connecting to Iam')
   
    try:
        
        iam.User(user_name).delete()
        print(f"iam user with  name '{user_name}' deleted successfully")
        return True
    
    except Exception as e:
        
        
        print("Couldn't delete user", user_name)
        return True

delete_iam_users(user_name)
