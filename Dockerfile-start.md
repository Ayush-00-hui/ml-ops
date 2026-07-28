# Docker Setup & Launch Guide

Build Docker Image:
```bash
docker build -t house-price:v1 -f Dockerfile .
```

Run Docker Container:
```bash
docker run -d -p 1234:1234 --name house-api house-price:v1
```

Test Invocations:
```bash
curl -X POST http://127.0.0.1:1234/invocations \
-H "Content-Type: application/json" \
-d '{
  "dataframe_records": [
    {
      "LotArea": 9000,
      "OverallQual": 7,
      "OverallCond": 5,
      "YearBuilt": 2010,
      "GrLivArea": 1900,
      "GarageCars": 2
    }
  ]
}'
```
