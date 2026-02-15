import sys
import json


#sends messages back to client
def send_message(message):
    print(message)
    sys.stdout.flush()


#server that listens to messages - json or normal and takes action
def start_server():
    for line in sys.stdin:
        message = line.strip()
        # case 1: Its just a simple hello
        if message == "hello":
            send_message("Hello There")
            continue
        if message == "exit":
            send_message("Ok, Exiting...")
            sys.stdout.flush()
            break
        #only option left is json message else exception
        try:
            json_message = json.loads(message)
            if json_message['jsonrpc']=="2.0":
                method = json_message['method']
                msg_id = json_message["id"]
                if method == "tools/list":
                    response = {
                        "jsonrpc":"2.0",
                        "id":msg_id,
                        "tools/list":[
                            {"name":"tool1","description": "first tool"},
                            {"name":"tool2","description": "second tool"}
                        ]
                    }
                    send_message(json.dumps(response))
            else:
                send_message(f"Unknown JSON Message:{message}")

        except json.JSONDecodeError:
            send_message(f'Error Parsing JSON Message:{message}')
            continue

start_server()
        
        

