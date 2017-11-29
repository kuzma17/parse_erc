#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql
import cgi
import os

class ErcFunction:

    __host = '127.0.0.1'
    __user = 'root'
    __password = '170270'
    __database = 'parse_erc'
    __session = None
    __connection = None

    def open(self):
        try:
            #con = MySQLdb.connect(self.__host, self.__user, self.__password, self.__database)
            con = pymysql.connect(self.__host, self.__user, self.__password, self.__database, charset='utf8', use_unicode=False)
            self.__connection = con
            self.__session = con.cursor()
        except pymysql.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    def save(self):
        self.__connection.commit()

    def close(self):
        self.__session.close()
        self.__connection.close()
        ## End def close

    def vendor(self, name): # the test function
        sql = "SELECT id FROM erc_vendors WHERE name = %s"
        self.open()
        self.__session.execute(sql, [name])
        id = self.__session.fetchone()[0]
        self.close()
        return id

    def code_prom(self, category, sub_category, vendor):
        sql = "SELECT pc.id, pc.code, pc.status FROM erc_codes AS pc " \
              "LEFT JOIN erc_categories AS ct ON ct.id = pc.category_id " \
              "LEFT JOIN erc_sub_categories AS sc ON sc.id = pc.sub_category_id " \
              "LEFT JOIN erc_vendors AS v ON v.id = pc.vendor_id " \
              "WHERE ct.name = %s AND sc.name = %s AND v.name = %s LIMIT 1"
        self.__session.execute(sql, [category, sub_category, vendor])
        code = self.__session.fetchone()
        return code

    def update_status(self, id, status):
        if status == 'on':
            status = 1
        else:
            status = 0
        sql = "UPDATE erc_codes SET status = %s WHERE id = %s"
        self.__session.execute(sql, [status, id])

    def add_vendor(self, name):
        try:
            sql = "SELECT id FROM erc_vendors WHERE name = %s"
            self.__session.execute(sql, [name])
            id = self.__session.fetchone()[0]
        except:
            sql = "INSERT INTO erc_vendors SET name = %s"
            self.__session.execute(sql, [name])
            id = self.__session.lastrowid
        return id

    def add_category(self, name):
        try:
            sql = "SELECT id FROM erc_categories WHERE name = %s"
            self.__session.execute(sql, [name])
            id = self.__session.fetchone()[0]
        except:
            sql = "INSERT INTO erc_categories SET name = %s"
            self.__session.execute(sql, [name])
            id = self.__session.lastrowid
        return id

    def add_subcategory(self, name):
        try:
            sql = "SELECT id FROM erc_sub_categories WHERE name = %s"
            self.__session.execute(sql, [name])
            id = self.__session.fetchone()[0]
        except:
            sql = "INSERT INTO erc_sub_categories SET name = %s"
            self.__session.execute(sql, [name])
            id = self.__session.lastrowid
        return id

    def add_code(self, vendor_id, category_id, subcategory_id, code, status='None'):
        if status == 'on':
            status = '1'
        else:
            status = '0'
        sql = "INSERT INTO erc_codes (vendor_id, category_id, sub_category_id, code, status) VALUE(%s, %s, %s, %s, %s)"
        self.__session.execute(sql, [vendor_id, category_id, subcategory_id, code, status])

    def prices(self, ddp, par, sprice, rprice, curr):
        sql = "SELECT a.value FROM erc_arguments AS a LEFT JOIN erc_categories AS ct ON ct.id = a.category_id  WHERE ct.name = %s"
        self.__session.execute(sql, [par])
        parr = self.__session.fetchone()[0]
        ddp = int(ddp)
        param = float(parr)
        sprice = float(sprice)
        rprice = float(rprice)
        curr = float(curr)
        if ddp == 0:
            currency = curr
        else:
            currency = 1
        price = round(sprice * currency * param, 0)
        price_res = max(price, rprice)
        return str(parr)

    def catalogs(self):
        sql = "SELECT * FROM erc_codes"
        self.__session.execute(sql)
        cat = self.__session.fetchall()
        return cat

    def categories(self):
        sql = "SELECT * FROM erc_categories"
        self.__session.execute(sql)
        categories = self.__session.fetchall()
        return categories

    def category(self, id):
        sql = "SELECT * FROM erc_categories WHERE id = %s"
        self.__session.execute(sql, [id])
        category = self.__session.fetchone()
        return category

    def edit_category(self, id, name):
        sql = "UPDATE erc_categories SET name = %s WHERE id = %s"
        self.__session.execute(sql, [name, id])

    def dell_category(self, id):
        sql = "DELETE FROM erc_categories WHERE id = %s"
        self.__session.execute(sql, [id])
