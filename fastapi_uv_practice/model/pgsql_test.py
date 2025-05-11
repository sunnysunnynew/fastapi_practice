import psycopg
import psycopg_pool
from config import config

pool_default = psycopg_pool.ConnectionPool(
    config.PGSQL_TEST_DATABASE_STRING,
    min_size = config.PGSQL_TEST_POOL_MIN_SIZE,
    max_size = config.PGSQL_TEST_POOL_MAX_SIZE,
    max_idle = config.PGSQL_TEST_POOL_MAX_IDLE,

)

# def list_admin():
#     with pool_default.connection() as conn:
#         cur = conn.cursor(row_factory=psycopg.rows.dict_row)
        
#         try:
#             results = cur.execute("SELECT * FROM TB_ADMIN").fetchall()
#         except psycopg.OperationalError as err:
#             print(f'Error querying: {err}')
#         except psycopg.ProgrammingError as err:
#             print("database error via psycopg. %s",err)
#             results = False
#         except psycopg.IntergrityError as err:
#             print('PostgreSQL intergrity error as via psycopg %s', err)
#             results = False
            
#     return results


def list_admin():
    with pool_default.connection() as conn:
        cur = conn.cursor(row_factory=psycopg.rows.dict_row)
        
        try:
            cur.execute("CALL SP_L_ADMIN('out1')")
            results = cur.execute("FETCH ALL FROM out1").fetchall()
            conn.commit()
        except psycopg.OperationalError as err:
            print(f'Error querying: {err}')
        except psycopg.ProgrammingError as err:
            print("database error via psycopg. %s",err)
            results = False
        except psycopg.IntergrityError as err:
            print('PostgreSQL intergrity error as via psycopg %s', err)
            results = False
            
    return results