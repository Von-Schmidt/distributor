import requests

nextcloud_url = 'https://10.10.50.152'
admin_username = 'ncp'
admin_password = 'bambulka-666'

headers = {
    'OCS-APIRequest': 'true',
    'Content-Type': 'application/x-www-form-urlencoded'
}

def create_user(username, password, email):
    url = f'{nextcloud_url}/ocs/v1.php/cloud/users'
    data = {
        'userid': username,
        'password': password,
        'email': email
    }
    response = requests.post(url, data=data, auth=(admin_username, admin_password), headers=headers, verify=False)

    return response

def add_user_to_group(username, group_id):
    url = f'{nextcloud_url}/ocs/v1.php/cloud/users/{username}/groups'
    data = {'groupid': group_id}
    response = requests.post(url, data=data, auth=(admin_username, admin_password), headers=headers, verify=False)
    return response

user = input("input the user:")

response = create_user(user, 'b0b4anFAKTh0dn3r5d', 'jirinka@ecomsro.cz')
print(response.text)
response = add_user_to_group(user, 'forshare')
print(response.text)

