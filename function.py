#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import MySQLdb
import cgi
import os

class ErcFunction:

    __host = '127.0.0.1'
    __user = 'root'
    __password = '170270'
    __database = 'parse_erc'
    __session = None
    __connection = None

    def __open(self):
        try:
            cnx = MySQLdb.connect(self.__host, self.__user, self.__password, self.__database, 'utf8')
            self.__connection = cnx
            self.__session = cnx.cursor()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    def __close(self):
        self.__session.close()
        self.__connection.close()
        ## End def __close

    def vendor(self, name):
        sql = "SELECT id FROM erc_vendors WHERE name = %s"
        self.__open()
        self.__session.execute(sql, [name])
        id = self.__session.fetchone()[0]
        self.__close()
        return id
