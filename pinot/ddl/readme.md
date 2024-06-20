# Submit Schema and Tables through Pinot's API

```sh
kubectl port-forward svc/pinot-controller 9000:9000 -n datastore

curl -X POST \
  -H "Content-Type: application/json" \
  -d @schema_enriched_orders.json \
  http://localhost:9000/schemas


curl -X POST \
  -H "Content-Type: application/json" \
  -d @table_enriched_orders.json \
  http://localhost:9000/tables

```


# Read data through Pinot's API

```sh
kubectl port-forward svc/pinot-broker 8099:8099 -n datastore

curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "sql": "select count(1), sum(total_amount), city from enriched_orders where request_time > toDateTime(now() - 60 * 60 * 1000, '\''yyyy-MM-dd HH:mm:ss Z'\'') group by city order by count(*) desc"
      }' \
  http://localhost:8099/query/sql


curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "sql": "select sum(total_amount) from enriched_orders where request_time > toDateTime(now() - 60 * 60 * 1000, '\''yyyy-MM-dd HH:mm:ss Z'\'')"
      }' \
  http://localhost:8099/query/sql


curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "sql": "select sum(total_amount) from enriched_orders where request_time > toDateTime(now() - 60 * 60 * 1000, '\''yyyy-MM-dd HH:mm:ss Z'\'')"
      }' \
  http://localhost:8099/query/sql


curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "sql": "select count(1), state from enriched_orders where request_time > toDateTime(now() - 60 * 60 * 1000, '\''yyyy-MM-dd HH:mm:ss Z'\'') group by state"
      }' \
  http://localhost:8099/query/sql


```


