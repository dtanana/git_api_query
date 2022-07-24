import requests
from urllib.parse import urlparse
#using request to faciltate quicker release of product
#using urlparse to get good info from the url
#seperating the commands in to have cleaner code

#test data for building

base_url = 'https://api.github.com/repos/'


#function to grab the releases endpoint data from the repo

def releases_request(user , repo , token):
    if token == '':
        git_token = ''
    else:
        git_token = f'-H "Authorization: token {token}"'
    #pul repsonse and the return the name and tag for the
    response = requests.get(base_url + f'{user}/{repo}/releases', git_token )
    res_json = response.json()
    #catch an edge case that user doesn't use releases
    if not res_json:
        res_ret = ['Error:', "No Pull Releases in Repo", response.status_code]
        return res_ret
    #succesful response
    elif response.status_code  >= 200 and response.status_code  <=299:  
        i = 0
        res_ret = []
        #catch young repos that only have a single release
        while i < 3 and i < len(res_json) :
            elem_array = [res_json[i].get('name'), res_json[i].get('tag_name'),response.status_code]
            res_ret.append(elem_array)
            i += 1
        return res_ret
    #error from the client case, check what was sent
    elif response.status_code  >= 400 and response.status_code  <= 499: 
        res_ret = ['Error:', response.text, 4]
        return res_ret
    #catch server errors
    elif response.status_code  >= 500 and response.status_code  <= 599: 
        res_ret = ['Error:', response.text + "check status.github.com", 5]
        return res_ret

#function to grab the pulls endpoint data from the repo
def pulls_request(user , repo, token):
    if token == '':
        git_token = ''
    else:
        git_token = f'-H "Authorization: token {token}"'
    response = requests.get(base_url + f'{user}/{repo}/pulls', git_token) 
    res_json = response.json()
    #catch same errors as the releases function
    if not res_json:
        res_ret = ['Error:', "No Pull Requests in Repo", response.status_code]
        return res_ret
    elif response.status_code >= 200 and response.status_code  <=299:  
        i = 0
        res_ret = []
        while i < 3 and i < len(res_json) - 1 :
            elem_array = [res_json[i].get('title'), res_json[i].get('number'),'success']
            res_ret.append(elem_array)
            i += 1
        return res_ret
    elif response.status_code  >= 400 and response.status_code  <= 499: 
        res_ret = ['Error:', response.text, response.status_code]
        return res_ret
    elif response.status_code  >= 500 and response.status_code  <= 599: 
        res_ret = ['Error:', response.text + "check status.github.com", 'success']
        return res_ret

#function to normalize git urls
#trusting the user to supply a propper url to repo
def parse_git_url(git_url):
    git_urls = urlparse(git_url)
    path_string = git_urls.path + '/'
    path_array = path_string.split('/')
    if len(path_array) < 3:
       user , repo = "path_issuefdasf" , "path issue" 
       return
    user , repo = path_array[1] , path_array[2]
    return user, repo



