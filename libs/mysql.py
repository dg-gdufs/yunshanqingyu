# encoding: utf-8

import pymysql

class Mysql():
    '''
    用于链接mysql数据库的工具类
    '''

    db = None
    cur = None

    def __init__(self, db_config):
        self.db = pymysql.connect(
            host=db_config['host'],
            port=db_config['port'],
            user=db_config['user'],
            password=db_config['password'],
            db=db_config['db'],
            charset='utf8mb4',
            read_timeout=30,
            write_timeout=30
        )
        self.cur = self.db.cursor()

    def __del__(self):
        self.cur.close()
        self.db.close()

    def insert(self, table, keys, values):
        '''
        sql语句insert
        '''
        values_num = []
        for i in values:
            values_num.append(r'%s')
        sql = "insert into {} ({}) values ({})".format(table, ','.join(keys), ','.join(values_num))
        self.cur.execute(sql, values)
        self.db.commit()

    def select(self, sql):
        '''
        sql语句select
        '''
        self.cur.execute(sql)
        return self.cur.fetchall()


    def update(self, table, set_keys, set_values, get_keys=[], get_values=[]):
        sql = "update {} set {}".format(table, ','.join([i + r' = %s' for i in set_keys]))
        if get_keys and get_values:
            sql += " where {}".format(' and '.join([i + r' = %s' for i in get_keys]))
            set_values.extend(get_values)
        self.cur.execute(sql, set_values)
        self.db.commit()

    def execute(self, sql):
        '''
        sql语句其他
        '''
        self.cur.execute(sql)
        self.db.commit()