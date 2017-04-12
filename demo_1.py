#-*-coding:utf8-*-

'使用Python语言以GET方式调用REST API代码示例'
'text=待分析的文本'
'format=结果形式，xml(XML格式)，json(JSON格式)，conll(CONLL格式)，plain(简洁文本格式) 	'
'pattern=分析模式,ws(分词)，pos(词性标注)，ner(命名实体识别)，dp(依存句法分析)，srl(语义角色标注),all(全部任务)'

import urllib2

if __name__ == '__main__':
    url_get_base = 'http://ltpapi.voicecloud.cn/analysis/?'
    api_key = 'a1k4B879j4T0X8m6V9c1MgHSBbYAcXAHAirZYAJF'
    text = '今天很开心'
    format = 'plain'
    pattern = 'ws'
    result = urllib2.urlopen( "%sapi_key=%s&text=%s&format=%s&pattern=%s" % (url_get_base,api_key,text,format,pattern))
    content = result.read().decode('utf-8').strip()
    print content
