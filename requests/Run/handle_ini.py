#conding = utf-8
'''
封装方法：通过configparser库读取配置文件server.ini文件
'''
import configparser
import os
base_path = os.getcwd()
latest_path = os.path.dirname(base_path)

class HandleIni:
    def get_file_ini(self):
        '''
        :return: 返回读取的文件对象，用于后续调用做准备
        '''
        file_path = latest_path+"/Config/server.ini"
        #定义configparser对象
        cg = configparser.ConfigParser()
        #读取文件，增加encoding参数是为了解决读取内容为汉字时的乱码问题
        cg.read(file_path,encoding='utf-8')
        return cg

    def get_ini_value(self,key,option=None):
        '''
        :param key: 传入需要读取的字段，如：url,username
        :param option: 传入读取模块的[]中的值
        :return: 返回配置文件中对应字段的值
        '''
        #获取文件下server模块下url的值
        data = self.get_file_ini().get(option,key)
        return data
handlini = HandleIni()

if __name__ == '__main__':
    handleini=HandleIni()
    print(handleini.get_ini_value(option='server',key='username'))

    '''
    server.ini文件中的内容为：
    [server]
    url = https://www.imooc.com
    username = 测试
    password = testpassword
    '''


