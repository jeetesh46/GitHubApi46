import requests
import json

def github_fetch_data(user_id):

    response = {}
    repos_url = "https://api.github.com/users/{}/repos".format(user_id)
    repos_data = requests.get(repos_url)
    repos_json_data = json.loads(repos_data.text)

    if repos_data.status_code == 200:
        for data in repos_json_data:
            commit_url ="https://api.github.com/repos/{}/{}/commits".format(user_id, data['name'])
            commit_data = requests.get(commit_url)
            commit_json_data = json.loads(commit_data.text)
            response[data['name']] = len(commit_json_data)

    return response

if __name__ == '__main__':
    response = github_fetch_data("Varun2480")
    for key,value in response.items():
        output_message = "Repo: {} Number of commits: {}"
        print(output_message.format(key,value))