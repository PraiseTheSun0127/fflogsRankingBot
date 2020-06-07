# iniを読み込む

# coding: utf-8
import configparser,os

iniPath = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

def discordTokenLoad():

    # configparserの宣言とiniファイルの読み込み
    config_ini = configparser.ConfigParser()
    
    # pwd+common/fflogBot.iniでフルパスになること
    config_ini.read(iniPath, encoding='UTF-8')

    # config,iniから値取得
    discordToken=config_ini['TOKEN']['DISCORD_TOKEN']

    return discordToken

def fflogsTokenLoad():

     # configparserの宣言とiniファイルの読み込み
    config_ini = configparser.ConfigParser()
    
    # pwd+common/fflogBot.iniでフルパスになること
    config_ini.read(iniPath, encoding='UTF-8')

    # config,iniから値取得
    discordToken=config_ini['TOKEN']['FFLOGS_TOKEN']

    return discordToken

if __name__ == "__main__":

    discord = discordTokenLoad()
