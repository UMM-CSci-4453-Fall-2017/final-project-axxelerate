import pymysql.cursors
import credentials



class AxxeleratePipeline(object):

    def __init__(self):
        print("init AxxeleratePipeline")
        self.connectToDb()

    def connectToDb(self):
        self.connection = pymysql.connect(host = credentials.host,
                                     user = credentials.user,
                                     password = credentials.password,
                                     db = credentials.db,
                                     cursorclass = pymysql.cursors.DictCursor)

    def insert_url(self, url, cursor):
        sql_url_filter = "SELECT `ID` FROM pages WHERE `url` = %s"
        cursor.execute(sql_url_filter, url)
        pageID = 0
        result = cursor.fetchone()
        if (result == None):
            sql_url_title = "INSERT INTO `pages` (`url`) VALUES (%s)"
            cursor.execute(sql_url_title, (url))
            pageID = cursor.lastrowid
        else:
            pageID = result["ID"]
        return pageID

    def process_item(self, item, spider):
        try:
            with self.connection.cursor() as cursor:

                pageID = self.insert_url(item['url'], cursor)
                sql_url_title = "UPDATE `pages` SET `title` = %s WHERE `ID` = %s"
                cursor.execute(sql_url_title, (item['title'], pageID))

                placeHolders = []
                valuesToInsert = []

                for word in item['keywords']:
                    valuesToInsert.append(word)
                    valuesToInsert.append(pageID)
                    placeHolders.append("(%s,%s)")

                if len(placeHolders) > 0:
                    sql_keywords = "INSERT INTO `keywords` (`word`, `pageID`) VALUES " + (",".join(placeHolders))
                    cursor.execute(sql_keywords, valuesToInsert)

            self.connection.commit()

        except pymysql.OperationalError as e:
            print("caught pymysql.OperationError: ")
            print(e)
            if e.errno == 2006:
                print("reconnecting to DB")
                connectToDb()
                process_item(self, item, spider)
        except Exception as e: 
            print("GGGGRRRRRRRRRRRRRRRRRRRR")
            print(e)
            pass
        return item
