# Winter Supplement Rules Engine

## Setup

1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`.

## Usage

1. Update `.env` with the correct `<MQTT_TOPIC_ID>` from the web calculator.
2. Run the program: `python main.py`.

## Running Tests

Run tests using:

```bash
 python -m pytest .\\rules_engine\\tests\\rules_engine_tests.py
```

The tests are parameterized and covers all the test cases mentioned in the problem statement.
