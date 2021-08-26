import pymysql

def get_monthly_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT DATE_FORMAT(sdate, '%m') AS `month`, 
            SUM(revenue) AS revenue, SUM(profit) AS profit
            FROM sales_book
            GROUP BY `month`
            ORDER BY `month`;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

def get_company_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    
    sql = '''
        SELECT scompany, pname, sunit
        FROM sales_book
        ORDER BY scompany;
    '''

    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

def get_name_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql="""
        SELECT pname AS `product`,
        SUM(sunit) AS total_unit, SUM(revenue) AS revenue, SUM(profit) AS profit
        FROM sales_book
        GROUP BY `product`
        ORDER BY `product`
    """

    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

def get_category_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = '''
        SELECT pcategory AS `category`,
        SUM(revenue) AS revenue, SUM(profit) AS profit
        FROM sales_book
        GROUP BY `category`
        ORDER BY `category`;
    '''
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results