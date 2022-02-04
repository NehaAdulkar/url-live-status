#!/usr/bin/python3
import argparse, requests

parser = argparse.ArgumentParser(description="Tool to whether check URL is accessible")
parser.add_argument("-f", type=str, help="enter file", required=True)
parser.add_argument("-o", type=str, help="enter output file")

try:
    
    a = parser.parse_args()
    #print(a.f)
    with open(a.f, "r") as j:
        for i in j.readlines():
            #print(i)
            i=i.replace("\n", "")
            page = requests.get(i)
            print("{} : [ {} ]\n".format(i, page.status_code))
            if a.o:
                with open(a.o, "a") as op:
                    op.write("{} : [ {} ]".format(i, page.status_code))

except Exception as e:
    print("Mess !!", e)
