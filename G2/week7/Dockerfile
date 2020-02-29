FROM mongo

COPY data.json /data.json  
CMD mongoimport --host mongodb --db test --collection restaurants --drop --file /data.json  