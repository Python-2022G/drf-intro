# drf-intro

## setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## endpoints

### GET /api/add?x=1&y=2

```json
{
  "result": 3
}
```

### GET /api/subtract?x=1&y=2

```json
{
  "result": -1
}
```

### GET /api/multiply?x=1&y=2

```json
{
  "result": 2
}
```

### GET /api/divide?x=1&y=2

```json
{
  "result": 0.5
}
```

### POST /api/add

```json
{
  "a": 1,
  "b": 2,
}
```

```json
{
  "result": 3
}
```

### POST /api/subtract

```json
{
  "a": 1,
  "b": 2,
}
```

```json
{
  "result": -1
}
```

### POST /api/multiply

```json
{
  "a": 1,
  "b": 2,
}
```

```json
{
  "result": 2
}
```

### POST /api/divide

```json
{
  "a": 1,
  "b": 2,
}
```

```json
{
  "result": 0.5
}
```
