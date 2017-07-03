import requests

BASE_URL = "https://api.instagram.com/v1/"
ACCESS_TOKEN = "1710907001.dfca125.4ebb054d26db41e380c1581ac7445cac"

def my_info():
    requested_url = (BASE_URL +"users/self/?access_token=%s") %(ACCESS_TOKEN)
    print "Requested url:%s" %(requested_url)
    access_my_info = requests.get(requested_url).json()
    print access_my_info


my_info()


