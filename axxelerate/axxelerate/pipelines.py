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

    def process_item(self, item, spider):
        try:
            with self.connection.cursor() as cursor:
                sql_url_filter = "SELECT `ID` FROM pages WHERE `url` = %s"
                cursor.execute(sql_url_filter, item['url'])

                pageID = 0
                result = cursor.fetchone()
                if (result == None):
                    sql_url_title = "INSERT INTO `pages` (`url`, `title`) VALUES (%s, %s)"
                    cursor.execute(sql_url_title, (item['url'], item['title']))
                    pageID = cursor.lastrowid
                else:
                    pageID = result["ID"]

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

        except pymysql.OperationError as e:
            print("caught pymysql.OperationError: ")
            print(e)
            if e.errno == 2006:
                print("reconnecting to DB")
                connectToDb()
                process_item(self, item, spider)
        except: 
            print("GGGGRRRRRRRRRRRRRRRRRRRR")
            pass
        return item
