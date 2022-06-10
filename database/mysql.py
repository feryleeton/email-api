import mysql.connector

import config


class Database:
    def __init__(self):
        self.conn_writer = mysql.connector.connect(host=config.DB_ENDPOINT_WRITER, user=config.DB_USER,
                                                   passwd=config.DB_PASSWORD, port=config.DB_PORT,
                                                   database=config.DB_NAME)

    def get_random_proxy(self):
        cur_writer = self.conn_writer.cursor(buffered=True)

        query = ("SELECT *  FROM proxies WHERE active = 1 ORDER BY RAND()")

        cur_writer.execute(query)
        proxy = cur_writer.fetchone()

        cur_writer.close()

        return proxy

    def get_proxy_by_ip(self, ip):
        cur_writer = self.conn_writer.cursor(buffered=True)

        query = ("SELECT *  FROM proxies WHERE ip = (%s)")

        cur_writer.execute(query, (ip, ))
        proxy = cur_writer.fetchone()

        cur_writer.close()

        return proxy
