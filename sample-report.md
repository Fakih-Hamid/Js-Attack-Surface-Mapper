# JS Attack Surface Map

## Endpoints by domain

### unknown
- `post` [public] (GraphQL) (src: examples\sample.js)

### api.example.com
- `https://api.example.com/v1/admin/impersonate` [auth-required] (GraphQL) (src: examples\sample.js)
- `https://api.example.com/v1/users?id=123&debug=true` [idor-candidate] (GraphQL) (src: examples\sample.js)

### ws.example.com
- `wss://ws.example.com/socket` [public] (GraphQL) (src: examples\sample.js)

## Parameters

- `id`=123 (query) -> https://api.example.com/v1/users?id=123&debug=true (src: examples\sample.js)
- `debug`=true (query) -> https://api.example.com/v1/users?id=123&debug=true (src: examples\sample.js)
- `id`=123 (query-fragment) -> n/a (src: examples\sample.js)
- `debug`=true (query-fragment) -> n/a (src: examples\sample.js)
- `apiKey`=AKIA_TEST_KEY_1234567890 (query-fragment) -> n/a (src: examples\sample.js)

## Secrets & tokens

- [jwt] `api.example.com/v1/users` (src: examples\sample.js)
- [jwt] `api.example.com/v1/admin/impersonate` (src: examples\sample.js)
- [jwt] `ws.example.com/socket` (src: examples\sample.js)
- [authorization-header] `Authorization: "Bearer test-token-abc123` (src: examples\sample.js)