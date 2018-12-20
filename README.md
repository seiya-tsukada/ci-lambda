# ci-lambda

## pip install

## to zip

```
zip -r /tmp/output.zip ./*
```

## zip upload to lambda

```
aws lambda \
update-function-code \
--function-name [function_name] \
--zip-file fileb:///tmp/output.zip \
--publish \
--region ap-northeast-1
```
