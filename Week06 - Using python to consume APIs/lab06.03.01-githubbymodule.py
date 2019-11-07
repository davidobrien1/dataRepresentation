from github import Github

# remove the minus sign from the key

g = Github("37134fea34fc11b5bdc5e82ad894109b3d141674")

for repo in g.get_user().get_repos():
   print(repo.name)