import pymysql.cursors
import credentials

connection = pymysql.connect(host = credentials.host,
                                 user = credentials.user,
                                 password = credentials.password,
                                 db = credentials.db,
                                 cursorclass = pymysql.cursors.DictCursor)


class AxxeleratePipeline(object):
    def process_item(self, item, spider):
        try:
            with connection.cursor() as cursor:
                sql_url_title = "INSERT INTO `pages` (`url`, `title`) VALUES (%s, %s)"
                cursor.execute(sql_url_title, (item['url'], item['title']))

                pageID = cursor.lastrowid

                placeHolders = []
                valuesToInsert = []

                for word in item['keywords']:
                    valuesToInsert.append(word)
                    valuesToInsert.append(pageID)
                    placeHolders.append("(%s,%s)")

                if len(placeHolders) > 0:
                    sql_keywords = "INSERT INTO `keywords` (`word`, `pageID`) VALUES " + (",".join(placeHolders))
                    cursor.execute(sql_keywords, valuesToInsert)

            connection.commit()

        except:
            pass
        return item
