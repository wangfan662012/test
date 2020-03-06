# encoding: utf-8
import mysql
import mysql.connector as sql
import hashlib
import random
import requests
import time
import json


config = {
 "host": "rm-bp14z434pwpq512kw0o.mysql.rds.aliyuncs.com",
 "user": "juke_test3",
 "password": "rUnovNtAnzeaYGwE0eCn",
 "port": 3306,
 "database": "member_test3",
 "charset": "gb2312"
}
try:
    cnn = mysql.connector.connect(**config)
    print("connect success")
except mysql.connector.Error as e:
    print('connect fails!{}'.format(e))


def insert_member_no(number, member_no):
    try:
        code = create_md5()
        phone = random.choice(['139', '138', '131', '155', '150', '188']) + "".join(
            random.choice("0123456789") for i in range(8))
        cursor = cnn.cursor()
        sql_query = f"""insert into `member_test3`.`guid_member` 
        ( `CODE`, `MEMBER_NO`, `MEMBER_NAME`, `SHOP_NO`, `SHOP_NAME`, `MERCHANT_NO`, `MERCHANT_NAME`, `STATUS`, `JOB_NUM`, 
        `MOBILE`, `IMEI`, `EMAIL`, `NICK_NAME`, `AREA_CODE`, `AREA_NAME`, `PROVINCE_CODE`, `CITY_CODE`, `CITY_AREA_CODE`, 
        `ADDRESS`, `AGE`, `GENDER`, `PWD`, `ENCRYPTION_CODE`, `HEAD_ADDRESS`, `WORK_DATE`, `QCORD`, `NO_WX`, 
        `NO_WX_PERSONAL`, `UPDATE_ID`, `UPDATE_DATE`, `CREATE_ID`, `CREATE_DATE`, `REMARK4`, `REMARK3`, `REMARK2`, `REMARK`) 
        values 
        ( 'LJ_{code}', 'LJ_{member_no}', 'zhaozhao{number}', 
        'LJ_468bc95019424b94b65b38f0ed895b67', '留客接口1', 'd6acf1e2e75d4027a8204b1c670aaa31', '留客接口', 'NORMAL', null, 
        '{phone}', null, null, null, '4', '华北地区', null, null, null, null, '0', 'MALE', 
        'f77359af77d10649707879f71f360f3b', '3', null, '2019-05-27 16:07:27', null, 'aaaaaa', null, null, null, 'api-os', 
        '2019-05-27 16:07:27', null, null, null, null);"""
        print("insert sql=========>", sql_query)
        cursor.execute(sql_query)
        cnn.commit()
        print(cursor.rowcount)
        cursor.close()
    except Exception as e:
        print(e)
        cnn.rollback()


def insert_login_check(member_no):
    try:
        code = create_md5()
        cursor = cnn.cursor()
        sql_query = f"""insert into `member_test3`.`login_check` ( `CODE`, `MEMBER_NO`, `MEMBER_TYPE`, `LOCK_STATUS`, 
        `LAST_LOGIN_DATE`, `CYCLE_LOGIN_FAIL_TIMES`, `LAST_LOGIN_ERROR_DATE`, `UPDATE_ID`, `UPDATE_DATE`) 
        values 
        ( '{code}', 'LJ_{member_no}', 'GUID', 'NORMAL', null, '0', 
        '2019-05-28 15:38:56', null, null);"""
        print("insert sql=========>", sql_query)
        cursor.execute(sql_query)
        cnn.commit()
        print(cursor.rowcount)
        cursor.close()
    except Exception as e:
        print(e)


def create_md5():
    """通过MD5的方式创建"""
    m = hashlib.md5()
    m.update(bytes(str(time.time()), encoding='utf-8'))
    return m.hexdigest()


def get_phone():
    cursor = cnn.cursor()
    sql_query = "SELECT guid_member.MOBILE FROM guid_member WHERE MERCHANT_NO='d6acf1e2e75d4027a8204b1c670aaa31'"
    print("insert sql=========>", sql_query)
    cursor.execute(sql_query)
    row_1 = cursor.fetchall()
    cursor.close()
    return row_1


def get_token(phone):
    url = "https://juke-test3.kuick.cn/api/member/h5Login.do"
    body = {"paramJson": "{\"mobile\":\"%s\",\"pwd\":\"24wNpibh\",\"clientmethod\":\"pc-web\",\"clientId\":1,\"appKey\":\"juke_im-pc_web\"}" % phone, "appKey": "juke_im-pc_web"}
    res = requests.post(url=url, data=body)
    datas = json.loads(res.text)
    print(datas['returnObject']['token'])


if __name__ == '__main__':
    a = get_phone()
    print(len(a))
    for phone in a:
        get_token(phone[0])

    # loop.run_until_complete(start_server())
    # for i in range(10000):
    #     #     print(f"=========={i}")
    #     #     member_no = create_md5()
    #     #     insert_member_no(i, member_no)
    #     #     insert_login_check(member_no)


# {
# "order_no":"123123123123",
# "order_status":"0",
# "timestamp":"1560947935",
# "deal_user_id":"1f73889b-3a9a-46b4-b30d-805a684f44f7",
# "sign":"422F19073816E0608FF58F9C3380EC6D"
# }
#
#
# curl -v "http://127.0.0.1:8080/api/health/status"


