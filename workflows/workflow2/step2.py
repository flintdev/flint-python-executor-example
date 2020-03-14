import time


def execute(handler):
    print("running workflow2 step2")
    path = "$.workflow2.step1.field1.field2"
    handler.flow_data.get(path)
    time.sleep(1)
