from django.db import connection
from django.db.models import QuerySet


def get_sql(qs: QuerySet):
    sql, params = qs.query.sql_with_params()
    cursor = connection.cursor()
    cursor.execute('EXPLAIN ' + sql, params)
    pure_sql: str = cursor.db.ops.last_executed_query(cursor, sql, params)

    return pure_sql


def print_result(qs: QuerySet):
    for x in qs:
        print(x)
