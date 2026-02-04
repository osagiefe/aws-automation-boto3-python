import json
import boto3
iam=boto3.resource('iam')
def list_all_iam_users():
    
    print('connecting to Iam')
    userslist=iam.users.all()
    #create list of users
    print('list of users')
   
    names=[i.name for i in userslist]
    print(names)
  
list_all_iam_users()
