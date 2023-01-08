import boto3


def main(event, context):

    rds = boto3.client('rds', region_name='ap-east-1')

    action = event.get('action', None)
    dbIdentifier = event.get('dbIdentifier', None)
    if 'start' == action and dbIdentifier:
        try:
            result = rds.start_db_cluster(DBClusterIdentifier=dbIdentifier)
            print('Start DB: %s, result: %s' % (dbIdentifier, result))
        except Exception as e:
            print(e)
    elif 'stop' == action and dbIdentifier:
        try:
            result = rds.stop_db_cluster(DBClusterIdentifier=dbIdentifier)
            print('Stop DB: %s, result: %s' % (dbIdentifier, result))
        except Exception as e:
            print(e)
    else:
        print('Please input the start or stop action.')
