- Files

  `text_similarity.py` Library for compute text similarity

  `text_similarity_server.py` Server for compute text similarity

- Run Server
```
gunicorn text_similarity_server:__hug_wsgi__
```

- Build docker image
```
docker build image -t ts .
```

- Run server using docker

```
docker run -p 8000:8000 ts
```

- Query example

Put two texts in the body with parameter names as text1 and text2.
```
curl -X POST -d '{"text1": "a b c", "text2":"a c b"}' -H "Accept: application/json" -H "Content-type: application/json" 127.0.0.1:8000
```
