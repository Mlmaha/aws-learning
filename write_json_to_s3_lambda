import json, boto3

json_data = {
    'dummy': 'se',
    'message': 'success'
}
s3 = boto3.resource('s3')
object = s3.Object('BUCKET', 'test/sample.json')
object.put(Body=json.dumps(json_data))
