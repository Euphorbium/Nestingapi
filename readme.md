# Solution to the sql tasks

## Task 1
```
SELECT t.user_id, sum(t.amount*coalesce(er.rate,1)) AS total_spent_gbp  
FROM transactions t LEFT JOIN exchange_rates er 
ON er.from_currency = t.currency AND er.to_currency = 'GBP'
WHERE er.ts = (SELECT max(ts) FROM exchange_rates ee WHERE ee.from_currency = t.currency) OR er.ts IS NULL
GROUP BY t.user_id
ORDER BY t.user_id ASC;
```

## Task 2

```
SELECT t.user_id, sum(t.amount*coalesce(er.rate,1)) AS total_spent_gbp
FROM transactions t LEFT JOIN exchange_rates er 
ON er.from_currency = t.currency AND er.to_currency = 'GBP'
WHERE er.ts = (select max(ts) FROM exchange_rates ee WHERE ee.from_currency = t.currency AND ee.ts <= t.ts) OR er.ts IS NULL
GROUP BY t.user_id
ORDER BY t.user_id ASC;
``` 

# Python tasks

first install requirements, then run app.py 

The command line interface is used like `cat input.json | python nest.py currency country city`

There is a hardcoded api user with a username `testuser` and password `badpassword`
api call example
``` 
curl --request POST \
  --url 'http://127.0.0.1:5000/nest/?currency=&country=&city=' \
  --header 'authorization: Basic dGVzdHVzZXI6YmFkcGFzc3dvcmQ=' \
  --header 'content-type: application/json' \
  --data '[
  {
    "country": "US",
    "city": "Boston",
    "currency": "USD",
    "amount": 100
  },
  {
    "country": "FR",
    "city": "Paris",
    "currency": "EUR",
    "amount": 20
  },
  {
    "country": "FR",
    "city": "Lyon",
    "currency": "EUR",
    "amount": 11.4
  },
  {
    "country": "ES",
    "city": "Madrid",
    "currency": "EUR",
    "amount": 8.9
  },
  {
    "country": "UK",
    "city": "London",
    "currency": "GBP",
    "amount": 12.2
  },
  {
    "country": "UK",
    "city": "London",
    "currency": "FBP",
    "amount": 10.9
  }
]'
```