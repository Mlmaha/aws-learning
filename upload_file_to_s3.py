def upload_to_aws(local_file, s3_file):
    s3 = boto3.client('s3')

    try:
        s3.upload_file(local_file, os.environ['BUCKET_NAME'], s3_file)
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': os.environ['BUCKET_NAME'],
                'Key': s3_file
            },
            ExpiresIn=24 * 3600
        )

        print("Upload Successful", url)
        return url
    except FileNotFoundError:
        print("The file was not found")
        return None
    except NoCredentialsError:
        print("Credentials not available")
        return None

#upload csv
def upload_csv(bucket):
    bucket_name = bucket
    s3_object = "test/reports.csv"
    os.chdir('/tmp')
    local_file_path = '/tmp/report.csv'
     s3.upload_file(
        local_file_path,
        bucket_name,
        s3_object,
        ExtraArgs={'ContentType': 'text/csv'}
    )


    return {
        'statusCode': 200,
        'body': json.dumps({'Please click on the link to download': 's3 link'})
    }
