#coding:utf-8
import redis

if __name__ == '__main__':
    try:
        rs=redis.Redis(host='localhost',port=6379,db=0,decode_responses=True)
    except Exception as e:
        print(e)
    rs.set('food','fuit')
    rs.mset({'name':'Marry','cu':'pumk'})
    print(rs.strlen('name'))
