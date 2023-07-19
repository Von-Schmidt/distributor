import requests

nextcloud_url = 'x'
admin_username = 'x'
admin_password = 'x'

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
    requests.post(url, data=data, auth=(admin_username, admin_password), headers=headers, verify=False)

def add_user_to_group(username, group_id):
    url = f'{nextcloud_url}/ocs/v1.php/cloud/users/{username}/groups'
    data = {'groupid': group_id}
    requests.post(url, data=data, auth=(admin_username, admin_password), headers=headers, verify=False)

def delete_user(username):
    url = f'{nextcloud_url}/ocs/v1.php/cloud/users/{username}'
    requests.delete(url, auth=(admin_username, admin_password), headers=headers)
