zip -r9 function.zip extract.py
aws s3 cp function.zip s3://maitreyaverma/
aws lambda update-function-code --function-name newsFunction --s3-key function.zip --s3-bucket maitreyaverma
aws lambda invoke --function-name newsFunction temp --log-type Tail --query 'LogResult' --output text |  base64 -d
