# osbee
Utilities for OSBee-3.0 device from OpenSprinkler

The OSBeeAPI class wraps an async client of the OSBee REST API to make it look like a few
independent valves.  Essentially split off from my HomeAssistant integration.


## Can I talk to my OSBee?

My personal OSBee is a v1.0.0; I've been chatting with someone whose v1.0.2 behaves a bit
differently.  examples/dump_status.py can be used to connect to an OSBee and see if we can read the
status of the valves and the OSBee in general.

    python3 -m venv osbee_testing
    source osbee_testing/bin/activate
    pip install osbee
    python3 examples/dump_status.py
    deactivate

You *should* see the status of your OSBee dumped out:

    $ python3 examples/dump_status.py
    type of timeout/max_runtime is <class 'int'>
    created OSBeeAPI at 192.168.0.1 max_runtime 30 (<class 'int'>)
    {
        "cid": 5437235,
        "fwv": 100,
        "mac": "C45BBE123456",
        "mnp": 6,
        "name": "My OSBee WiFi",
        "np": 0,
        "nt": 0,
        "pid": -1,
        "prem": 0,
        "rssi": -59,
        "sot": 1,
        "tid": -1,
        "trem": 0,
        "utct": 1716967540,
        "zbits": 0,
        "zons": [
            "Zone 1",
            "Zone 2",
            "Zone 3"
        ]
    }

If you see an exception and/or stack-trace, file an Issue in github and let's chat about it.
