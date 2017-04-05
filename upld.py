from vk_requests import create_api
from requests import post,codes
import json

def CREATE(PATHS = [], TEXT = 'Test'):
    api = create_api(app_id = 5540525, login = '+79780728194',
                        password = 'Ctnnfhjdfhba1998',
                        scope = ['offline', 'photos', 'wall'],
                        api_version = '5.53')
    print(len(PATHS))
    if len(PATHS) > 0:
        upld_url = api.photos.getWallUploadServer()
        file = PATHS
        for i in range(len(file)):
            poste = post(upld_url['upload_url'],files={'photo': open(file[i], 'rb')})
            print(upld_url['upload_url'], '\n',poste.text)
            poste.status_code == codes.ok
            params = {'server': poste.json()['server'], 'photo': poste.json()['photo'], 'hash': poste.json()['hash']}
            wallphoto = api.photos.saveWallPhoto(**params)
            photoID.append(wallphoto[0]['id'])

        params = {'attachments' : [], 'message': TEXT}
        for i in range(len(photoID)):
            params['attachments'].append('photo' + '146897234_'+ str(photoID[i]))

        api.wall.post(**params)
    else:
        api.wall.post(message =(TEXT))
