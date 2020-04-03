import requests
import os
import json

url = "https://sm.ms/api/upload"
file_list = os.listdir()
i=1
for each in file_list:
    print(i)
    i=i+1
    files = {}
    files['smfile'] = ('cat.jpg',open(each,'rb'),'image/png')
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}



    response = requests.post(url,files=files,headers=headers)
    try:
        with open('img_url.txt','a') as f:
            f.write(each+'      '+json.loads(response.text)['data']['url']+'\n')
        
    except:
        pass
print('--------------')


```
import requests
import os
import json

url = "https://sm.ms/api/upload"
file_list = os.listdir()
for each in file_list:
    
    files = {}
    files['smfile'] = (each,open(each,'rb'),'image/png')
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    f1 = open('img_url.txt','a')
    f2 = open('img_def.txt','a')
    response = requests.post(url,files=files,headers=headers)

    try:
        f1.write(each+'      '+json.loads(response.text)['data']['url']+'\n')    
    except:
        f2.write(each+'\n') 

    f1.close()
    f2.close()

```

