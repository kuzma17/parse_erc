#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import MySQLdb

class ErcFunction:

    __host = '127.0.0.1'
    __user = 'root'
    __password = '170270'
    __database = 'parse_erc'
    __session = None
    __connection = None

    def open(self):
        try:
            con = MySQLdb.connect(self.__host, self.__user, self.__password, self.__database, charset='utf8', use_unicode=False)
            self.__connection = con
            self.__session = con.cursor()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    def save(self):
        self.__connection.commit()

    def close(self):
        self.__session.close()
        self.__connection.close()

    def code_prom(self, category, sub_category, vendor):
        sql = "SELECT pc.id, pc.code, pc.status FROM erc_codes AS pc " \
              "LEFT JOIN erc_categories AS ct ON ct.id = pc.category_id " \
              "LEFT JOIN erc_subcategories AS sc ON sc.id = pc.sub_category_id " \
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
            sql = "SELECT id FROM erc_subcategories WHERE name = %s"
            self.__session.execute(sql, [name])
            id = self.__session.fetchone()[0]
        except:
            sql = "INSERT INTO erc_subcategories SET name = %s"
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

    def argument(self, par):
        sql = "SELECT op.value FROM erc_options AS op LEFT JOIN erc_categories AS ct ON ct.id = op.category_id  WHERE ct.name = %s"
        self.__session.execute(sql, [par])
        arg = self.__session.fetchone()[0]
        return arg

    def currency(self):
        sql = "SELECT op.value FROM erc_options AS op WHERE op.key = 'currency'"
        self.__session.execute(sql)
        curr = self.__session.fetchone()[0]
        return curr

    def currency_edit(self, curr):
        curr = curr.replace(',', '.')
        curr = round(float(curr), 2)
        sql = "UPDATE erc_options AS op SET op.value = %s WHERE op.key = 'currency'"
        self.__session.execute(sql, [curr])

    def catalogs(self):
        sql = "SELECT * FROM erc_codes"
        self.__session.execute(sql)
        cat = self.__session.fetchall()
        return cat

    def cat_list(self, table):
        sql = "SELECT * FROM "+table
        self.__session.execute(sql)
        cat = self.__session.fetchall()
        return cat

    def cat(self, table, id):
        sql = "SELECT * FROM "+table+" WHERE id = %s"
        self.__session.execute(sql, [id])
        cat = self.__session.fetchone()
        return cat

    def cat_edit(self, table, id, name):
        sql = "UPDATE "+table+" SET name = %s WHERE id = %s"
        self.__session.execute(sql, [name, id])

    def cat_dell(self, table, id):
        sql = "DELETE FROM "+table+" WHERE id = %s"
        self.__session.execute(sql, [id])

    def cat_add(self, table, name):
        sql = "INSERT INTO "+table+" SET name = %s"
        self.__session.execute(sql, [name])

    def code_list(self):
        sql = "SELECT c.id, ct.name, sc.name, v.name, pc.code, pc.title, c.status FROM erc_codes AS c " \
              "LEFT JOIN erc_categories AS ct ON ct.id = c.category_id " \
              "LEFT JOIN erc_subcategories AS sc ON sc.id = c.sub_category_id " \
              "LEFT JOIN erc_vendors AS v ON v.id = c.vendor_id " \
              "LEFT JOIN erc_promcats AS pc ON pc.id = c.promcat_id"
        self.__session.execute(sql)
        codes = self.__session.fetchall()
        return codes

    def code_edit(self, category, subcategory, vendor, code, parent_code, title, status, id):
        sql = "UPDATE erc_codes SET category_id = %s, sub_category_id = %s, vendor_id = %s, code = %s, parent_code = %s, title = %s, status = %s WHERE id = %s"
        self.__session.execute(sql, [category, subcategory, vendor, code, parent_code, title, status, id])

    def code_add(self, category, subcategory, vendor, code, parent_code, title, status):
        sql = "INSERT INTO erc_codes SET category_id = %s, sub_category_id = %s, vendor_id = %s, code = %s, parent_code = %s, title = %s, status = %s"
        self.__session.execute(sql, [category, subcategory, vendor, code, parent_code, title, status])

    def option_edit(self, key, value_cat):
        value_cat = value_cat.replace(',', '.')
        sql = "UPDATE erc_options AS o SET o.value = %s WHERE o.key = %s"
        self.__session.execute(sql, [value_cat, key])

    def save_xml_set(self, form):
        new_currency = form.getvalue('currency')
        categories = form.getlist("category")
        new_categories = form.getlist("new_category")
        new_vendor = form.getlist("add_vendor")
        new_category = form.getlist("add_category")
        new_subcategory = form.getlist("add_subcategory")

        if new_currency:
            self.currency_edit(new_currency)

        for category in categories:
            status = form.getvalue('status[' + category + ']')
            self.update_status(category, status)

        for new_id in new_categories:
            vendor_id = self.add_vendor(new_vendor[int(new_id)])
            category_id = self.add_category(new_category[int(new_id)])
            subcategory_id = self.add_subcategory(new_subcategory[int(new_id)])
            code = form.getvalue('add_code[' + new_id + ']')
            status = form.getvalue('add_status[' + new_id + ']')

            if code:
                self.add_code(vendor_id, category_id, subcategory_id, code, status)

    def country_ru(self, name_ua):
        sql = "SELECT name_ru FROM erc_countries WHERE name_ua = %s"
        self.__session.execute(sql, [name_ua])
        name_ru = self.__session.fetchone()[0]
        return name_ru

    def prom_edit(self, id, code, parent_code, title):
        sql = "UPDATE erc_promcats SET code = %s, parent_code = %s, title = %s WHERE id = %s"
        self.__session.execute(sql, [code, parent_code, title, id])

    def prom_add(self, code, parent_code, title):
        sql = "INSERT INTO erc_promcats SET code = %s, parent_code = %s, title = %s "
        self.__session.execute(sql, [code, parent_code, title])

    def prom_code_list123(self, code):
        sql = "SELECT id, code FROM erc_promcats WHERE code = %s"
        self.__session.execute(sql, [code])
        cat = self.__session.fetchone()
        return cat

    def prom_code_list_save(self, code_id, code):
        sql = "UPDATE erc_codes SET promcat_id = %s WHERE code = %s"
        self.__session.execute(sql, [code_id, code])