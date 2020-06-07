import requests,json,sys,collections as cl
from conf import loadConf
from datetime import datetime
from tabulate import tabulate
import prettytable

'''

fflogsAPIから取得したRankingとGNで受け取ったguildNameを突合させ、
指定したguildNameが各encounterで何位かを調べる（200位まで調べる)

parm:encountersList zoneが保持するencounters(json形式)
    :guildName GNコマンドから渡されたguildName

return:result 集計結果
    
'''

api_key = loadConf.fflogsTokenLoad()

def getRanking(encountersList,guildName):

    #One Dimensional
    odTable = [str(guildName)]

    header = ['']

    for encounters in encountersList:

        id = encounters['id']

        rank = checkRanking(id,guildName)

        odTable.append(str(rank))

        if header is None:

            header = [str(encounters['name'])]

        else:

            header.append(str(encounters['name']))

    tdTable = [odTable]

    result = prettytable.PrettyTable(header)

    for list in tdTable:

        result.add_row(list)

    return result

def checkRanking(id,guildName):

    ranking = 0

    for i in range(1,5) :

        url = 'https://www.fflogs.com:443/v1/rankings/encounter/'+str(id)+'?metric=speed&page='+str(i)+'&api_key='+api_key

        res = requests.get(url)

        rankingLists = json.loads(res.text)

        for list in rankingLists['rankings']:

            if list['guildName'] == guildName:

                return ranking + 1

            ranking = ranking + 1

    return 'None'

if __name__ == "__main__":

   json_open = open('test.json', 'r')

   json_load = json.load(json_open)
    
   result = getRanking(json_load,'guildName')

   print(result)