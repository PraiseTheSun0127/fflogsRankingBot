import requests,json,sys
from conf import loadConf

'''

fflogsでzoneが保持するencounterを返却する
凍結されているコンテンツは取得しない

parm:zoneName fflogs上ではzoneと定義されているが、コンテンツ(例：絶バハムート討滅戦)
　　　　　　　　やレイドダンジョン(希望の園エデン:共鳴編)のことである
return:encountersList コンテンツのボス名などを保持するリスト（json形式）

'''

def getZone(zoneName):

    api_key = loadConf.fflogsTokenLoad()

    url = 'https://www.fflogs.com:443/v1/zones?api_key='+api_key

    res = requests.get(url)

    zoneLists = json.loads(res.text)

    for zone in zoneLists:
        
        encounterList = getEncounters(zone,zoneName)

        if encounterList is None:

            continue
        
        else:

            return encounterList['encounters']

    return None

def getEncounters(zone,zoneName):

    if bool(zone['frozen'] == False):

        if (zone['name'] == zoneName):

            return zone

if __name__ == "__main__":
    
    id = getZone("Eden's Verse")

    print(id)
