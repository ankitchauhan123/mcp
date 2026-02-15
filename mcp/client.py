import json
import subprocess

def send_message(proc:subprocess.Popen,message:str):
    print(f"[Client Sending Message]: {message}")
    proc.stdin.write(message)
    proc.stdin.flush()

def get_response(proc: subprocess.Popen):
    message = proc.stdout.readline()
    print(f"[Server Sent Message]:{message}")

def get_proc():
    proc = subprocess.Popen(["python","server.py"],stdin=subprocess.PIPE,stdout=subprocess.PIPE, text= True)
    return proc


def run_client():
    proc = get_proc()
    #case 1
    send_message(proc,"hello\n")
    get_response(proc)


    #case 2
    list_tools_message= {
        "jsonrpc":"2.0",
        "id" : 1,
        "method": "tools/list",
        "params": {}
    }

    send_message(proc,json.dumps(list_tools_message)+'\n')
    get_response(proc)


    #case 3
    send_message(proc,"exit\n")
    get_response(proc)
    proc.stdin.close()
    exit_code= proc.wait()
    print(f"Process Exited With Code: {exit_code}")




run_client()






