import redis

#crear una connexion con la instancia del servidor local de redis
# por default corren en puerto 6379
redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
redis_db.keys()
redis_db.set("redis","Esta funcionando!")
redis_db.keys()
redis_db.get("redis")
redis_db.incr("visitas")
redis_db.get("visitas")
