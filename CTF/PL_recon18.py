import wget

for i in range(0,2):
    url = f'https://github.com/hackycorp/repo0a/blob/master/TEST{i}.txt'
    img=wget.download(url)
    print(f'img downloaded')
